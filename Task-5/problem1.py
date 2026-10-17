# Find the Runner-Up Score!
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    max_score = max(arr)
    
    while max_score in arr:
        arr.remove(max_score)
        
    runner_up = max(arr)
    print(runner_up)
