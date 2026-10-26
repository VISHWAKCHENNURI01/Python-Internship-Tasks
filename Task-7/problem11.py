# Two Strings
# https://www.hackerrank.com/challenges/two-strings/problem


def twoStrings(s1, s2):
    
    set1 = set(s1)
    set2 = set(s2)
    

    if set1 & set2:
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        s1 = input().strip()
        s2 = input().strip()
        print(twoStrings(s1, s2))
