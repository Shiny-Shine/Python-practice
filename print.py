# -*- coding: utf-8 -*-
'''
    2019-12-14 Python Study

    Print문 공부
'''

#1. 출력 양식의 지정 (formatting)
#print('양식 문자열(%d등...)' % 값)
print('%d' % 2)
print('%02d' % 5)
print()

#print('양식 문자열들' % (값, 값...))
print('%d, %d, %d' % (2, 4, 6))
print('%.2f' % 3.14159)
print()

#2. 출력의 마지막 문자 지정. (print문 기본값은 \n)
#print('출력 문자열', end = '\n')
print('hello python')
print('hi programmer', end = '\n')
print()

#print('출력 문자열', end = ',')
print('hello', end = ' ')   #개행 안하고 공백 출력
print('python', end = ',')
print('hi', end = ' ')
print('programmer')
print()

#3. 혼합 사용
#print('양식 문자열' % 값, end = '\n')
print('%d+%d = %d' % (2, 4, 6), end = '\n') #기본값 인데 굳이...?
print('%d-%d = ' % (10, 5), end = ' ')
print('%d' % 5)
print('\n\n')

#구구단 출력
for i in range(2, 10):
    for j in range(1, 10):
        print('%02d' % (i * j), end = ' ')
    print()