# Set .add()
# https://www.hackerrank.com/challenges/py-set-add/problem


if __name__ == '__main__':
    n = int(input().strip())   
    stamps = set()             
    
    for _ in range(n):
        country = input().strip()
        stamps.add(country)    
    
    print(len(stamps))         
