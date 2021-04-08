# def solution(lst):
#     global N, RGB, min_value
#
#     if len(lst) == N:
#         print(lst)
#         total = RGB[0][0][lst[0]] + RGB[1][0][lst[1]] + RGB[2][0][lst[2]]
#         if total < min_value:
#             min_value = total
#         return
#
#     for rgb in [0, 1, 2]:
#         if RGB[len(lst)][0][rgb] == RGB[len(lst)][1]:
#             continue
#         if len(lst) > 0 and lst[-1] == rgb:
#             continue
#
#         lst.append(rgb)
#         solution(lst)
#         lst.pop()
#
#
# N = int(input())
# RGB = []
# for n in range(N):
#     rgb = list(map(int, input().split()))
#     RGB.append([rgb, max(rgb)])
#
# min_value = 99999999999999999
# solution([])
# print(min_value)
#

answer = []

N = int(input())
for n in range(N):
    R, G, B = map(int, input().split())
    if len(answer) > 0:
        answer.append((R + min(answer[-1][1], answer[-1][2]), G + min(answer[-1][0], answer[-1][2]), B + min(answer[-1][0], answer[-1][1])))
    else:
        answer.append((R, G, B))
print(min(answer[-1]))
