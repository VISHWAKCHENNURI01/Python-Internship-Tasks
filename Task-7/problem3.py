# Mars Exploration
# https://www.hackerrank.com/challenges/mars-exploration/problem


s = input().strip()

expected = "SOS" * (len(s) // 3)


count = sum(1 for i in range(len(s)) if s[i] != expected[i])

print(count)
