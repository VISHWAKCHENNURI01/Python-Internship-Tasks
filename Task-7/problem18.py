# String Construction
# https://www.hackerrank.com/challenges/string-construction/problem


def stringConstruction(s):
    # Cost is the number of distinct characters
    return len(set(s))

if __name__ == "__main__":
    q = int(input().strip())
    for _ in range(q):
        s = input().strip()
        print(stringConstruction(s))



