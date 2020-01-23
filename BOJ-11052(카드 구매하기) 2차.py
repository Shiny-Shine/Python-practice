'''
    2020-01-23 BOJ-11052(카드 구매하기) 2차
'''
n = int(input())
d = [0] * 1001
p = input().split()
for i in range(n):
    p[i] = int(p[i])

for i in range(1, n + 1):
    for j in range(1, i + 1):
        d[i] = max(d[i], d[i - j] + p[j - 1])

print(d[n])