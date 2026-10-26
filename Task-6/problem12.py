# Set .discard(), .remove() & .pop()
# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem


if __name__ == '__main__':
    n = int(input().strip())
    s = set(map(int, input().split()))
    N = int(input().strip())

    for _ in range(N):
        parts = input().split()
        cmd = parts[0]
        if cmd == "pop":
            s.pop()
        elif cmd == "remove":
            s.remove(int(parts[1]))
        elif cmd == "discard":
            s.discard(int(parts[1]))

    print(sum(s))
