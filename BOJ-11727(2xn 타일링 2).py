'''
    -*- coding: utf-8 -*-
    2019-12-26 BOJ-11727(2xn타일링 2)

    점화식 찾는 게 너무 힘들다ㅠㅠ 수학이 약해서...
    파이썬에서는 안전상 재귀 횟수를 1000회로 제한한다고 한다.
    sys.setrecursionlimit() 함수로 원하는 횟수로 바꿀 수 있다.
'''
import sys
sys.setrecursionlimit(2000)
d = [0] * 100000
d[1] = 1
d[2] = 3

def dp(n):
    # base check
    if n < 2:  return n

    # memoization
    if d[n] > 0: return d[n]

    # recurrence fomula
    d[n] = (dp(n - 1) % 10007 + 2 * dp(n - 2) % 10007) % 10007
    return d[n] % 10007

num = int(input())
print(dp(num) % 10007)