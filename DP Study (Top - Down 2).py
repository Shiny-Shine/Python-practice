'''
    -*- coding: utf-8 -*-
    2019-12-26 DP Study (Top - Down 2)

    DP 알고리즘을 공부하는 중. 피보나치 수열 구하기.
'''

d = [0] * 100000

def dp(n):
    # 1. base check
    if n <= 1:  return n

    # 2. memoization
    if d[n] > 0: return d[n]

    # 3. recurrence formula(점화식)
    d[n] = dp(n - 1) + dp(n - 2)
    return d[n]

num = int(input())
print(dp(num))