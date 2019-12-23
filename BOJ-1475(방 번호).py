# -*- coding: utf-8 -*-
'''
    2019-12-23 BOJ-1475(방 번호)
'''
import sys
import math

rnum = input()
if rnum == 0:
    print(1)
    sys.exit(1)

card = [0] * 10

for i in rnum: card[int(i)] += 1

card[6] = int(math.ceil((card[6] + card[9]) / 2))
card[9] = 0
print(max(card))