#-*- coding: utf-8 -*-
'''
    2019-12-16 Python Study

    list function(함수)

    데이터 삭제 함수 (del, remove, pop)

    1. 데이터 삭제 : del data
        list의 요소를 삭제한다 : ex) del a[2]
        list slicing 으로 삭제 : ex) del a[:3]

    2. 데이터 삭제 : remove(data)
        list에서 해당 데이터를 '하나' 없앤다. ex) a.remove(3)
        지우려는 값이 여러개여도 앞의 하나만 지운다.

    3. 데이터 삭제 : pop(idx)
        list의 idx를 제거하고 값을 반환. ex) pop(2)
        idx가 없는 경우는 마지막 데이터를 제거후 반환.    ex) pop()
        마지막 idx의 경우 O(1), 첫 idx의 경우 O(N)의 시간복잡도를 가진다.
'''

# del 은 list의 idx를 념겨줘야함, 값을 넣으면 오류.
a = [2, 4, 5, 9, 1, 3]
del a[1]
print(a, end = '\n\n')

del a[:2]
print(a, end = '\n\n')

# remove 는 중복되는 값이 있어도 앞의 하나만 제거됨.
a = [2, 4, 3, 2, 1, 3]
a.remove(3)
print(a, end = '\n\n')
a.remove(3)
print(a, end = '\n\n')

# pop 은 print 함수 안에서도 사용이 가능하다.
a = [2, 4, 5, 9, 1, 3]
b = a.pop(3)
print(b)
print(a)

print(a.pop())
print(a)