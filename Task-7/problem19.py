# Weighted Uniform Strings
# https://www.hackerrank.com/challenges/weighted-uniform-string/problem


def weightedUniformStrings(s, queries):
    weights = set()
    prev_char = ""
    run_length = 0
    
    for ch in s:
        val = ord(ch) - ord('a') + 1
        if ch == prev_char:
            run_length += 1
        else:
            run_length = 1
            prev_char = ch
        weights.add(val * run_length)
    
    return ["Yes" if q in weights else "No" for q in queries]

if __name__ == "__main__":
    s = input().strip()
    n = int(input().strip())
    queries = [int(input().strip()) for _ in range(n)]
    results = weightedUniformStrings(s, queries)
    for r in results:
        print(r)
