N = int(input())
dists = list(map(int, input().split()))
costs = list(map(int, input().split()))

answer = 0
lst = [0] * (N - 1)
for i in range(N - 1):
    if lst[i]:
        continue
    for j in range(i, len(costs) - 1):
        if costs[i] > costs[j]:
            break
        lst[j] = costs[i]
print(sum([lst[n] * dists[n] for n in range(N - 1)]))