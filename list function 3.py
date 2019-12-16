#-*- coding: utf-8 -*-
'''
    2019-12-16 Python Study

    list function(함수)

    데이터 개수 함수 (len, count)
    데이터 수정(modify)함수, 데이터 utility 함수

    1. 데이터 개수 : len(list) = list 의 데이터 개수 반환.
    2. 데이터 개수 : count(data) = list에서 헤당 데이터의 개수를 반환.

    3. 데이터 수정 : list 데이터를 할당연산자(=)를 통해 직접 수정.
    4. sort() : list 데이터를 '오름차 or 사전순'으로 정렬.
    5. reverse() : list 데이터를 '역순' 으로 재배치.

'''

# len, count
a = [1, 3, 4, 5, 3, 3, 2, 4, 3]
print("list개수 : %d" % len(a))
print("3은 %d개, 4는 %d개" % (a.count(3), a.count(4)), end = '\n\n')

# len응용
print("origin : ", end = '')
for i in a: print(i, end = ' ')
print()

print("reverse : ", end = '')
for i in range(len(a)):
    print(a[len(a) - i - 1], end = ' ')
    #len - i 에 -1을 해줘야 인덱스 값이 맞음
print('\n')

# 데이터 수정
a = [1, 2, 3, 4, 5]
print(a)

for i in range(len(a)) : a[i] *= 10 # a[i] = a[i] * 10 이랑 같음.
print(a)

a.reverse()
print(a)

a.sort()
print(a)