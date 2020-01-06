'''
    2020-01-06 BOJ-2133(타일 채우기)Bottom-up

    다이나믹 프로그래밍(DP) 기본 문제. Bottom-up로 재구현
'''
d = [0] * 31
d[0] = 1
d[1] = 0
d[2] = 3

n = int(input())
for i in range(2, n + 1):
    d[i] = 3 * d[i - 2]
    for j in range(4, i + 1, 2):
        d[i] += 2 * d[i - j]

print(d[n])