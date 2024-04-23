from modules.helpers import _initTitle,_readJson,_readFile,_print
from modules.scrape import Scrape
from modules.check import Check
from modules.filter import Filter
from modules.duplicateRemove import DuplicateRemove
from time import sleep
from pystyle import Colors

class Menu:
    def __init__(self) -> None:
        _initTitle('PT [MENU]')

    def _menu(self):        
        _initTitle('PT [MENU]')

        self.scrape_config = _readJson('config/scrape_config.json','r')

        self.checker_config = _readJson('config/checker_config.json','r')
        self.checker_proxies_path = self.checker_config['checker_proxies_path']
        self.checker_proxies = _readFile(self.checker_proxies_path,'r',0)

        self.filter_config = _readJson('config/filter_config.json','r')
        self.filter_proxies_path = self.filter_config['filter_proxies_path']
        self.filter_proxies = _readFile(self.filter_proxies_path,'r',0)

        self.duplicate_rem_config = _readJson('config/duplicate_rem_config.json','r')

        options = ['Scrape Proxies','Check Proxies','Filter Proxies','Remove Duplicates']
        counter = 0
        for option in options:
            counter+=1
            _print(Colors.cyan,Colors.yellow,str(counter),option)
        print('')

        selected = int(input(f'{Colors.cyan}[{Colors.yellow}>{Colors.cyan}] {Colors.cyan}Select something:{Colors.yellow} '))

        if selected == 1:
            Scrape(self.scrape_config)._start()
            sleep(2)
            self._menu()
        elif selected == 2:
            Check(self.checker_config,self.checker_proxies)._start()
            sleep(2)
            self._menu()
        elif selected == 3:
            Filter(self.filter_config,self.filter_proxies)._start()
            sleep(2)
            self._menu()
        elif selected == 4:
            DuplicateRemove(self.duplicate_rem_config)._start()
            sleep(2)
            self._menu()
        else:
            self._menu()