'''
    2020-02-13 BOj-11057(오르막 수)
'''

d = [[0] * 10 for i in range(1001)]
for i in range(10): d[1][i] = 1
n = int(input())

for i in range(2, n + 1):
    for j in range(10):
        for k in range(j, 10):
            d[i][j] += d[i - 1][k]
            d[i][j] %= 10007

sum = 0
for i in range(10): sum += d[n][i]
print(sum % 10007)