import requests
import aiofiles
from asyncio import run
from aiohttp import ClientSession,ClientTimeout
from colorama import init,Fore,Style
from sys import stdout,exit
from os import system,name,path,getcwd,startfile
from random import choice,shuffle
from threading import Thread,Lock,active_count
from time import sleep
from hashlib import sha224,sha256,sha384,sha512,md5
from subprocess import check_output
from getpass import getuser
from subprocess import call

def clear():
    if name == 'posix':
        system('clear')
    elif name in ('ce', 'nt', 'dos'):
        system('cls')
    else:
        print("\n") * 120

def SetTitle(title_name:str):
    system("title {0}".format(title_name))

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

class Authentication:
    def __init__(self):
        clear()
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

        self.use_proxy = int(input(Style.BRIGHT+Fore.WHITE+'\t\t\t ['+Fore.GREEN+'>'+Fore.WHITE+'] ['+Fore.GREEN+'1'+Fore.WHITE+']Proxy ['+Fore.GREEN+'0'+Fore.WHITE+']Proxyless: '))
        
        if self.use_proxy == 1:
            self.proxy_type = int(input(Style.BRIGHT+Fore.WHITE+'\t\t\t ['+Fore.GREEN+'>'+Fore.WHITE+'] ['+Fore.GREEN+'1'+Fore.WHITE+']Https ['+Fore.GREEN+'2'+Fore.WHITE+']Socks4 ['+Fore.GREEN+'3'+Fore.WHITE+']Socks5: '))
        
        print('')
        self.username = str(input(Style.BRIGHT+Fore.WHITE+'\t\t\t ['+Fore.GREEN+'>'+Fore.WHITE+'] USERNAME: '))
        self.password = str(input(Style.BRIGHT+Fore.WHITE+'\t\t\t ['+Fore.GREEN+'>'+Fore.WHITE+'] PASSWORD: '))
        print('')

    def GetCPUName(self):
        try:
            cpuname = check_output(["wmic","cpu","get", "name"]).decode().split('\n')[1].strip()
            return cpuname
        except:
            pass
        
    def GetMOBOName(self):
        try:
            moboname = check_output(['wmic','baseboard','get','Product']).decode().split('\n')[1].strip()
            return moboname
        except:
            pass

    def GetMOBOSerial(self):
        try:
            serial = check_output(['wmic','baseboard','get','serialnumber']).decode().split('\n')[1].strip()
            return serial
        except:
            pass

    def GetGPUName(self):
        try:
            gpuname = check_output(['wmic','PATH','Win32_VideoController','GET','Name']).decode().split('\n')[1].strip()
            return gpuname
        except:
            pass

    def GetUUID(self):
        try:
            uuid = check_output(['wmic','csproduct','get','uuid']).decode().split('\n')[1].strip()
            return uuid
        except:
            pass

    def GetOSUsername(self):
        try:
            os_username = getuser()
            return os_username
        except:
            pass

    def GenHWID(self):
        try:
            cpu_name = 'ő'+self.GetCPUName()+'kalács'
            mobo_name = 'ők'+self.GetMOBOName()+'sütemény'
            mobo_serial = 'őz'+self.GetMOBOSerial()+'őz'
            gpu_name = 'gőz'+self.GetGPUName()+'ékezet'
            uuid = 'mák'+self.GetUUID()+'makóitiesztó'
            os_username = 'dióbélbácsivagyokszia'+self.GetOSUsername()+'őűáéí@{$ß°'

            hashed_cpu_name = md5(cpu_name.encode('utf-8')).hexdigest()
            hashed_mobo_name = sha224(mobo_name.encode('utf-8')).hexdigest()
            hashed_mobo_serial = sha256(mobo_serial.encode('utf-8')).hexdigest()
            hashed_gpu_name = sha384(gpu_name.encode('utf-8')).hexdigest()
            hashed_uuid = sha512(uuid.encode('utf-8')).hexdigest()
            hashed_os_username = sha384(os_username.encode('utf-8')).hexdigest()

            hashed_sum = hashed_cpu_name+hashed_gpu_name+hashed_mobo_name+hashed_mobo_serial+hashed_uuid+hashed_os_username
            hashed_data = sha512(hashed_sum.encode('utf-8')).hexdigest()

            return hashed_data
        except:
            pass
        
    def AuthCheck(self):
        try:
            success = 0

            link = 'https://pastebin.com/raw/E9tEpjEA'

            headers = {
                'User-Agent':GetRandomUserAgent()
            }

            response = ''

            if self.use_proxy == 1:
                response = requests.get(link,headers=headers,proxies=GetRandomProxy(self.proxy_type))
            else:
                response = requests.get(link,headers=headers)

            new_username = 'apádfia'+self.username+'diló'
            new_password = 'dikmore'+self.password+'zsámóő'

            self.username = sha512(new_username.encode('utf-8')).hexdigest()
            self.password = sha512(new_password.encode('utf-8')).hexdigest()

            for user in response.text.splitlines():
                if user.split(':')[0] == self.username and user.split(':')[1] == self.password and user.split(':')[-1] == '0':
                    if user.split(':')[2] == self.GenHWID():
                        success = 1
                else:
                    success = 0
            return success
        except:
            pass

    def Menu(self):
        if self.AuthCheck() == 1:
            PrintText(Fore.WHITE,Fore.GREEN,'AUTH','GRANTED!')
            sleep(2)
            clear()
            print(self.title)
            SetTitle(f'[One Man Builds AIO Username Checker {version}] ^| AUTHENTICATED')
            functions = ['ProxyChecker (New)','ProxyFilter (New)','ProxyScrape (New)']
            index = 0
            for function in functions:
                index += 1
                PrintText(Fore.WHITE,Fore.GREEN,str(index),function)
            print('')

            self.option = int(input(Style.BRIGHT+Fore.WHITE+'\t\t\t ['+Fore.GREEN+'>'+Fore.WHITE+'] Choose something: '))

            ''
        else:
            PrintText(Fore.WHITE,Fore.RED,'AUTH FAILED',self.GenHWID())
            system('pause > nul')

