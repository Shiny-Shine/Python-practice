'''
    -*- coding: utf-8 -*-
    2019-12-26 BOJ-11726(2xn타일링)

'''
d = [0] * 100000
num = int(input())

def dp(n):
    # base check
    if n < 4:  return n

    # memoization
    if d[n] > 0: return d[n]

    # recurrence fomula
    d[n] = dp(n - 1) + dp(n - 2)
    return d[n]

print(dp(num) % 10007)