#-*- coding: utf-8 -*-
'''
    2019-12-16 Python Study

    list slicing (리스트 슬라이싱)

    [start idx : end idx + 1]
    [0:3] idx 0~2 까지 3개
    [1:5] idx 1~4 까지 4개
    [:2] 첫 idx~1 까지 2개
    [3:] 3~마지막 idx 까지
'''

# for loop에서 리스트 사용 가능.
# for 변수명 in 배열명 :
a = [7, 6, 9, 4, 2]
for i in a:
    print(i, end = ',')
print("\n")

# slicing
print(a)
print(a[0:3])
print(a[1:5])
print(a[:2])
print(a[3:])