# 2020-06-13 BOJ-11722(가장 긴 감소하는 부분 수열)
# d[n] = n 번째 원소를 마지막으로 하는 LDS(Longest Decreasing Subsequence)의 길이
n = int(input())
dp = [1] * 1001
num = list(map(int, input().split()))
mdp = dp[0]

for i in range(1, n):
    for j in range(i):
        if num[i] < num[j]:
            dp[i] = max(dp[i], dp[j] + 1)
    if dp[i] > mdp: mdp = dp[i]

print(mdp)
