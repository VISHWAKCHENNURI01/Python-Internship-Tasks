# String Split and Join
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem




def split_and_join(line):
    # write your code here
    words = line.split()
    new = "-".join(words)
    return new

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
