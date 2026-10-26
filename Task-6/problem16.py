# Check Subset
# https://www.hackerrank.com/challenges/py-check-subset/problem


if __name__ == '__main__':
    t = int(input().strip())  

    for _ in range(t):
        n_a = int(input().strip())
        a = set(map(int, input().split()))
        n_b = int(input().strip())
        b = set(map(int, input().split()))

        print(a.issubset(b))
