# Anagram
# https://www.hackerrank.com/challenges/anagram/problem


from collections import Counter

def anagram(s):
    # If length is odd, cannot split evenly
    if len(s) % 2 != 0:
        return -1
    
    mid = len(s) // 2
    s1, s2 = s[:mid], s[mid:]
    
    # Count characters in both halves
    c1 = Counter(s1)
    c2 = Counter(s2)
    
    # Find how many characters in s1 are "extra"
    changes = 0
    for ch in c1:
        if c1[ch] > c2.get(ch, 0):
            changes += c1[ch] - c2.get(ch, 0)
    
    return changes

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        print(anagram(s))
