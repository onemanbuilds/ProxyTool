import requests
from colorama import init,Fore,Style
from sys import stdout
from os import system,name
from random import choice
from threading import Thread,Lock,active_count
from time import sleep
from itertools import chain

def clear():
    if name == 'posix':
        system('clear')
    elif name in ('ce', 'nt', 'dos'):
        system('cls')
    else:
        print("\n") * 120

def SetTitle(title:str):
    if name == 'posix':
        stdout.write(f"\x1b]2;{title}\x07")
    elif name in ('ce', 'nt', 'dos'):
        system(f'title {title}')
    else:
        stdout.write(f"\x1b]2;{title}\x07")

def GetRandomUserAgent():
    useragents = ReadFile('[Data]/useragents.txt','r')
    return choice(useragents)

def PrintText(bracket_color:Fore,text_in_bracket_color:Fore,text_in_bracket,text):
    lock.acquire()
    stdout.flush()
    text = text.encode('ascii','replace').decode()
    stdout.write(Style.BRIGHT+bracket_color+'['+text_in_bracket_color+text_in_bracket+bracket_color+'] '+bracket_color+text+'\n')
    lock.release()

def ReadFile(filename,method):
    with open(filename,method,encoding='utf8') as f:
        content = [line.strip('\n') for line in f]
        return content

def FormatProxy(proxy_type,proxy):
    proxies = {}
    if proxy_type == 1:
        proxies = {
            "http":"http://{0}".format(proxy),
            "https":"https://{0}".format(proxy)
        }
    elif proxy_type == 2:
        proxies = {
            "http":"socks4://{0}".format(proxy),
            "https":"socks4://{0}".format(proxy)
        }
    else:
        proxies = {
            "http":"socks5://{0}".format(proxy),
            "https":"socks5://{0}".format(proxy)
        }
    return proxies

        
class ProxyChecker:
    def __init__(self):
        clear()
        SetTitle('[One Man Builds Proxy Checker]')

        self.title = Style.BRIGHT+Fore.GREEN+"""
                         ╔════════════════════════════════════════════════════════════════╗
                                         ╔═╗╔╗╔╔═╗╔╦╗╔═╗╔╗╔╔╗ ╦ ╦╦╦  ╔╦╗╔═╗     
                                         ║ ║║║║║╣ ║║║╠═╣║║║╠╩╗║ ║║║   ║║╚═╗     
                                         ╚═╝╝╚╝╚═╝╩ ╩╩ ╩╝╚╝╚═╝╚═╝╩╩═╝═╩╝╚═╝     
                                       ╔═╗╦═╗╔═╗═╗ ╦╦ ╦  ╔═╗╦ ╦╔═╗╔═╗╦╔═╔═╗╦═╗
                                       ╠═╝╠╦╝║ ║╔╩╦╝╚╦╝  ║  ╠═╣║╣ ║  ╠╩╗║╣ ╠╦╝
                                       ╩  ╩╚═╚═╝╩ ╚═ ╩   ╚═╝╩ ╩╚═╝╚═╝╩ ╩╚═╝╩╚═  
                         ╚════════════════════════════════════════════════════════════════╝

        """
        print(self.title)

        self.proxy_type = int(input(Style.BRIGHT+Fore.WHITE+'['+Fore.GREEN+'>'+Fore.WHITE+'] ['+Fore.GREEN+'1'+Fore.WHITE+']Https ['+Fore.GREEN+'2'+Fore.WHITE+']Socks4 ['+Fore.GREEN+'3'+Fore.WHITE+']Socks5: '))
        self.site_to_check_on = str(input(Style.BRIGHT+Fore.WHITE+'['+Fore.GREEN+'>'+Fore.WHITE+'] https://'))
        
        self.site_to_check_on = 'https://'+self.site_to_check_on

        self.threads_num = int(input(Style.BRIGHT+Fore.WHITE+'['+Fore.GREEN+'>'+Fore.WHITE+'] Threads: '))
        print('')

        self.goods = 0
        self.deads = 0
        self.skipped = 0

    def CheckProxy(self,proxy):
        try:
            headers = {
                'User-Agent':GetRandomUserAgent()
            }

            response = requests.get(self.site_to_check_on,headers=headers,timeout=5,proxies=FormatProxy(self.proxy_type,proxy))
            response_ms = response.elapsed.total_seconds()*1000

            PrintText(Fore.WHITE,Fore.GREEN,'GOOD',f'PROXY {proxy} | TIMEOUT: {response_ms}ms | STATUS CODE: <{response.status_code}>')
            with open('[Data]/[ProxyChecker]/[Results]/goods.txt','a',encoding='utf8') as f:
                f.write(proxy+'\n')
            self.goods += 1
        except requests.exceptions.ProxyError as p:
            PrintText(Fore.WHITE,Fore.RED,'DEAD',f'PROXY {proxy}')
            with open('[Data]/[ProxyChecker]/[Results]/deads.txt','a',encoding='utf8') as f:
                f.write(proxy+'\n')
            self.deads += 1
        except requests.exceptions.ConnectionError as c:
            PrintText(Fore.WHITE,Fore.RED,'DEAD',f'PROXY {proxy}')
            with open('[Data]/[ProxyChecker]/[Results]/deads.txt','a',encoding='utf8') as f:
                f.write(proxy+'\n')
            self.deads += 1
        except:
            self.skipped += 1
            pass
        
    def Start(self):
        threads = []

        proxies = ReadFile('[Data]/[ProxyChecker]/proxies.txt','r')
        for proxy in proxies:
            Run = True
            while Run:
                if active_count()<=self.threads_num:
                    thread = Thread(target=self.CheckProxy,args=(proxy,))
                    threads.append(thread)
                    thread.start()
                    Run = False

        for x in threads:
            x.join()

        print('')
        PrintText(Fore.WHITE,Fore.GREEN,'PROXYCHECKER',f'TOTAL: {len(proxies)} GOOD: {self.goods} DEAD: {self.deads}')
        print('')
        PrintText(Fore.WHITE,Fore.GREEN,'#','RETURNING TO THE MENU')
        sleep(2)

