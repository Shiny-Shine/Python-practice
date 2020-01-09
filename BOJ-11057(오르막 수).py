'''
    2020-01-09 BOJ-11057(오르막 수)
    
    거의 근접한 접근을 했지만... 혼자 힘으로 풀진 못했다 ㅠㅠㅠ
    내 힘으로 푼 느낌이 없어 푸는 맛도 안나고 공부가 아예 안된 느낌이다. 
'''
n = int(input())
d = [[0] * 10 for i in range(1001)]
for i in range(10): d[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        for k in range(j + 1):
            d[i][k] += d[i - 1][j]
sum = 0
for i in range(10): sum += d[n][i]

print(sum % 10007)
