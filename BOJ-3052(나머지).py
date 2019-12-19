# -*- coding: utf-8 -*-
'''
  2019-12-18 BOJ-3052(나머지)

  C, C++, Python 으로 각각 따로 구현해보았다.
  아직 나한테는 C++이 제일 쉽다. C++는 코드가 술술 나오는데 파이썬은 아직.....
'''

num = [0] * 43
cnt = 0

for i in range(1, 11):
    a = int(input())
    num[a % 42] += 1

for i in num:
    if(i != 0):
        cnt += 1

print(cnt)
