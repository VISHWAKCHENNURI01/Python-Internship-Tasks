# Finding the Percentage
# https://www.hackerrank.com/challenges/finding-the-percentage/problem


if __name__ == '__main__':
    n = int(input().strip())
    student_marks = {}
    for _ in range(n):
        line = input().split()
        name, scores = line[0], list(map(float, line[1:]))
        student_marks[name] = scores
    
    query_name = input().strip()
    avg = sum(student_marks[query_name]) / len(student_marks[query_name])
    print("{:.2f}".format(avg))
