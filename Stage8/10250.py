T = int(input())
for t in range(T):
    H, W, N = map(int, input().split())
    num = N // H if N % H == 0 else N // H + 1
    floor = H if N % H == 0 else N % H
    print(floor, str(num).zfill(2), sep='')