class ProxyFilter:
    def __init__(self):
        clear()
        SetTitle('[One Man Builds Proxy Filter]')

        self.title = Style.BRIGHT+Fore.GREEN+"""
                         ╔════════════════════════════════════════════════════════════════╗
                                         ╔═╗╔╗╔╔═╗╔╦╗╔═╗╔╗╔╔╗ ╦ ╦╦╦  ╔╦╗╔═╗
                                         ║ ║║║║║╣ ║║║╠═╣║║║╠╩╗║ ║║║   ║║╚═╗
                                         ╚═╝╝╚╝╚═╝╩ ╩╩ ╩╝╚╝╚═╝╚═╝╩╩═╝═╩╝╚═╝
                                          ╔═╗╦═╗╔═╗═╗ ╦╦ ╦  ╔═╗╦╦ ╔╦╗╔═╗╦═╗ 
                                          ╠═╝╠╦╝║ ║╔╩╦╝╚╦╝  ╠╣ ║║  ║ ║╣ ╠╦╝ 
                                          ╩  ╩╚═╚═╝╩ ╚═ ╩   ╚  ╩╩═╝╩ ╚═╝╩╚═ 
                         ╚════════════════════════════════════════════════════════════════╝

        """
        print(self.title)

        self.proxy_type = int(input(Style.BRIGHT+Fore.WHITE+'['+Fore.GREEN+'>'+Fore.WHITE+'] ['+Fore.GREEN+'1'+Fore.WHITE+']Https ['+Fore.GREEN+'2'+Fore.WHITE+']Socks4 ['+Fore.GREEN+'3'+Fore.WHITE+']Socks5: '))
        self.site_to_check_on = str(input(Style.BRIGHT+Fore.WHITE+'['+Fore.GREEN+'>'+Fore.WHITE+'] https://'))
        self.site_to_check_on = 'https://'+self.site_to_check_on
        self.max_timeout = float(input(Style.BRIGHT+Fore.WHITE+'['+Fore.GREEN+'>'+Fore.WHITE+'] Max Timeout (ms): '))
        self.threads_num = int(input(Style.BRIGHT+Fore.WHITE+'['+Fore.GREEN+'>'+Fore.WHITE+'] Threads: '))
        print('')

        self.goods = 0
        self.deads = 0
        self.skipped = 0

    def FilterProxy(self,proxy):
        try:
            headers = {
                'User-Agent':GetRandomUserAgent()
            }

            response = requests.get(self.site_to_check_on,headers=headers,timeout=5,proxies=FormatProxy(self.proxy_type,proxy))
            response_ms = response.elapsed.total_seconds()*1000
            if response_ms <= self.max_timeout:
                PrintText(Fore.WHITE,Fore.GREEN,'GOOD',f'PROXY {proxy} | TIMEOUT: {response_ms} | STATUS CODE: <{response.status_code}>')
                with open(f'[Data]/[ProxyFilter]/[Results]/{self.max_timeout}ms_good_proxies.txt','a',encoding='utf8') as f:
                    f.write(proxy+'\n')
                self.goods += 1
        except requests.exceptions.ProxyError as p:
            PrintText(Fore.WHITE,Fore.RED,'DEAD',f'PROXY {proxy}')
            with open(f'[Data]/[ProxyFilter]/[Results]/{self.max_timeout}ms_deads.txt','a',encoding='utf8') as f:
                f.write(proxy+'\n')
            self.deads += 1
        except requests.exceptions.ConnectionError as c:
            PrintText(Fore.WHITE,Fore.RED,'DEAD',f'PROXY {proxy}')
            with open(f'[Data]/[ProxyFilter]/[Results]/{self.max_timeout}ms_deads.txt','a',encoding='utf8') as f:
                f.write(proxy+'\n')
            self.deads += 1
        except:
            self.skipped += 1
            pass
        
    def Start(self):
        threads = []

        proxies = ReadFile('[Data]/[ProxyFilter]/proxies.txt','r')
        for proxy in proxies:
            Run = True
            while Run:
                if active_count()<=self.threads_num:
                    thread = Thread(target=self.FilterProxy,args=(proxy,))
                    threads.append(thread)
                    thread.start()
                    Run = False

        for x in threads:
            x.join()

        print('')
        PrintText(Fore.WHITE,Fore.GREEN,'PROXYFILTER',f'TOTAL: {len(proxies)} GOOD: {self.goods} DEAD: {self.deads}')
        print('')
        PrintText(Fore.WHITE,Fore.GREEN,'#','RETURNING TO THE MENU')
        sleep(2)
        
