N = int(input())
count = len(str(N))
construct = 0
if N >= 20:
    for i in range(N - (count * 10), N):
        tmp = str(i)
        if i + sum(map(int, tmp)) == N:
            if construct == 0 or construct > i:
                construct = i
print(construct)