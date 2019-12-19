# -*- coding: utf-8 -*-
'''
    2019-12-17 BOJ-2577(숫자의 개수)

    등신같이 괄호 이상하게 써서 틀렸다.
    가 아니라 입력을 잘못 받았다. 파이썬에서 공백 단위로 입력받으러면 코드를 다르게 짜야하나보다.
'''
mon, day= input().split()
mon = int(mon)
day = int(day)
sum = 0
week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

for i in range(1, mon):
    if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
        sum += 31 % 7
    elif i == 4 or i == 6 or i == 9 or i == 11:
        sum += 30 % 7

print(week[(sum + day) % 7])
