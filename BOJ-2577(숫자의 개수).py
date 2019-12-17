# -*- coding: utf-8 -*-
'''
    2019-12-17 BOJ-2577(숫자의 개수)

    C로 푼 문제를 파이썬으로 풀어봤다.
    파이썬은 메모리와 시간을 아주 많이 잡아먹는다...
    자료형이 왔다갔다해서 좀 맘에 안든다. 코드는 기적적으로 짧긴 하다.
'''
# a, b, c = input().split()으로 쓰면 공백단위로 입력받음 
a = int(input())
b = int(input())
c = int(input())
cnt = [0] * 10

num = str(a * b * c)

for i in range(len(num)):
    cnt[int(num[i])] += 1

for i in cnt:
    print(i)