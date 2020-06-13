# 2020-06-13 BOJ-11053(가장 긴 증가하는 부분 수열)
# d[n] = n 번째 원소를 마지막으로 하는 LIS의 길이
n = int(input())
dp = [1] * 1001
num = list(map(int, input().split()))
mdp = dp[0]

for i in range(1, n):
    for j in range(i):
        if num[i] > num[j]:
            dp[i] = max(dp[i], dp[j] + 1)
    if dp[i] > mdp: mdp = dp[i]

print(mdp)
