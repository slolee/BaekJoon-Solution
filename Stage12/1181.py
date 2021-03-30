import sys

N = int(input())
words = []
for n in range(N):
    word = sys.stdin.readline()
    if (word, len(word)) not in words:
        words.append((word, len(word)))

for i in sorted(sorted(words, key=lambda x: x[0]), key=lambda x: x[1]):
    sys.stdout.write(i[0])
