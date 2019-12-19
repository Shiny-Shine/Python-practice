# -*- coding: utf-8 -*-
'''
    2019-12-19 BOJ-1085(직사각형에서 탈출)

    처음 문제를 볼땐 좌표를 다루는 문제라 어려울 것 같았지만 그렇지 않았다.
    좌표를 다루는 문제는 수학이던 코딩이던 너무 어렵다 ㅠㅠ
'''
x, y, w, h = map(int, input().split())
if x > w - x:
    xx = w - x;
else: xx = x
if y > h - y:
    yy = h - y;
else: yy = y

print(min(xx, yy))
