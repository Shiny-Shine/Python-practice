'''
    2020-01-03 BOJ-2193(이친수)

    혼자 풀었다.
    다만 이번에도 n + 1의 값을 정의하려고 찾아보니 규칙성을 찾아 풀었다.
    조금만 더 하면 뭔가 보일 것 같은데 ㅠㅠ
    내가 점화식을 찾으면 이 점화식이 맞는 지 확신이 안 선다.
'''
def dp(n):
    if d[n] != 0:   return d[n]

    d[n] = dp(n - 1) + dp(n - 2)
    return d[n]

d = [0] * 91
d[1] = 1
d[2] = 1
n = int(input())
print(dp(n))