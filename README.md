# python-fb-scrapper
### Python Facebook Scrapper based on functions of library [selenium-browser-random-agent](https://github.com/lshoobridge471/python-selenium-wrapper)

Scrapper developed in Python.

## Usage:

First, create credentials file (credentials are optional params):

```python
# credentials.py
credentials = {
    'email': 'youremail@yourdomain.com',
    'password': 'yourpassword',
}
```
Next, create the main file. Example: ```main.py```:
```python
from fb_scrapper import Scrapper

scrapper =  Scrapper(credentials['email'], credentials['password'])
```
## Methods
```python
# Class init method (username and password are optional)
# kwargs supports browser settings and open browser with settings and random agents custom:
"""
kwargs['browser'] = {
    'browser': {
        'data_dir': 'my-data',
        'window_size': '1024,768',
        'time_sleep': 5,
    },
    'agents': {
        'custom': 'Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36',
        'limit': 100,
        'random': True,
    },
}
"""
__init__(username='', password='', **kwargs)
# Close browser
close()
# Login in Facebook (automatic called in init of class)
login(username, password)
# Process URLS (groups/profiles/pages)
process_urls(self, urls, words, exclusive_words, have_phone=False, have_email=False, scroll_down_amount=10)
"""
process_urls Params:
- urls: list of urls (strings)
- words: list of words (strings)
- exclusive_words: all words are needed in post (boolean)
- have_phone: the post have a phone number (boolean)
- have_email: the post have a email (boolean)
- scroll_down_amount: number of go to bottom of page (integer)
- scroll_down_time: number of seconds wait to next scroll (integer)
"""
```
## Examples
Example ```GET POSTS``` of url's list:

