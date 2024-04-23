from os import name,system,stat
from sys import stdout
from random import choice
from time import sleep
from pystyle import Center,Colors,Colorate,Box
import json

def _clear():
    """Clear the console on every os."""
    if name == 'posix':
        system('clear')
    elif name in ('ce', 'nt', 'dos'):
        system('cls')
    else:
        print("\n") * 120

def _setTitle(title:str):
    """Sets the console title on every os."""
    if name == 'posix':
        stdout.write(f"\x1b]2;{title}\x07")
    elif name in ('ce', 'nt', 'dos'):
        system(f'title {title}')
    else:
        stdout.write(f"\x1b]2;{title}\x07")

def _initTitle(title:str):
    _setTitle(title)
    _clear()
    print(Colorate.Vertical(Colors.cyan_to_blue,Center.XCenter("""
    
   ▄███████▄     ███     
  ███    ███ ▀█████████▄ 
  ███    ███    ▀███▀▀██ 
  ███    ███     ███   ▀ 
▀█████████▀      ███     
  ███            ███     
  ███            ███     
 ▄████▀         ▄████▀   
                         
    """)))
    _printContact()

def _printContact():
    print(Colorate.Vertical(Colors.cyan_to_blue,Center.XCenter(Box.DoubleCube("""discord: #onemanbuilds#2108 - email: onemanbuilds@proton.me - github: onemanbuilds"""))))
    print('')

def _print(bracket_color,text_in_bracket_color,text_in_bracket,text):
    """Prints colored formatted text."""
    stdout.flush()
    text = text.encode('ascii','replace').decode()
    stdout.write(bracket_color+'['+text_in_bracket_color+text_in_bracket+bracket_color+'] '+bracket_color+text+'\n')

def _readFile(filename:str,method,empty_check):
    """Read file with empty and file not found check."""
    try:
        if stat(filename).st_size != 0:
            with open(filename,method,encoding='utf8') as f:
                content = [line.strip('\n') for line in f]
                return content
        else:
            if empty_check == 1:
                _print(Colors.cyan,Colors.red,'ERROR',f'{filename} is empty!')
                sleep(2)
                raise SystemExit
    except FileNotFoundError:
        _print(Colors.cyan,Colors.red,'ERROR','File not found!')

def _readJson(filename:str,method):
    """Read json file with empty and file not found check."""
    try:
        if stat(filename).st_size != 0:
            with open(filename,method,encoding='utf8') as f:
                return json.load(f)
        else:
            _print(Colors.cyan,Colors.red,'ERROR',f'{filename} is empty!')
            sleep(2)
            raise SystemExit
    except FileNotFoundError:
        _print(Colors.cyan,Colors.red,'ERROR','File not found!')

def _writeFile(filename:str,content):
    """Write file to path in new line errors ignored"""
    with open(filename,'a',encoding='utf8',errors='ignore') as f:
        f.write(str(content)+"\n")

def _writeProxies(filename:str,content):
    """Write file to path in new line errors ignored"""
    with open(filename,'w+',encoding='utf8',errors='ignore') as f:
        f.write(str(content).replace('\n',''))

def _getRandomUserAgent(path:str):
    """Returns a random user agent."""
    useragents = _readFile(path,'r',1)
    return choice(useragents)

def _getRandomProxy(use_proxy:int,proxy_type:int,path:str):
    """Returns random proxy dict with proxy type check."""
    proxies = {}
    if use_proxy == 1:
        proxy_file = _readFile(path,'r',1)
        random_proxy = choice(proxy_file)
        if proxy_type == 1:
            proxies = {
                "http": "http://{0}".format(random_proxy),
                "https": "https://{0}".format(random_proxy)
            }
        elif proxy_type == 2:
            proxies = {
                "http": "socks4://{0}".format(random_proxy),
                'https': "socks4://{0}".format(random_proxy)
            }
        else:
            proxies = {
                "http": "socks5://{0}".format(random_proxy),
                "https": "socks5://{0}".format(random_proxy)
            }
    else:
        proxies = {
            "http": None,
            "https": None
        }
    return proxies

def _formatProxy(proxy,proxy_type:int):
    """Returns random proxy dict with proxy type check."""
    proxies = {}
    if proxy_type == 1:
        proxies = {
            "http": "http://{0}".format(proxy),
            "https": "https://{0}".format(proxy)
        }
    elif proxy_type == 2:
        proxies = {
            "http": "socks4://{0}".format(proxy),
            'https': "socks4://{0}".format(proxy)
        }
    else:
        proxies = {
            "http": "socks5://{0}".format(proxy),
            "https": "socks5://{0}".format(proxy)
        }
    return proxies
    
def _getCC(country_code_option):
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

def _anonimityCheck(proxy_type,anonimity_option,timeout,cc):
    link = ''
    if proxy_type == 1:
        if anonimity_option == 1:
            link = f'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout={timeout}&country={cc}&ssl=all&anonymity=all'
        elif anonimity_option == 2:
            link = f'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout={timeout}&country={cc}&ssl=all&anonymity=elite'
        elif anonimity_option == 3:
            link = f'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout={timeout}&country={cc}&ssl=all&anonymity=anonymous'
        elif anonimity_option == 4:
            link = f'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout={timeout}&country={cc}&ssl=all&anonymity=transparent'
        else:
            link = f'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout={timeout}&country={cc}&ssl=all&anonymity=all'
    elif proxy_type == 2:
        link = f'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout={timeout}&country={cc}&ssl=all&anonymity=all'
    elif proxy_type == 3:
        link = f'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout={timeout}&country={cc}&ssl=all&anonymity=all'
    else:
        link = f'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout={timeout}&country={cc}&ssl=all&anonymity=all'

    return link