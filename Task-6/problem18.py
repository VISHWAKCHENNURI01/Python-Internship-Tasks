# Set Mutations
# https://www.hackerrank.com/challenges/py-set-mutations/problem


if __name__ == '__main__':
    n = int(input().strip())
    A = set(map(int, input().split()))
    N = int(input().strip())

    for _ in range(N):
        op, _ = input().split()   
        other = set(map(int, input().split()))
        
        # perform the mutation
        if op == "update":
            A.update(other)
        elif op == "intersection_update":
            A.intersection_update(other)
        elif op == "difference_update":
            A.difference_update(other)
        elif op == "symmetric_difference_update":
            A.symmetric_difference_update(other)

    print(sum(A))
