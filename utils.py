from urllib.parse import urlparse
import re
from datetime import datetime, timedelta
import unidecode

def replace_hostname(url, hostname):
    """
        Replace hostname of url by another url hostname
        Arguments:
            - url
            - hostname
    """
    # Parse the URL recived
    parsed_url = urlparse(url)
    # Replace subdomain, domain name and top level domain 
    new_url = parsed_url._replace(netloc = hostname)
    return new_url.geturl()

def regex_search(text, pattern):
    """
        Search regex pattern in text.
    """
    # Return true if there is a phone number 
    value = False
    try:
        value = bool(re.search(pattern, text))
    except:
        pass
    return value


def valid_words(text, words, exclusive_words):
    """
        Search words in string.
        Arguments:
        
    """
    # Prevent execute witouth words
    if not len(words):
        return False
    # Text to lower and replace new lines in text.
    text = text.lower().replace('\n', ' ')
    # Remove accented characters
    text = unidecode.unidecode(text)
    # Remove non-alphabetic characters
    text = re.sub(r'[^a-zA-Z0-9,.\_\- ]', '', text)
    # Generate list with words valid/invalid.
    words_valid = [unidecode.unidecode(word.lower()) in text for word in words]
    # Get the custom function.
    func = all if exclusive_words else any
    # Returns boolean.
    return func(words_valid)

def contains_phone(content):
    """
        Search a ponhe number in content published.
        Phone number models:
            '341 3687111',
            '3462603099',
            '3462-(671583)',
            '3402 648224',
            '03462 15627084',
            '341-674975'
            '(2477)347127'

            Args:
                content: str

            Return:
                Boolean
    """
    # Return true if there is a phone number 
    return regex_search(content, r'[0-9]{2,5}[ |-]\(?\d{6,8}\)?|\(?\d{2,5}\)?\d{6,8}')

def contains_email(content):
    """
        Search a email in content published.
        Email models:
            sdfdsf_3444@dfggf.llt
            gtrgtAAAAAAABBBgfgF@dsfds.fd

            Args:
                content: str

            Return:
                Boolean
    """
    # Return true if there is a phone number 
    return regex_search(content, r'[a-zA-Z0-9_\-\.]+@\w+\.[a-zA-Z]{2,3}')

def parse_post_time(time_string, locale='es_ES'):
    """
        Function transforms string time Facebook to YYYY-mm-dd HH:MM:SS format.
        Examples:
            - time_string: 1 h
            - time_string: 19 m
    """
    # Equivalents to minutes
    equivalents = {
        'd': 60*24,
        'h': 60, # minutes
        'hour': 60, # minutes
        'hours': 60, # minutes
        'm': 1, # minutes
        'min': 1, # minutes
        'mins': 1, # minutes
        'minutes': 1, # minutes
    }
    value = None
    substract_now = 0
    date_time = None

    now = datetime.now()

    if time_string == 'Hace un momento':
        # Now
        substract_now = 1
    # Hours, Minutes, Days
    elif len(time_string.split(' ')) == 2:
        # 13 minutes | 2 hours
        time = time_string.split(' ')
        qty = int(time[0])
        u = time[1]
        substract_now = qty * equivalents[u]
    # Yesterday
    elif 'Ayer' in time_string:
        date_format = 'Ayer a las %H:%M'
        try:
            parsed_time = datetime.strptime(time_string, date_format)
            yesterday = now - timedelta(days=1)
            date_time = yesterday.replace(hour=parsed_time.hour, minute=parsed_time.minute, second=0)
        except:
            pass
    # Today
    elif 'Hoy' in time_string:
        date_format = 'Hoy a las %H:%M'
        try:
            parsed_time = datetime.strptime(time_string, date_format)
            date_time = now.replace(hour=parsed_time.hour, minute=parsed_time.minute, second=0)
        except:
            pass
    else:
        # Set available formats
        available_formats = ['%d de %B a las %H:%M', '%d de %B de %Y a las %H:%M']
        for format in available_formats:
            try:
                date_time = datetime.strptime(time_string, format)
                # If date has not year.
                if date_time.year == 1900:
                    # Replace year by current year.
                    date_time = date_time.replace(year=now.year)
                break
            except:
                pass
        pass
    
    # If substract time from now
    if substract_now:
        date_time = datetime.now() - timedelta(minutes=substract_now)
        value = date_time.strftime('%Y-%m-%d %H:%M:%S')
    
    # If specific date time
    if date_time:
        value = date_time.strftime('%Y-%m-%d %H:%M:%S')
    return value