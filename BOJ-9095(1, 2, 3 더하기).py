'''
    2020-01-03 BOJ-9095(1, 2, 3 더하기)

    점화식이 찾아질 것 같으면서도 안 찾아진다 ㅠㅠ
    n에서 n + 1의 값을 어텋게 정의할지 아직 감이 안잡힌다.
'''
def dp(n):
    if d[n] != 0:   return d[n]

    d[n] = dp(n - 1) + dp(n - 2) + dp(n - 3)
    return d[n]

d = [0] * 12
d[0] = 1
d[1] = 1
d[2] = 2
t = int(input())
for i in range(t):
    n = int(input())
    print(dp(n))