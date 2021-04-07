N = int(input())
answer = {0: 0, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}
for i in range(2, N + 1):
    answer = {0: answer[1], 1: answer[0] + answer[2],
              2: answer[1] + answer[3], 3: answer[2] + answer[4],
              4: answer[3] + answer[5], 5: answer[4] + answer[6],
              6: answer[5] + answer[7], 7: answer[6] + answer[8],
              8: answer[7] + answer[9], 9: answer[8]}
if N == 0:
    print(0)
else:
    print(sum(answer.values()) % 1000000000)