'''
    2020-01-20 BOJ-11726(2xn 타일링) 재시도.
'''
def dp(n):
    if n <= 3:  return n

    if(d[n] != 0):  return d[n]

    d[n] = dp(n - 1) + dp(n - 2)
    return d[n]

d = [0] * 1001
d[1] = 1
d[2] = 2
d[3] = 3
n = int(input())

dp(n)
'''
for i in range(4, n + 1):
    d[i] = d[i - 1] + d[i - 2]
'''
print(d[n])