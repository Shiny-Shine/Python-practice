#-*- coding: utf-8 -*-
'''
    2019-12-16 Python Study

    list function(함수)

    데이터 추가 함수 (append, insert, extend)

    1. 데이터 추가 : append(data)
       list end 지점에서 데이터를 추가함.

    2. 삽입 : insert(idx, data)
       list의 idx 지점에서 데이터를 삽입시킨다.

    3.  확장 : extend(다른 list)
        새로운 list를 붙여서 데이터를 확장시킨다.
'''

a = [5, 4, 3]
a.append(9)
print(a, end = '\n\n')

a.insert(0, 2)
a.insert(4, 8)
print(a, end = '\n\n')

b = [10, 11, 12]
a.extend(b)
print(a, end = '\n\n')