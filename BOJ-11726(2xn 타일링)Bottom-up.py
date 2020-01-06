'''
    2020-01-06 BOJ-11726(2xn 타일링)Bottom-up

    다니아믹 프로그래밍(DP) 기본 문제. Bottom-up로 재구현
'''
d = [0] * 1001
d[0] = 1
d[1] = 1
num = int(input())

for i in range(2, num + 1):
    d[i] = (d[i - 1] + d[i - 2]) % 10007

print(d[num])