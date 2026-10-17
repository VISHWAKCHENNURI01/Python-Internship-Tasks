# Symmetric Difference
# https://www.hackerrank.com/challenges/symmetric-difference/problem


# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    m = int(input().strip())
    a = set(map(int, input().split()))

    n = int(input().strip())
    b = set(map(int, input().split()))

    # Symmetric difference
    result = a.symmetric_difference(b)

    # Print in ascending order
    for val in sorted(result):
        print(val)