class ProxyScrapeAPI:
    def GetCountry(self,country_code_option):
        country = ''
        if country_code_option == 1:
            country = 'all'
        elif country_code_option == 2:
            country = 'UA'
        elif country_code_option == 3:
            country = 'IR'
        elif country_code_option == 4:
            country = 'PK'
        elif country_code_option == 5:
            country = 'BW'
        elif country_code_option == 6:
            country = 'CO'
        elif country_code_option == 7:
            country = 'RU'
        elif country_code_option == 8:
            country = 'BR'
        elif country_code_option == 9:
            country = 'CN'
        elif country_code_option == 10:
            country = 'SK'
        elif country_code_option == 11:
            country = 'CL'
        elif country_code_option == 12:
            country = 'TH'
        elif country_code_option == 13:
            country = 'VN'
        elif country_code_option == 14:
            country = 'US'
        elif country_code_option == 15:
            country = 'BD'
        elif country_code_option == 16:
            country = 'DE'
        elif country_code_option == 17:
            country = 'PL'
        elif country_code_option == 18:
            country = 'PH'
        elif country_code_option == 19:
            country = 'IN'
        elif country_code_option == 20:
            country = 'RS'
        elif country_code_option == 21:
            country = 'LB'
        elif country_code_option == 22:
            country = 'KE'
        elif country_code_option == 23:
            country = 'IT'
        elif country_code_option == 24:
            country = 'GE'
        elif country_code_option == 25:
            country = 'UG'
        elif country_code_option == 26:
            country = 'ID'
        elif country_code_option == 27:
            country = 'KH'
        elif country_code_option == 28:
            country = 'TR'
        elif country_code_option == 29:
            country = 'NG'
        elif country_code_option == 30:
            country = 'AR'
        elif country_code_option == 31:
            country = 'FR'
        elif country_code_option == 32:
            country = 'PY'
        elif country_code_option == 33:
            country = 'MX'
        elif country_code_option == 34:
            country = 'SG'
        elif country_code_option == 35:
            country = 'MY'
        elif country_code_option == 36:
            country = 'NP'
        elif country_code_option == 37:
            country = 'CZ'
        elif country_code_option == 38:
            country = 'ES'
        elif country_code_option == 39:
            country = 'KR'
        elif country_code_option == 40:
            country = 'BG'
        elif country_code_option == 41:
            country = 'HU'
        elif country_code_option == 42:
            country = 'AL'
        elif country_code_option == 43:
            country = 'EC'
        elif country_code_option == 44:
            country = 'RO'
        elif country_code_option == 45:
            country = 'LV'
        elif country_code_option == 46:
            country = 'IQ'
        elif country_code_option == 47:
            country = 'HN'
        elif country_code_option == 48:
            country = 'SC'
        elif country_code_option == 49:
            country = 'AM'
        elif country_code_option == 50:
            country = 'MD'
        elif country_code_option == 51:
            country = 'BO'
        elif country_code_option == 52:
            country = 'KZ'
        elif country_code_option == 53:
            country = 'VE'
        elif country_code_option == 54:
            country = 'CY'
        elif country_code_option == 55:
            country = 'PE'
        elif country_code_option == 56:
            country = 'MN'
        elif country_code_option == 57:
            country = 'TW'
        elif country_code_option == 58:
            country = 'PR'
        elif country_code_option == 59:
            country = 'GB'
        elif country_code_option == 60:
            country = 'CA'
        elif country_code_option == 61:
            country = 'HR'
        elif country_code_option == 62:
            country = 'PS'
        elif country_code_option == 63:
            country = 'CR'
        elif country_code_option == 64:
            country = 'MW'
        elif country_code_option == 65:
            country = 'IE'
        elif country_code_option == 66:
            country = 'GR'
        elif country_code_option == 67:
            country = 'KG'
        elif country_code_option == 68:
            country = 'GT'
        elif country_code_option == 69:
            country = 'SE'
        elif country_code_option == 70:
            country = 'ZA'
        elif country_code_option == 71:
            country = 'NL'
        else:
            country = 'all'

        return country

    def __init__(self):
        clear()
        SetTitle('[One Man Builds ProxyScrape]')
        self.title = Style.BRIGHT+Fore.GREEN+f"""                                        
                    ╔══════════════════════════════════════════════════════════════════════════════╗
                                          ╔═╗╦═╗╔═╗═╗ ╦╦ ╦  ╔═╗╔═╗╦═╗╔═╗╔═╗╔═╗
                                          ╠═╝╠╦╝║ ║╔╩╦╝╚╦╝  ╚═╗║  ╠╦╝╠═╣╠═╝║╣ 
                                          ╩  ╩╚═╚═╝╩ ╚═ ╩   ╚═╝╚═╝╩╚═╩ ╩╩  ╚═╝
                    ╚══════════════════════════════════════════════════════════════════════════════╝
        """
        print(self.title)
        print('\t\t    ════════════════════════════════════════════════════════════════════════════════')
        print(Fore.WHITE+'\t\t\t\t\t\t     COUNTRY CODES')
        print(Fore.GREEN+'\t\t    ════════════════════════════════════════════════════════════════════════════════')
        print(f'\t\t\t {Fore.WHITE}[{Fore.GREEN}1{Fore.WHITE}]ALL {Fore.WHITE}[{Fore.GREEN}2{Fore.WHITE}]UA {Fore.WHITE}[{Fore.GREEN}3{Fore.WHITE}]IR {Fore.WHITE}[{Fore.GREEN}4{Fore.WHITE}]PK {Fore.WHITE}[{Fore.GREEN}5{Fore.WHITE}]BW {Fore.WHITE}[{Fore.GREEN}6{Fore.WHITE}]CO {Fore.WHITE}[{Fore.GREEN}7{Fore.WHITE}]RU {Fore.WHITE}[{Fore.GREEN}8{Fore.WHITE}]BR {Fore.WHITE}[{Fore.GREEN}9{Fore.WHITE}]CN {Fore.WHITE}[{Fore.GREEN}10{Fore.WHITE}]SK {Fore.WHITE}[{Fore.GREEN}11{Fore.WHITE}]CL')
        print(f'\t\t\t {Fore.WHITE}[{Fore.GREEN}12{Fore.WHITE}]TH {Fore.WHITE}[{Fore.GREEN}13{Fore.WHITE}]VN {Fore.WHITE}[{Fore.GREEN}14{Fore.WHITE}]US {Fore.WHITE}[{Fore.GREEN}15{Fore.WHITE}]BD {Fore.WHITE}[{Fore.GREEN}16{Fore.WHITE}]DE {Fore.WHITE}[{Fore.GREEN}17{Fore.WHITE}]PL {Fore.WHITE}[{Fore.GREEN}18{Fore.WHITE}]PH {Fore.WHITE}[{Fore.GREEN}19{Fore.WHITE}]IN {Fore.WHITE}[{Fore.GREEN}20{Fore.WHITE}]RS {Fore.WHITE}[{Fore.GREEN}21{Fore.WHITE}]LB')
        print(f'\t\t\t {Fore.WHITE}[{Fore.GREEN}22{Fore.WHITE}]KE {Fore.WHITE}[{Fore.GREEN}23{Fore.WHITE}]IT {Fore.WHITE}[{Fore.GREEN}24{Fore.WHITE}]GE {Fore.WHITE}[{Fore.GREEN}25{Fore.WHITE}]UG {Fore.WHITE}[{Fore.GREEN}26{Fore.WHITE}]ID {Fore.WHITE}[{Fore.GREEN}27{Fore.WHITE}]KH {Fore.WHITE}[{Fore.GREEN}28{Fore.WHITE}]TR {Fore.WHITE}[{Fore.GREEN}29{Fore.WHITE}]NG {Fore.WHITE}[{Fore.GREEN}30{Fore.WHITE}]AR {Fore.WHITE}[{Fore.GREEN}31{Fore.WHITE}]FR')
        print(f'\t\t\t {Fore.WHITE}[{Fore.GREEN}32{Fore.WHITE}]PY {Fore.WHITE}[{Fore.GREEN}33{Fore.WHITE}]MX {Fore.WHITE}[{Fore.GREEN}34{Fore.WHITE}]SG {Fore.WHITE}[{Fore.GREEN}35{Fore.WHITE}]MY {Fore.WHITE}[{Fore.GREEN}36{Fore.WHITE}]NP {Fore.WHITE}[{Fore.GREEN}37{Fore.WHITE}]CZ {Fore.WHITE}[{Fore.GREEN}38{Fore.WHITE}]ES {Fore.WHITE}[{Fore.GREEN}39{Fore.WHITE}]KR {Fore.WHITE}[{Fore.GREEN}40{Fore.WHITE}]BG {Fore.WHITE}[{Fore.GREEN}41{Fore.WHITE}]HU')
        print(f'\t\t\t {Fore.WHITE}[{Fore.GREEN}42{Fore.WHITE}]AL {Fore.WHITE}[{Fore.GREEN}43{Fore.WHITE}]EC {Fore.WHITE}[{Fore.GREEN}44{Fore.WHITE}]RO {Fore.WHITE}[{Fore.GREEN}45{Fore.WHITE}]LV {Fore.WHITE}[{Fore.GREEN}46{Fore.WHITE}]IQ {Fore.WHITE}[{Fore.GREEN}47{Fore.WHITE}]HN {Fore.WHITE}[{Fore.GREEN}48{Fore.WHITE}]SC {Fore.WHITE}[{Fore.GREEN}49{Fore.WHITE}]AM {Fore.WHITE}[{Fore.GREEN}50{Fore.WHITE}]MD {Fore.WHITE}[{Fore.GREEN}51{Fore.WHITE}]BO')
        print(f'\t\t\t {Fore.WHITE}[{Fore.GREEN}52{Fore.WHITE}]KZ {Fore.WHITE}[{Fore.GREEN}53{Fore.WHITE}]VE {Fore.WHITE}[{Fore.GREEN}54{Fore.WHITE}]CY {Fore.WHITE}[{Fore.GREEN}55{Fore.WHITE}]PE {Fore.WHITE}[{Fore.GREEN}56{Fore.WHITE}]MN {Fore.WHITE}[{Fore.GREEN}57{Fore.WHITE}]TW {Fore.WHITE}[{Fore.GREEN}58{Fore.WHITE}]PR {Fore.WHITE}[{Fore.GREEN}59{Fore.WHITE}]GB {Fore.WHITE}[{Fore.GREEN}60{Fore.WHITE}]CA {Fore.WHITE}[{Fore.GREEN}61{Fore.WHITE}]HR')
        print(f'\t\t\t {Fore.WHITE}[{Fore.GREEN}62{Fore.WHITE}]PS {Fore.WHITE}[{Fore.GREEN}63{Fore.WHITE}]CR {Fore.WHITE}[{Fore.GREEN}64{Fore.WHITE}]MW {Fore.WHITE}[{Fore.GREEN}65{Fore.WHITE}]IE {Fore.WHITE}[{Fore.GREEN}66{Fore.WHITE}]GR {Fore.WHITE}[{Fore.GREEN}67{Fore.WHITE}]KG {Fore.WHITE}[{Fore.GREEN}68{Fore.WHITE}]GT {Fore.WHITE}[{Fore.GREEN}69{Fore.WHITE}]SE {Fore.WHITE}[{Fore.GREEN}70{Fore.WHITE}]ZA {Fore.WHITE}[{Fore.GREEN}71{Fore.WHITE}]NL')
        print(Fore.GREEN+'\t\t    ════════════════════════════════════════════════════════════════════════════════')
        print('')

        self.country_code_option = int(input(Style.BRIGHT+Fore.WHITE+'['+Fore.GREEN+'>'+Fore.WHITE+'] Choose a country: '))
        self.proxy_type = int(input(Style.BRIGHT+Fore.WHITE+'['+Fore.GREEN+'>'+Fore.WHITE+'] ['+Fore.GREEN+'1'+Fore.WHITE+']Https ['+Fore.GREEN+'2'+Fore.WHITE+']Socks4 ['+Fore.GREEN+'3'+Fore.WHITE+']Socks5: '))
        if self.proxy_type == 1:
            self.anonimity_option = int(input(Style.BRIGHT+Fore.WHITE+'['+Fore.GREEN+'>'+Fore.WHITE+'] ['+Fore.GREEN+'1'+Fore.WHITE+']ALL ['+Fore.GREEN+'2'+Fore.WHITE+']Elite ['+Fore.GREEN+'3'+Fore.WHITE+']Anonymous ['+Fore.GREEN+'4'+Fore.WHITE+']Transparent: '))
        self.timeout = int(input(Style.BRIGHT+Fore.WHITE+'['+Fore.GREEN+'>'+Fore.WHITE+'] Timeout: '))
        print('')

    def Scrape(self):
        try:
            link = ''

            country = self.GetCountry(self.country_code_option)

            if self.proxy_type == 1:
                if self.anonimity_option == 1:
                    link = f'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout={self.timeout}&country={country}&ssl=all&anonymity=all'
                elif self.anonimity_option == 2:
                    link = f'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout={self.timeout}&country={country}&ssl=all&anonymity=elite'
                elif self.anonimity_option == 3:
                    link = f'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout={self.timeout}&country={country}&ssl=all&anonymity=anonymous'
                elif self.anonimity_option == 4:
                    link = f'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout={self.timeout}&country={country}&ssl=all&anonymity=transparent'
                else:
                    link = f'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout={self.timeout}&country={country}&ssl=all&anonymity=all'
            elif self.proxy_type == 2:
                link = f'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout={self.timeout}&country={country}&ssl=all&anonymity=all'
            elif self.proxy_type == 3:
                link = f'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout={self.timeout}&country={country}&ssl=all&anonymity=all'
            else:
                link = f'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout={self.timeout}&country={country}&ssl=all&anonymity=all'

            headers = {
                'User-Agent':GetRandomUserAgent()
            }

            response = requests.get(link,headers=headers)
            proxies = response.text

            with open('[Data]/[ProxyScraper]/[Results]/proxies.txt',encoding='utf8',mode='w+') as f:
                f.write(proxies.replace('\n',''))
            
            proxies_length = len(proxies.split('\n'))-1

            PrintText(Fore.WHITE,Fore.GREEN,'PROXYSCRAPER',f'TOTAL: {proxies_length}')
            print('')
            PrintText(Fore.WHITE,Fore.GREEN,'#','RETURNING TO THE MENU')
            sleep(2)
        except:
            pass

