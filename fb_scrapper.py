import traceback
from settings import _DEFAULT_BROWSER_SETTINGS
# Import Selenium Browser class
from selenium_wrapper.browser import Browser as SeleniumBrowser
# Import selenium functions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
# Another imports
import utils
from urllib.parse import urlparse

class Scrapper(object):
    
    _protocol = 'https'
    _hostname = 'm.facebook.com'
    _hostname_full = 'www.facebook.com'

    def __init__(self, username='', password='', **kwargs):
        """
            Example of settings in settings.py
        """
        # Default settings
        browser_settings = { **_DEFAULT_BROWSER_SETTINGS }
        # If kwargs have a custom browser settings
        if kwargs.get('browser', False):
            # Merge browser settings.
            browser_settings = { **browser_settings, **kwargs.get('browser') }
        # If kwargs have a custom remote settings
        if kwargs.get('remote', False):
            # Merge browser settings.
            browser_settings = { **browser_settings, **kwargs.get('remote') }
        # Instance the SeleniumBrowser
        self.selenium = SeleniumBrowser(**browser_settings)
        # Parse login url
        self.base_url = '{protocol}://{hostname}'.format(protocol=self._protocol, hostname=self._hostname)
        # If username and password are set.
        if username and password:
            # Login the username
            self.login(username, password)

    def close(self):
        """
            Close browser.
        """
        self.selenium.close()

    def login(self, username, password):
        """
            Enter to the login form.
            Arguments:
                - username: string
                - password: string
        """
        login_url = '{base_url}/login'.format(base_url=self.base_url)
        # Go to login page
        self.selenium.browser.get(login_url)
        try:
            # Check if not logged
            assert self.selenium.browser.current_url == login_url
            # Search login_form
            try:
                login_form = WebDriverWait(self.selenium.browser, 10).until(
                    EC.presence_of_element_located((By.ID, "login_form"))
                )
            finally:
                # Complete the email field.
                email_field = login_form.find_element_by_name('email')
                email_field.clear()
                email_field.send_keys(username)
                # Complete the password field.
                password_field = login_form.find_element_by_name('pass')
                password_field.clear()
                password_field.send_keys(password)
                # Send return
                password_field.send_keys(Keys.RETURN)
                self.selenium.sleep()
                try:
                    # If the url is not login
                    assert self.selenium.browser.current_url != login_url
                except AssertionError:
                    raise Exception('Login incorrect.')
        except AssertionError:
            pass

    def process_urls(self, urls, words, exclusive_words, have_phone=False, have_email=False, wait_page_load=5, scroll_down_amount=10, scroll_down_time=1):
        """
            Go through urls, for save wanted information
                Args:
                    - urls: list of urls (string[])
                    - words: list of words (string[])
                    - exclusive_words: if find all words (boolean)
                    - scroll_down_amount: scroll down times (integer)
                    - have_phone: the text have phone (boolean)
                    - have_email: the text have email (boolean)
                Returns:
                    A list of posts.
        """
        # Data
        posts = []
        # Loop the provided urls
        for url in urls:
            # Set random agent (browser)
            self.selenium.set_random_agent()
            posts_container = None
            # Formated URL
            self.selenium.browser.get(utils.replace_hostname(url, self._hostname))
            # Scroll down
            self.selenium.scroll_to_bottom(scroll_down_amount, scroll_down_time)
            # Set posible containers
            posts_containers_availables = [
                EC.presence_of_element_located((By.CLASS_NAME, "storyStream")), # Profiles and groups
                EC.presence_of_element_located((By.ID, "pages_msite_body_contents")), # Pages pages_msite_body_contents
            ]
            # Loop containers
            for container in posts_containers_availables:
                try:
                    # Get story stream.
                    posts_container = WebDriverWait(self.selenium.browser, wait_page_load).until(container)
                    break
                except (TimeoutException, WebDriverException):
                    pass
            # If search container found
            if not posts_container:
                raise Exception('Cannot find posts container.')
            # Search all posts
            articles = posts_container.find_elements_by_tag_name('article')
            # Loop the getted articles
            for article in articles:
                try:
                    # Get all post data
                    story_body_container = article.find_element_by_class_name('story_body_container')
                    header = story_body_container.find_element_by_tag_name('header')
                    content = story_body_container.find_elements_by_tag_name('p')
                    # ==========================================================================================
                    publisher = header.find_element_by_tag_name('strong').text
                    post = " ".join([line.text for line in content])
                    # CONTENT: get content
                    # ========= FILTER WORDS
                    valid = utils.valid_words(post, words, exclusive_words)
                    if not valid:
                        continue
                    # ========= FILTER PHONE
                    if have_phone and not utils.contains_phone(post):
                        # Skip this post
                        continue
                    # ========= FILTER EMAIL
                    if have_email and not utils.contains_email(post):
                        # Skip this post
                        continue
                    # Time element
                    # TODO: arreglar get post
                    time_element = header.find_element_by_xpath('.//div[@data-sigil="m-feed-voice-subtitle"]')
                    post_life = time_element.find_element_by_tag_name('abbr').text
                    post_url = time_element.find_element_by_tag_name('a').get_attribute('href')
                    # Parse URL witouth params
                    if post_url:
                        try:
                            post_url = urlparse(post_url)._replace(query='').geturl()
                        except:
                            pass
                        # Replace hostname with default
                        try:
                            post_url = utils.replace_hostname(post_url, self._hostname_full)
                        except:
                            pass
                    # Parse post datetime
                    try:
                        datetime = utils.parse_post_time(post_life)
                    except:
                        datetime = None
                        pass
                    # Save a dict with data
                    element = {
                        'publisher': publisher,
                        'datetime': datetime,
                        'content': post,
                        'searcher_url': url,
                        'post_url': post_url,
                    }
                    # Add element in global list
                    posts.append(element)
                except Exception as e:
                    error = traceback.format_exc()
                    print('Failed to get group post\nError: {error}'.format(error=error))
        return posts