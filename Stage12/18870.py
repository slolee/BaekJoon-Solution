import sys

N = int(sys.stdin.readline())
Xs = list(map(int, sys.stdin.readline().split()))

sorted_Xs = sorted(set(Xs))
xt = {sorted_Xs[i]: i for i in range(len(sorted_Xs))}
for i in Xs:
    sys.stdout.write(str(xt[i]) + ' ')