class Main:
    def __init__(self):
        self.title = Style.BRIGHT+Fore.GREEN+"""
                         ╔════════════════════════════════════════════════════════════════╗
                                       ╔═╗╔╗╔╔═╗╔╦╗╔═╗╔╗╔╔╗ ╦ ╦╦╦  ╔╦╗╔═╗
                                       ║ ║║║║║╣ ║║║╠═╣║║║╠╩╗║ ║║║   ║║╚═╗
                                       ╚═╝╝╚╝╚═╝╩ ╩╩ ╩╝╚╝╚═╝╚═╝╩╩═╝═╩╝╚═╝
                                          ╔═╗╦═╗╔═╗═╗ ╦╦ ╦  ╔╦╗╔═╗╔═╗╦      
                                          ╠═╝╠╦╝║ ║╔╩╦╝╚╦╝   ║ ║ ║║ ║║      
                                          ╩  ╩╚═╚═╝╩ ╚═ ╩    ╩ ╚═╝╚═╝╩═╝    
                         ╚════════════════════════════════════════════════════════════════╝

        """
        print(self.title)

    def RemoveDuplicates(self,path):
        try:
            content = ReadFile(path,'r')

            started_length = len(content)

            output_set = set(content)
            
            with open(path,'w+',encoding='utf8') as f:
                f.write('\n'.join(output_set))

            final_length = len(output_set)

            PrintText(Fore.WHITE,Fore.GREEN,'#',f'STARTED: {started_length} / ENDED WITH: {final_length} / REMOVED: {started_length-final_length}')
            print('')
            PrintText(Fore.WHITE,Fore.GREEN,'#','RETURNING TO THE MENU')
            sleep(2)
        except:
            pass

    def Menu(self):
        clear()
        SetTitle('[One Man Builds Proxy Tool]')
        print(self.title)
        functions = ['Proxy Checker','Proxy Filter','Proxy Scrape (Proxyscrape.com API)','Remove Duplicates']
        index = 0
        for function in functions:
            index += 1
            PrintText(Fore.WHITE,Fore.GREEN,str(index),function)

        print('')
        self.option = int(input(Style.BRIGHT+Fore.WHITE+'['+Fore.GREEN+'>'+Fore.WHITE+'] Choose something: '))
        print('')
        
        if self.option == 1:
            proxychecker = ProxyChecker()
            proxychecker.Start()
            SetTitle('[One Man Builds Proxy Tool]')
            self.Menu()
        elif self.option == 2:
            proxyfilter = ProxyFilter()
            proxyfilter.Start()
            SetTitle('[One Man Builds Proxy Tool]')
            self.Menu()
        elif self.option == 3:
            proxyscraper = ProxyScrapeAPI()
            proxyscraper.Scrape()
            SetTitle('[One Man Builds Proxy Tool]')
            self.Menu()
        elif self.option == 4:
            path = str(input(Style.BRIGHT+Fore.WHITE+'['+Fore.GREEN+'>'+Fore.WHITE+'] File Path: '))
            print('')
            self.RemoveDuplicates(path)
            self.Menu()
        else:
            proxyscraper = ProxyScrapeAPI()
            proxyscraper.Scrape()
            SetTitle('[One Man Builds Proxy Tool]')
            self.Menu()


if __name__ == "__main__":
    init(convert=True)
    lock = Lock()
    SetTitle('[One Man Builds Proxy Tool] ^| LOADING...')
    main = Main()
    main.Menu()