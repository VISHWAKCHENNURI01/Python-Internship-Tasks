# Nested Lists
# https://www.hackerrank.com/challenges/nested-list/problem


if __name__ == '__main__':
    students = []
    for _ in range(int(input().strip())):
        name = input().strip()
        score = float(input().strip())
        students.append([name, score])

    # Extract all scores
    scores = sorted({s[1] for s in students})   
    second_lowest = scores[1]                   

    # Collect names with that score
    names = [s[0] for s in students if s[1] == second_lowest]

    # Print alphabetically
    for name in sorted(names):
        print(name)
