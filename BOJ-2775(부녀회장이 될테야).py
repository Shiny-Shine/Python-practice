'''
    -*- coding: utf-8 -*-
    2019-12-26 BOJ-2775(부녀회장이 될테야)
    
    크리스마스 전후로 며칠 놀다 푼거라 쉬운 문제인데 많이 버벅였다.
    파이썬 2차원 배열은 C에서 malloc으로 2차원 동적할당 하는것과 같아서 헷갈린다.
'''

room = [[0] * 15 for i in range(15)]
for i in range(1, 15):
    room[0][i] = i
    room[i][1] = 1

for i in range(1, 15):
    for j in range(1, 15):
        room[i][j] = room[i - 1][j] + room[i][j - 1]

t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())
    print(room[k][n])
