'''
    2020-01-20 BOJ-1463(1로 만들기)
'''
d = [0] * 1000001
n = int(input())
d[2] = 1
d[3] = 1

for i in range(4, n + 1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0:  d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:  d[i] = min(d[i], d[i // 3] + 1)
print(d[n])