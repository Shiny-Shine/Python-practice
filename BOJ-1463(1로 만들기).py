'''
    2020-01-03 BOJ-1463(1로 만들기)

    2020년 첫 코딩이다...질문 검색에서 답을 찾았다.
    그냥 어렵다.
'''
dp = [0] * 1000001
n = int(input())

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    if(i % 2 == 0): dp[i] = min(dp[i], dp[int(i / 2)] + 1)
    if(i % 3 == 0): dp[i] = min(dp[i], dp[int(i / 3)] + 1)

print(dp[n])