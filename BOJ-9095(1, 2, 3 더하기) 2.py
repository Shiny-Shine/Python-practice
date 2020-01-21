'''
    2020-01-21 BOJ-9095(1, 2, 3 더하기)

    DP 근본 다지기 2일차. 어느정도 생각이 조금 되는 것 같다.
'''
def dp(n):
    if d[n] != 0:   return d[n]

    d[n] = dp(n - 1) + dp(n - 2) + dp(n - 3)
    return d[n]

d = [0] * 12
d[1] = 1
d[2] = 2
d[3] = 4
d[4] = 7
t = int(input())

for i in range(t):
    n = int(input())
    print(dp(n))