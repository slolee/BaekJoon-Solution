C = int(input())
for i in range(C):
    lst = list(map(int, input().split(' ')))
    N = lst[0]
    stu = lst[1:]

    avg = sum(stu) / N
    temp = len(list(filter(lambda x: x > avg, stu))) / N * 100
    print(f'{temp:.3f}%')