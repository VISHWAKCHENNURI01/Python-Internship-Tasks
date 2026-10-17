# Piling Up!
# https://www.hackerrank.com/challenges/piling-up/problem


def piling_up(cubes):
    left, right = 0, len(cubes) - 1
    top = float('inf')  
    
    while left <= right:
        
        if cubes[left] >= cubes[right]:
            chosen = cubes[left]
            left += 1
        else:
            chosen = cubes[right]
            right -= 1
        
    
        if chosen > top:
            return "No"
        top = chosen
    
    return "Yes"


if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        n = int(input().strip())
        cubes = list(map(int, input().split()))
        print(piling_up(cubes))
