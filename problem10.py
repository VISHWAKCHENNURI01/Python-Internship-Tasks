# Swap Case
# https://www.hackerrank.com/challenges/swap-case/problem


if __name__ == '__main__':
    n = int(input().strip())
    word_counts = {}

    for _ in range(n):
        word = input().strip()
        word_counts[word] = word_counts.get(word, 0) + 1


    print(len(word_counts))

    print(' '.join(str(count) for count in word_counts.values()))
