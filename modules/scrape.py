import requests
from modules.helpers import _initTitle,_getRandomUserAgent,_print,_anonimityCheck,_writeProxies,_getCC
from pystyle import Colors
from time import sleep

class Scrape:
    def __init__(self,scrape_config) -> None:
        _initTitle('PT [SCRAPE]')

        self.proxy_type = scrape_config['proxy_type']
        self.country_code = scrape_config['country_code']
        self.anonimity = scrape_config['anonimity']
        self.timeout = scrape_config['timeout']
        self.session = requests.session()
        print('')

    def _scrape(self):
        headers = {
            'User-Agent':_getRandomUserAgent('config/useragents.txt'),
            'Connection':'keep-alive'
        }

        try:
            cc = _getCC(self.country_code)
            url = _anonimityCheck(self.proxy_type,self.anonimity,self.timeout,cc)
            response = self.session.get(url,headers=headers)
            proxies = response.text
            _writeProxies('saved/scraped_proxies.txt',proxies)
            proxies_length = len(proxies.split('\n'))-1
            _print(Colors.cyan,Colors.green,'FINISH',f'TOTAL <{proxies_length}>')
            sleep(2)
        except Exception:
            pass

    def _start(self):
        self._scrape()

        print('')
        _print(Colors.cyan,Colors.yellow,'FINISH','Process done!')
