import requests
from modules.helpers import _initTitle,_getRandomUserAgent,_formatProxy,_writeFile,_print
from threading import Thread,active_count
from pystyle import Colors

class Check:
    def __init__(self,checker_config,check_proxies) -> None:
        _initTitle('PT [CHECK]')

        self.proxy_type = checker_config['proxy_type']
        self.threads = checker_config['threads']+20
        self.test_site = checker_config['test_site']
        self.check_proxies = check_proxies
        self.session = requests.session()
        print('')

    def _check(self,proxy):
        headers = {
            'User-Agent':_getRandomUserAgent('config/useragents.txt'),
            'Connection':'keep-alive'
        }

        try:
            response = self.session.get(self.test_site,proxies=_formatProxy(proxy,self.proxy_type),headers=headers)
            response_ms = response.elapsed.total_seconds()*1000
            _print(Colors.cyan,Colors.green,'HIT',f'{proxy} - TIMEOUT <{response_ms}ms> - STATUS <{response.status_code}>')
            _writeFile('saved/checked_hits.txt',proxy)
            response.close()
        except requests.exceptions.ProxyError:
            _print(Colors.cyan,Colors.red,'DEAD',proxy)
            _writeFile('saved/checked_deads.txt',proxy)
        except requests.ConnectionError:
            _print(Colors.cyan,Colors.red,'DEAD',proxy)
            _writeFile('saved/checked_deads.txt',proxy)
        except Exception:
            pass

    def _start(self):
        threads = []

        for proxy in self.check_proxies:
            run = True

            while run:
                if active_count()<=self.threads:
                    thread = Thread(target=self._check,args=(proxy,))
                    threads.append(thread)
                    thread.start()
                    run = False
        for x in threads:
            x.join()

        print('')
        _print(Colors.cyan,Colors.yellow,'FINISH','Process done!')
