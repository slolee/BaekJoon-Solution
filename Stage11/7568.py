T = int(input())
users = []
tier = [1] * T
for t in range(T):
    users.append(list(map(int, input().split())))

for user_index in range(len(users)):
    for target_user_index in range(len(users)):
        if user_index == target_user_index:
            continue

        if users[user_index][0] < users[target_user_index][0] and users[user_index][1] < users[target_user_index][1]:
            tier[user_index] += 1

for i in tier:
    print(i, end=' ')