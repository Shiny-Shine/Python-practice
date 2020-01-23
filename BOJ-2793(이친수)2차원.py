'''
    2019-12-26 BOJ-2793(이친수) 2차원 구현

'''
d = [[0] * 2 for i in range(91)]
n = int(input())
d[1][0] = 0
d[1][1] = 1

for i in range(2, n + 1):
    d[i][1] = d[i - 1][0]
    d[i][0] = d[i - 1][0] + d[i - 1][1]

print(d[n][0] + d[n][1])