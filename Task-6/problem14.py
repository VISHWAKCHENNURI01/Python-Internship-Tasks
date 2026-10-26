# Set .intersection() Operation
# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem


if __name__ == '__main__':
    n_eng = int(input().strip())
    eng = set(map(int, input().split()))
    n_french = int(input().strip())
    french = set(map(int, input().split()))

    both = eng.intersection(french)

    print(len(both))
