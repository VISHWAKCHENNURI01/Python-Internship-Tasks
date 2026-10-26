# Check Strict Superset
# https://www.hackerrank.com/challenges/py-check-strict-superset/problem


if __name__ == '__main__':
    A = set(map(int, input().split()))
    n = int(input().strip())

    result = True
    for _ in range(n):
        other = set(map(int, input().split()))
        # strict superset means: A.issuperset(other) and A != other
        if not (A.issuperset(other) and A != other):
            result = False
            break

    print(result)
