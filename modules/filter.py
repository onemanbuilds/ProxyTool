import requests
from modules.helpers import _initTitle,_getRandomUserAgent,_formatProxy,_writeFile,_print
from threading import Thread,active_count
from pystyle import Colors

class Filter:
    def __init__(self,filter_config,filter_proxies) -> None:
        _initTitle('PT [FILTER]')

        self.proxy_type = filter_config['proxy_type']
        self.threads = filter_config['threads']+20
        self.test_site = filter_config['test_site']
        self.max_timeout = filter_config['max_timeout']
        self.filter_proxies = filter_proxies
        self.session = requests.session()
        print('')

    def _filter(self,proxy):
        headers = {
            'User-Agent':_getRandomUserAgent('config/useragents.txt'),
            'Connection':'keep-alive'
        }

        try:
            response = self.session.get(self.test_site,proxies=_formatProxy(proxy,self.proxy_type),headers=headers)
            response_ms = response.elapsed.total_seconds()*1000
            if response_ms <= self.max_timeout:
                _print(Colors.cyan,Colors.green,'HIT',f'{proxy} - TIMEOUT <{response_ms}ms> - STATUS <{response.status_code}>')
                _writeFile('saved/filter_hits.txt',proxy)
            else:
                _print(Colors.cyan,Colors.yellow,'TIMEOUT',f'{proxy} - TIMEOUT <{response_ms}ms> - STATUS <{response.status_code}>')
                _writeFile('saved/filter_timedouts.txt',proxy)
            response.close()
        except requests.exceptions.ProxyError:
            _print(Colors.cyan,Colors.red,'DEAD',proxy)
            _writeFile('saved/filter_deads.txt',proxy)
        except requests.ConnectionError:
            _print(Colors.cyan,Colors.red,'DEAD',proxy)
            _writeFile('saved/filter_deads.txt',proxy)
        except Exception:
            pass

    def _start(self):
        threads = []

        for proxy in self.filter_proxies:
            run = True

            while run:
                if active_count()<=self.threads:
                    thread = Thread(target=self._filter,args=(proxy,))
                    threads.append(thread)
                    thread.start()
                    run = False
        for x in threads:
            x.join()

        print('')
        _print(Colors.cyan,Colors.yellow,'FINISH','Process done!')
