# Alternating Characters
# https://www.hackerrank.com/challenges/alternating-characters/problem


def funnyString(s):
    rev = s[::-1]
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(rev[i]) - ord(rev[i-1])):
            return "Not Funny"
    return "Funny"


q = int(input().strip())
for _ in range(q):
    s = input().strip()
    print(funnyString(s))
