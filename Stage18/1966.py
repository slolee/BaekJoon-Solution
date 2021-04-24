for _ in range(int(input())):
    N, M = map(int, input().split())
    priorities = list(map(int, input().split()))

    from collections import deque
    queue = deque([(i, priorities[i - 1]) for i in range(1, N + 1)])
    cnt = 0
    while queue:
        item = queue.popleft()
        if queue and item[1] < max([q[1] for q in queue]):
            queue.append(item)
        else:
            cnt += 1
            if item[0] == M + 1:
                print(cnt)
                break

