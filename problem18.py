# Lists
# https://www.hackerrank.com/challenges/python-lists/problem


if __name__ == '__main__':
    N = int(input().strip())
    lst = []

    for _ in range(N):
        cmd = input().split()
        op = cmd[0]

        if op == "insert":
            i, e = int(cmd[1]), int(cmd[2])
            lst.insert(i, e)
        elif op == "print":
            print(lst)
        elif op == "remove":
            e = int(cmd[1])
            lst.remove(e)
        elif op == "append":
            e = int(cmd[1])
            lst.append(e)
        elif op == "sort":
            lst.sort()
        elif op == "pop":
            lst.pop()
        elif op == "reverse":
            lst.reverse()
