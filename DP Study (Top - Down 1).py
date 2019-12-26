'''
    -*- coding: utf-8 -*-
    2019-12-26 DP Study (Top - Down 1)

    DP 알고리즘을 공부하는 중. 1~n까지 합 구하기.
'''
n = int(input())
sum = 0

# 일반 반복문 돌리는 방식.
for i in range(1, n + 1):
    sum += i
print(sum)

#가우스 공식.
sum = ((n + 1) * n) / 2
print(sum)

# DP
sum = 0
d = [0] * 100000

def dp(n):
    # 1. base check
    if n == 1:  return 1

    # 2. memoization
    if d[n] > 0: return d[n]

    # 3. recurrence formula(점화식)
    d[n] = dp(n - 1) + n
    return d[n]

sum = dp(n)
print(sum)