# Sherlock and the Valid String
# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem


from collections import Counter

def isValid(s):
    freq = Counter(s)
    values = list(freq.values())
    freq_count = Counter(values)

    # Case 1: all frequencies equal
    if len(freq_count) == 1:
        return "YES"

    # Case 2: exactly two different frequencies
    if len(freq_count) == 2:
        (f1, c1), (f2, c2) = freq_count.items()

        # One frequency occurs once and is either 1
        # or differs by exactly 1 from the other frequency
        if (c1 == 1 and (f1 == 1 or f1 - 1 == f2)) or \
           (c2 == 1 and (f2 == 1 or f2 - 1 == f1)):
            return "YES"

    return "NO"

if __name__ == "__main__":
    s = input().strip()
    print(isValid(s))
