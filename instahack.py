import os, re, time, sys, random, instaloader
from rich.console import Console

console = Console()

def banner():
    os.system('clear')
    c1 = '\033[1;31m' # الأحمر
    c2 = '\033[1;37m' # الأبيض
    print(f"{c1}" + "═"*62)
    print(f"{c2}   ___ _  _ ___ _____   _   _  _   _   ___ _  __")
    print(f"{c1}  |_ _| \| / __|_   _| /_\ | || | /_\ / __| |/ /")
    print(f"{c2}   | || .` \__ \ | |  / _ \| __ |/ _ \ (__| ' < ")
    print(f"{c1}  |___|_|\_|___/ |_| /_/ \_\_||_/_/ \_\___|_|\_\\")
    print(f"{c1}" + "═"*62)
    # التعديل المطلوب: ABOOD_FAYOMI
    print(f"{c2}  [ OWNER: {c1}ABOOD_FAYOMI {c2}] | [ STATUS: {c1}SYSTEM_READY {c2}]")
    print(f"{c1}  [!] ATTACK VECTOR MENU:")
    print(f"{c1}" + "═"*62 + "\033[0m")

def matrix_scan(text):
    for char in text:
        sys.stdout.write(f"\033[1;32m{char}")
        sys.stdout.flush()
        time.sleep(0.01)
    print()

def get_ultra_data():
    banner()
    user = input("\n\033[1;37m[?] Enter Target Username: ").strip()
    try:
        L = instaloader.Instaloader()
        matrix_scan(f"[*] Extracting Intelligence Data... @{user}")
        profile = instaloader.Profile.from_username(L.context, user)
        
        print(f"\n\033[1;31m[ ACCESS GRANTED - DATA UNLOCKED ]")
        print(f"\033[1;37m- System ID  : \033[1;32m{profile.userid}")
        print(f"\033[1;37m- Full Identity: \033[1;32m{profile.full_name}")
        print(f"\033[1;37m- Followers  : \033[1;32m{profile.followers:,}")
        print(f"\033[1;37m- Avatar URL : \033[1;34m{profile.profile_pic_url}")
    except:
        print("\033[1;31m[!] Error: Instagram security blocked the connection.")
    input("\n[Press Enter to Return]")

def brute_force_real():
    banner()
    target = input("\n\033[1;37m[?] Target Username: ")
    wordlist = input("[?] Drag & Drop Wordlist (.txt): ").strip()
    
    if not os.path.exists(wordlist):
        print("\033[1;31m[!] Error: Wordlist file not found.")
        return

    with open(wordlist, 'r') as f:
        passwords = f.read().splitlines()

    matrix_scan(f"[*] Starting Brute-Force Payload on @{target}...")
    for pwd in passwords:
        sys.stdout.write(f"\r\033[1;37m[ATTEMPT] \033[1;31m@{target} \033[1;37m| Key: \033[1;33m{pwd.ljust(12)} \033[1;37m| Status: \033[1;31mDENIED")
        sys.stdout.flush()
        time.sleep(0.04)
        if pwd == "abood123":
            print(f"\n\n\033[1;42m\033[1;37m [MATCH FOUND] PASSWORD IDENTIFIED: {pwd} \033[0m")
            return
    print("\n\n\033[1;31m[!] Finished: No valid key found in wordlist.")
    input("\n[Press Enter]")

def mass_report_proxy():
    banner()
    target = input("\n\033[1;37m[?] Target Username: ")
    num = int(input("[?] Number of Reports: "))
    
    matrix_scan(f"[*] Launching {num} proxy-based reports at @{target}...")
    for i in range(1, num + 1):
        ip = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
        sys.stdout.write(f"\r\033[1;31m[REPORT] \033[1;37mPacket: {i}/{num} | \033[1;35mSource: {ip} \033[1;32m[SENT]")
        sys.stdout.flush()
        time.sleep(0.01)
    print(f"\n\n\033[1;32m[✔] Attack sequence complete. Target system flagged.")
    input("\n[Press Enter]")

def main():
    while True:
        banner()
        print("\033[1;31m [01] \033[1;37mGather Information (OSINT)")
        print("\033[1;31m [02] \033[1;37mMass Reporting (Simulation)")
        print("\033[1;31m [03] \033[1;37mBrute-Force Attack (Wordlist)")
        print("\033[1;31m [00] \033[1;37mExit Program")
        
        # سطر الإدخال التوجيهي
        choice = input("\n\033[1;32mSelect the operation number to start > \033[1;37m")
        
        if choice in ['1', '01']: get_ultra_data()
        elif choice in ['2', '02']: mass_report_proxy()
        elif choice in ['3', '03']: brute_force_real()
        elif choice in ['0', '00']:
            print("\033[1;31mShutting down system... Goodbye.")
            sys.exit()

if __name__ == "__main__":
    main()
