# Caesar Cipher
# https://www.hackerrank.com/challenges/caesar-cipher-1/problem


def caesarCipher(s, k):
    result = []
    k = k % 26  
    
    for ch in s:
        if ch.isalpha():
            if ch.islower():
                shifted = chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
            else:
                # shift within 'A' to 'Z'
                shifted = chr((ord(ch) - ord('A') + k) % 26 + ord('A'))
            result.append(shifted)
        else:
            result.append(ch)
    
    return "".join(result)

if __name__ == "__main__":
    n = int(input().strip())  
    s = input().strip()
    k = int(input().strip())
    print(caesarCipher(s, k))
