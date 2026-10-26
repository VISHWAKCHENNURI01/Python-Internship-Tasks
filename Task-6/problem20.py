# Validating the Phone Number
# https://www.hackerrank.com/challenges/validating-the-phone-number/problem?utm_source=chatgpt.com


import re

if __name__ == '__main__':
    n = int(input().strip())
    pattern = re.compile(r'^[789]\d{9}$')  

    for _ in range(n):
        s = input().strip()
        if pattern.match(s):
            print("YES")
        else:
            print("NO")
