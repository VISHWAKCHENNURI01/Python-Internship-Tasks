# Separate the Numbers
# https://www.hackerrank.com/challenges/separate-the-numbers/problem


def separateNumbers(s):
    n = len(s)
    
    for length in range(1, n // 2 + 1):
        first = int(s[:length])
        seq = str(first)
        next_num = first
        # Build the sequence until it matches or exceeds the input
        while len(seq) < n:
            next_num += 1
            seq += str(next_num)
        if seq == s:
            print("YES", first)
            return
    print("NO")

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        separateNumbers(s)