class UpdaterCheck:
    def __init__(self):
        clear()
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
        self.timeout = ClientTimeout(15_000)
        
    async def DownloadUpdater(self):
        try:
            if path.exists('updater.exe') == False:
                async with ClientSession() as session:
                    async with session.get('https://www.dropbox.com/s/87c0kstmmswk2jb/updater.exe?dl=1',timeout=self.timeout) as response:
                        response_content = await response.read()
                        f = await aiofiles.open('updater.exe',mode='wb')
                        await f.write(response_content)
                        await f.close()
                print(Style.BRIGHT+Fore.WHITE+'\t\t\t ['+Fore.GREEN+'DOWNLOADED'+Fore.WHITE+'] updater.exe')
                system('pause > nul')
            else:
                auth = Authentication()
                auth.Menu()
        except:
            pass
        
class ProxyChecker:
    def __init__(self):
        clear()
        SetTitle('One Man Builds Proxy Checker')

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
        self.site_to_check_on = str(input(Style.BRIGHT+Fore.WHITE+'['+Fore.GREEN+'>'+Fore.WHITE+'] Where Do You Want To Check Proxies (url): '))
        self.threads_num = int(input(Style.BRIGHT+Fore.WHITE+'['+Fore.GREEN+'>'+Fore.WHITE+'] Threads: '))
        print('')

        self.goods = 0
        self.deads = 0
        self.skipped = 0

    def TitleUpdate(self):
        while True:
            SetTitle(f'One Man Builds Proxy Checker ^| GOODS: {self.goods} ^| DEADS: {self.deads} ^| SKIPPED: {self.skipped} ^| THREADS: {active_count()-1}')
            sleep(0.1)

    def CheckProxy(self,proxy):
        try:
            headers = {
                'User-Agent':GetRandomUserAgent()
            }

            response = requests.get(self.site_to_check_on,headers=headers,proxies=FormatProxy(self.proxy_type,proxy))
            PrintText(Fore.WHITE,Fore.GREEN,'PROXY CHECKER',f'PROXY {proxy} {response.elapsed.total_seconds()*1000}ms GOOD')
            with open('[Data]/[ProxyChecker]/[Results]/goods.txt','a',encoding='utf8') as f:
                f.write(proxy+'\n')
            self.goods += 1
        except requests.exceptions.ProxyError as p:
            PrintText(Fore.WHITE,Fore.RED,'PROXY CHECKER',f'PROXY {proxy} DEAD')
            with open('[Data]/[ProxyChecker]/[Results]/deads.txt','a',encoding='utf8') as f:
                f.write(proxy+'\n')
            self.deads += 1
        except requests.exceptions.ConnectionError as c:
            PrintText(Fore.WHITE,Fore.RED,'PROXY CHECKER',f'PROXY {proxy} DEAD')
            with open('[Data]/[ProxyChecker]/[Results]/deads.txt','a',encoding='utf8') as f:
                f.write(proxy+'\n')
            self.deads += 1
        except:
            self.skipped += 1
            pass
        
    def Start(self):
        Thread(target=self.TitleUpdate).start()
        proxies = ReadFile('[Data]/[ProxyChecker]/proxies.txt','r')
        for proxy in proxies:
            Run = True
            while Run:
                if active_count()<=self.threads_num:
                    Thread(target=self.CheckProxy,args=(proxy,)).start()
                    Run = False

