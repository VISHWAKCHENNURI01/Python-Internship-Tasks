# Word Order
# https://www.hackerrank.com/challenges/word-order/problem


from collections import OrderedDict

if __name__ == '__main__':
    n = int(input().strip())
    word_counts = OrderedDict()

    for _ in range(n):
        word = input().strip()
        word_counts[word] = word_counts.get(word, 0) + 1

    # First line: number of distinct words
    print(len(word_counts))

    # Second line: occurrences in order of first appearance
    print(' '.join(str(count) for count in word_counts.values()))

