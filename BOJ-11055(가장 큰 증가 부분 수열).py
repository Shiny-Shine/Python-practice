# 2020-06-13 BOJ-11055(가장 큰 증가 부분 수열)
n = int(input())
num = list(map(int, input().split()))
dp = [0] * 1001
dp[0] = num[0]
mdp = num[0]

for i in range(1, n):
    for j in range(i):
        if num[i] > num[j]:
            dp[i] = max(dp[i], dp[j] + num[i])
    dp[i] = max(dp[i], num[i])
    if dp[i] > mdp: mdp = dp[i]

print(mdp)
