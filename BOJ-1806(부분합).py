# -*- coding: utf-8 -*-
'''
    2019-12-20 BOJ-1806(부분합)

    투 포인터 알고리즘을 이용해 풀었고, 런타임 오류를 뿜어내서 삽질했다.
    삽질한 이유는 모르겟다, 코드를 갈아엎고 새로 짜서 맞았다.
    더 빨리 풀수 있었으나, 이전에 한번 풀었던 문제를 가지고 삽질해 멘탈이 나가
    더 오래(1시간) 삽질했던 것 같다.
'''
import sys

n, s = map(int, input().split())
num = list(map(int, input().split()))

left = right = sums = 0
result = 987654321

while True:
    if sums < s:
        if right == n:  break
        sums += num[right]
        right += 1
    else:
        result = min(result, right - left)
        sums -= num[left]
        left += 1

print(result if result != 987654321 else 0)
