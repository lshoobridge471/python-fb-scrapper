from configparser import ConfigParser
import json
# Init config parser
config = ConfigParser()
try:
    # Read configuration file
    config.read('selenium.ini')
    # Get the default section
    remote = config['REMOTE']
    # Get the default section
    browser = config['BROWSER']
    # Get the default section
    agents = config['AGENTS']
except:
    remote = {}
    browser = {}
    agents = {}
    pass

# Settings default object
_DEFAULT_BROWSER_SETTINGS = {
    'remote': {
        'enabled': json.loads(remote.get('enabled', 'False').lower()),
        'protocol': remote.get('protocol', 'http'),
        'host': remote.get('host', 'localhost'),
        'port': int(remote.get('port', 4444)),
    },
    'browser': {
        'data_dir': browser.get('data_dir', None),
        'window_size': browser.get('window_size', '360,640'),
        'time_sleep': int(browser.get('time_sleep', 5)),
    },
    'agents': {
        'custom': browser.get('custom', None),
        'limit': int(browser.get('limit', 100)),
        'random': browser.get('random', False),
    },
}