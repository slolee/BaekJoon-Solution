N = int(input())
temp = 1
while N > temp:
    N -= temp
    temp += 1
    
if temp % 2 == 1:
    print(temp + 1 - N, '/', N, sep='')
else:
    print(N, '/', temp + 1 - N, sep='')