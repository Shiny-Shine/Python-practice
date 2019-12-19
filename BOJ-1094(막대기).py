# -*- coding: utf-8 -*-
'''
    2019-12-19 BOJ-1094(막대기)

    파이참의 디버깅에 조금 익숙해 지면서 문제풀이가 조금 더 수월해졌다.
    이전에 풀때는 수학적 접근이 안되서 풀고나서도 몰랐는데 이번엔 풀렸다.
'''
stick = 64
cnt = 0
sum = 0
num = int(input())
while sum != num:
    if stick <= num:
        if(sum + stick <= num):
            sum += stick
            cnt += 1
    stick /= 2

print(cnt)
