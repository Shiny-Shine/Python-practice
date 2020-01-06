'''
    2020-01-06 BOJ-1463(1로 만들기)Top-down

    다이나믹 프로그래밍(DP) 기본 문제. Top-down로 재구현...해보려 했으나
    MemoryError: Stack overflow...  어디서 많이 보던 사이트인데..
    입력 쵀댓값이 좀 많이 커서(10^6) 재귀를 쓰는 Top-down 방식으로는 커버가 불가능하다.
'''
import sys

sys.setrecursionlimit(10000001)

def dp(n):
    if n == 1:  return 0
    if n == 2:  return 1

    if d[n] != 0:   return d[n]

    d[n] = dp(n - 1) + 1
    if n % 2 == 0:  d[n] = min(d[n], dp(int(n / 2)) + 1)
    if n % 3 == 0:  d[n] = min(d[n], dp(int(n / 3)) + 1)
    return d[n]

d = [0] * 1000001
d[1] = 0
d[2] = 1
n = int(input())

print(dp(n))