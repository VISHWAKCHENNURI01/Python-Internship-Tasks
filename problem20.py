# No Idea!
# https://www.hackerrank.com/challenges/no-idea/problem


if __name__ == '__main__':
    # Read n (array size) and m (set sizes)
    n, m = map(int, input().split())
    
    # Read the array
    arr = list(map(int, input().split()))
    
    # Read sets A and B
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    
    # Calculate happiness
    happiness = 0
    for x in arr:
        if x in A:
            happiness += 1
        elif x in B:
            happiness -= 1
    
    print(happiness)