class ProxyFilter:
    def __init__(self):
        clear()
        SetTitle('One Man Builds Proxy Filter')

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
        self.site_to_check_on = str(input(Style.BRIGHT+Fore.WHITE+'['+Fore.GREEN+'>'+Fore.WHITE+'] Where Do You Want To Check Proxies (url): '))
        self.max_timeout = float(input(Style.BRIGHT+Fore.WHITE+'['+Fore.GREEN+'>'+Fore.WHITE+'] Max Timeout (ms): '))
        self.threads_num = int(input(Style.BRIGHT+Fore.WHITE+'['+Fore.GREEN+'>'+Fore.WHITE+'] Threads: '))
        print('')

        self.goods = 0
        self.deads = 0
        self.skipped = 0

    def TitleUpdate(self):
        while True:
            SetTitle(f'One Man Builds Proxy Filter ^| GOODS: {self.goods} ^| DEADS: {self.deads} ^| SKIPPED: {self.skipped} ^| THREADS: {active_count()-1}')
            sleep(0.1)

    def FilterProxy(self,proxy):
        try:
            headers = {
                'User-Agent':GetRandomUserAgent()
            }

            response = requests.get(self.site_to_check_on,headers=headers,proxies=FormatProxy(self.proxy_type,proxy))
            response_ms = response.elapsed.total_seconds()*1000
            if response_ms <= self.max_timeout:
                PrintText(Fore.WHITE,Fore.GREEN,'PROXY FILTER',f'PROXY {proxy} {response_ms} GOOD')
                with open(f'[Data]/[ProxyFilter]/[Results]/{self.max_timeout}ms_good_proxies.txt','a',encoding='utf8') as f:
                    f.write(proxy+'\n')
                self.goods += 1
        except requests.exceptions.ProxyError as p:
            PrintText(Fore.WHITE,Fore.RED,'PROXY FILTER',f'PROXY {proxy} DEAD')
            with open(f'[Data]/[ProxyFilter]/[Results]/{self.max_timeout}ms_deads.txt','a',encoding='utf8') as f:
                f.write(proxy+'\n')
            self.deads += 1
        except requests.exceptions.ConnectionError as c:
            PrintText(Fore.WHITE,Fore.RED,'PROXY FILTER',f'PROXY {proxy} DEAD')
            with open(f'[Data]/[ProxyFilter]/[Results]/{self.max_timeout}ms_deads.txt','a',encoding='utf8') as f:
                f.write(proxy+'\n')
            self.deads += 1
        except:
            self.skipped += 1
            pass
        
    def Start(self):
        Thread(target=self.TitleUpdate).start()
        proxies = ReadFile('[Data]/[ProxyFilter]/proxies.txt','r')
        for proxy in proxies:
            Run = True
            while Run:
                if active_count()<=self.threads_num:
                    Thread(target=self.FilterProxy,args=(proxy,)).start()
                    Run = False

class ProxyScrape:
    def __init__(self):
        clear()
        SetTitle('One Man Builds ProxyScrape')
        self.title = Style.BRIGHT+Fore.YELLOW+"""                                        
                    ╔══════════════════════════════════════════════════════════════════════════════╗
                                          ╔═╗╦═╗╔═╗═╗ ╦╦ ╦  ╔═╗╔═╗╦═╗╔═╗╔═╗╔═╗
                                          ╠═╝╠╦╝║ ║╔╩╦╝╚╦╝  ╚═╗║  ╠╦╝╠═╣╠═╝║╣ 
                                          ╩  ╩╚═╚═╝╩ ╚═ ╩   ╚═╝╚═╝╩╚═╩ ╩╩  ╚═╝
                    ╚══════════════════════════════════════════════════════════════════════════════╝

        """
        print(self.title)
        self.proxy_type = int(input(Style.BRIGHT+Fore.WHITE+'\t\t\t ['+Fore.YELLOW+'>'+Fore.WHITE+'] ['+Fore.YELLOW+'1'+Fore.WHITE+']Https ['+Fore.YELLOW+'2'+Fore.WHITE+']Socks4 ['+Fore.YELLOW+'3'+Fore.WHITE+']Socks5: '))
        self.timeout = int(input(Style.BRIGHT+Fore.WHITE+'\t\t\t ['+Fore.YELLOW+'>'+Fore.WHITE+'] Timeout: '))
        print('')

    def Scrape(self):
        try:
            link = ''

            if self.proxy_type == 1:
                link = f'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout={self.timeout}&country=all&ssl=all&anonymity=all'
            elif self.proxy_type == 2:
                link = f'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout={self.timeout}&country=all&ssl=all&anonymity=all'
            elif self.proxy_type == 3:
                link = f'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout={self.timeout}&country=all&ssl=all&anonymity=all'
            else:
                link = f'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout={self.timeout}&country=all&ssl=all&anonymity=all'

            headers = {
                'User-Agent':GetRandomUserAgent()
            }

            response = requests.get(link,headers=headers)
            proxies = response.text
            with open('[Data]/proxies.txt',encoding='utf8',mode='w+') as f:
                f.write(proxies.replace('\n',''))
            PrintText(Fore.WHITE,Fore.YELLOW,'PROXYSCRAPE','DONE!')
            sleep(2)
        except:
            pass

if __name__ == "__main__":
    init(convert=True)
    lock = Lock()
    version = 'v1.0.0'
    SetTitle(f'[One Man Builds Proxy Tool {version}] ^| LOADING...')
    sleep(2)
    proxy = ProxyFilter()
    proxy.Start()