# Making Anagrams
# https://www.hackerrank.com/challenges/making-anagrams/problem


from collections import Counter

def makingAnagrams(s1, s2):
    
    c1 = Counter(s1)
    c2 = Counter(s2)
    
    deletions = 0

    for ch in set(c1.keys()) | set(c2.keys()):
        deletions += abs(c1.get(ch, 0) - c2.get(ch, 0))
    
    return deletions

if __name__ == "__main__":
    s1 = input().strip()
    s2 = input().strip()
    print(makingAnagrams(s1, s2))
