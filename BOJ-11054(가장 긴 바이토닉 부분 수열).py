# 2020-06-17 BOJ-11054(가장 긴 바이토닉 부분 수열)
n = int(input())
num = list(map(int, input().split()))
dp = [[0] * 1001 for i in range(2)]  # 2 * 1000 배열, [0][i] = LIS, [1][i] = LDS


def LIS():
    for i in range(n):
        mdp = 1
        for j in range(i):
            if num[i] > num[j] and mdp <= dp[0][j]:
                mdp = dp[0][j] + 1
        dp[0][i] = mdp


def LDS():
    for i in range(n - 1, -1, -1):
        mdp = 1
        for j in range(i, n):
            if num[i] > num[j] and mdp <= dp[1][j]:
                mdp = dp[1][j] + 1
        dp[1][i] = mdp


LIS()
LDS()

lan = 0
for i in range(n):
    lan = max(lan, (dp[0][i] + dp[1][i] - 1))

print(lan)