```python
urls = [
    'https://www.facebook.com/groups/1626383370956138',
]
words = ['word1', 'word2', 'word3', 'word4', 'word5']
posts = scrapper.process_urls(urls, words)
```
Results of posts:
```json
[{'content': '⚡Escarchas para uñas HUDABEAUTY ⚡ $80 c/u Precio de contado\n'
             'Abonalo en efectivo o con tarjeta de crédito 💳',
  'datetime': '2019-08-25 23:47:00',
  'post_url': 'https://m.facebook.com/story.php?story_fbid=2375171789437267&id=2330857853868661&__tn__=-R',
  'publisher': 'Meraki makeup',
  'searcher_url': 'https://m.facebook.com/Meraki-makeup-2330857853868661'},
 {'content': '💧Esponjas tipo blender 💧 Ideales para darle un acabado natural a '
             'tu maquillaje diario\n'
             'Incluye espejo $80 c/u Precio de contado Abonalo en efectivo o '
             'con tarjeta de crédito 💳',
  'datetime': '2019-08-25 23:47:00',
  'post_url': 'https://m.facebook.com/story.php?story_fbid=2375171789437267&id=2330857853868661&__tn__=-R',
  'publisher': 'Meraki makeup',
  'searcher_url': 'https://m.facebook.com/Meraki-makeup-2330857853868661'},
 {'content': '🍌Polvo banana Pink 21🍌\n'
             'Sella correctores y base prolongando su duración\n'
             'Regula el exceso de grasa en la piel y le da un efecto '
             'aterciopelado. ⚠️Solo por encargue⚠️ $280 Precio de contado '
             'Abonalo en efectivo o con tarjeta de crédito 💳',
  'datetime': '2019-08-25 23:47:00',
  'post_url': 'https://m.facebook.com/story.php?story_fbid=2375171789437267&id=2330857853868661&__tn__=-R',
  'publisher': 'Meraki makeup',
  'searcher_url': 'https://m.facebook.com/Meraki-makeup-2330857853868661'},
 {'content': '🔸️Set de brochas ovaladas + limpia brochas + esponja tipo '
             'blender 🔸️ ⚠️Solo por encargue⚠️ $550 Precio de contado Abonalo '
             'en efectivo o con tarjeta de crédito 💳',
  'datetime': '2019-08-25 23:47:00',
  'post_url': 'https://m.facebook.com/story.php?story_fbid=2375171789437267&id=2330857853868661&__tn__=-R',
  'publisher': 'Meraki makeup',
  'searcher_url': 'https://m.facebook.com/Meraki-makeup-2330857853868661'},
 {'content': '🔹️Lapiz delineador de ojos y labios 🔹️ $35 c/u Precio de contado '
             'Abonalo en efectivo o con tarjeta de crédito 💳',
  'datetime': '2019-08-25 23:47:00',
  'post_url': 'https://m.facebook.com/story.php?story_fbid=2375171789437267&id=2330857853868661&__tn__=-R',
  'publisher': 'Meraki makeup',
  'searcher_url': 'https://m.facebook.com/Meraki-makeup-2330857853868661'},
 {'content': '🌸Brocha tipo blender mango largo🌸 $100 c/u Precio de contado\n'
             'Abonalo en efectivo o con tarjeta de crédito 💳',
  'datetime': '2019-08-25 23:47:00',
  'post_url': 'https://m.facebook.com/story.php?story_fbid=2375171789437267&id=2330857853868661&__tn__=-R',
  'publisher': 'Meraki makeup',
  'searcher_url': 'https://m.facebook.com/Meraki-makeup-2330857853868661'},
 {'content': 'Paleta de correctores PINK 21 📣 Amarillo, neutraliza tonos '
             'morados Verde, neutraliza enrojecimientos Durazno, neutraliza '
             'tonos azules Lila, neutraliza matices amarillos Naranja, '
             'neutraliza ojeras y manchas oscuras $300 Precio de contado\n'
             'Abonalo en efectivo o con tarjeta de crédito 💳',
  'datetime': '2019-08-25 23:47:00',
  'post_url': 'https://m.facebook.com/story.php?story_fbid=2375171789437267&id=2330857853868661&__tn__=-R',
  'publisher': 'Meraki makeup',
  'searcher_url': 'https://m.facebook.com/Meraki-makeup-2330857853868661'},
 {'content': 'La creatividad es tu mejor habilidad de maquillaje, no tengas '
             'miedo de experimentar 😘\n'
             'Crédito: @rubiitofficial',
  'datetime': '2019-08-25 23:47:00',
  'post_url': 'https://m.facebook.com/story.php?story_fbid=2375171789437267&id=2330857853868661&__tn__=-R',
  'publisher': 'Meraki makeup',
  'searcher_url': 'https://m.facebook.com/Meraki-makeup-2330857853868661'},
 {'content': '🌸Prebase con iluminador VLADA🌸\n'
             '🌸Humecta\n'
             '🌸Ilumina\n'
             '🌸Tonifica $170 c/u Precio de contado\n'
             'Abonalo en efectivo o con tarjeta de crédito 💳',
  'datetime': '2019-08-25 23:47:00',
  'post_url': 'https://m.facebook.com/story.php?story_fbid=2375171789437267&id=2330857853868661&__tn__=-R',
  'publisher': 'Meraki makeup',
  'searcher_url': 'https://m.facebook.com/Meraki-makeup-2330857853868661'},
 {'content': '🤩Paleta Kylie imantada 28 tonos 🤩\n'
             'Hermosa paleta con sombras individuales imantadas. Podes '
             'cambiarlas a tu gusto hasta lograr tu paleta ideal.\n'
             'Tonos matte y satinado.\n'
             'Pigmentación intensa y duradera $500 Precio de contado\n'
             'Abonalo en efectivo o con tarjeta de crédito 💳',
  'datetime': '2019-08-25 23:47:00',
  'post_url': 'https://m.facebook.com/story.php?story_fbid=2375171789437267&id=2330857853868661&__tn__=-R',
  'publisher': 'Meraki makeup',
  'searcher_url': 'https://m.facebook.com/Meraki-makeup-2330857853868661'}
]
```
