# Alphabet Rangoli
# https://www.hackerrank.com/challenges/alphabet-rangoli/problem


import string

def rangoli(size):
    alphabet = string.ascii_lowercase
    lines = []
    for i in range(size):
        left = alphabet[size-1:size-i-1:-1]
        right = alphabet[size-i:size]
        row = "-".join(left + right)
        lines.append(row.center(4*size - 3, "-"))
    return "\n".join(lines + lines[-2::-1])

if __name__ == "__main__":
    n = int(input().strip())
    print(rangoli(n))
