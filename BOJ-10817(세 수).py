# -*- coding: utf-8 -*-
'''
    2019-12-18 BOJ-10817(세 수)

    파이썬이 코드는 정말 기적적으로 짧아진다.
'''
a, b, c = map(int, input().split())

num = [a, b, c]
num.sort()
print(num[1])
