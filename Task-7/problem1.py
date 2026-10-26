# Set .symmetric_difference() Operation
# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem


n_eng = int(input())
eng = set(map(int, input().split()))

n_fre = int(input())
fre = set(map(int, input().split()))


result = eng.symmetric_difference(fre)

print(len(result))
