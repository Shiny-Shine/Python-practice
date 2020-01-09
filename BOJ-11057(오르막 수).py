'''
    2020-01-09 BOJ-11057(오르막 수)
'''
n = int(input())
d = [[0] * 10 for i in range(1001)]
for i in range(10): d[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        for k in range(j + 1):
            d[i][k] += d[i - 1][j]
sum = 0
for i in range(10): sum += d[n][i]

print(sum % 10007)