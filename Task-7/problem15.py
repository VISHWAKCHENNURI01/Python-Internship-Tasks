# Game of Thrones - I
# https://www.hackerrank.com/challenges/game-of-thrones/problem


from collections import Counter

def gameOfThrones(s):
    freq = Counter(s)
    odd_counts = sum(1 for count in freq.values() if count % 2 != 0)
    
    # Valid if at most one odd frequency
    return "YES" if odd_counts <= 1 else "NO"

if __name__ == "__main__":
    s = input().strip()
    print(gameOfThrones(s))
