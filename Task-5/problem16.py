# Collections.Counter()
# https://www.hackerrank.com/challenges/collections-counter/problem


# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

if __name__ == '__main__':
    # Number of shoes
    n = int(input().strip())
    
    # Shoe sizes in the shop
    sizes = list(map(int, input().split()))
    inventory = Counter(sizes)   # count of each shoe size
    
    # Number of customers
    customers = int(input().strip())
    
    earnings = 0
    for _ in range(customers):
        size, price = map(int, input().split())
        if inventory[size] > 0:  
            earnings += price
            inventory[size] -= 1 
    
    print(earnings)
