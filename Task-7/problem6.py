# Pangrams
# https://www.hackerrank.com/challenges/pangrams/problem


def pangrams(s):
    s = s.lower()
   
    letters = set([c for c in s if c.isalpha()])
  
    if len(letters) == 26:
        return "pangram"
    else:
        return "not pangram"


sentence = input().strip()
print(pangrams(sentence))
