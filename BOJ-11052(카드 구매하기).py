'''
    2020-01-07 BOJ-11052(카드 구매하기)

    하... 문제를 풀어도 공부가 되는 느낌이 안 든다.
    그냥 풀자니 아예 답이 안보이고, 그렇다고 인터넷을 뒤지면
    아예 점화식을 알려줘서 내 힘으로 풀지를 못한다...
    미치겠다...
    또, 파이썬은 배열 다루기가 참 어렵다 ㅠㅠ
'''
d = [0] * 1001
n = int(input())
cost = list(map(int, input().split()))
cost.insert(0, 0)

for i in range(1, n + 1):
    for j in range(1, i + 1):
        d[i] = max(d[i], d[i - j] + cost[j])

print(d[n])
