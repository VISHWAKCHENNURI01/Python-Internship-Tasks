# Set .union() Operation
# https://www.hackerrank.com/challenges/py-set-union/problem


if __name__ == '__main__':
    n_eng = int(input().strip())
    eng = set(map(int, input().split()))
    n_french = int(input().strip())
    french = set(map(int, input().split()))

  
    total = eng.union(french)

    print(len(total))
