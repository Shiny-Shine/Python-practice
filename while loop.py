#-*- coding: utf-8 -*-
'''
    2019-12-16 Python Study

    while loop

    while [T/F로 판단가능한 코드]:
          [조건이 '참'일 경우 반복될 코드]

    break : 해당 반복문을 빠져 나간다

    continue : 반복문의 다음 단계로 바로 넘어간다,
    continue밑의 코드는 진행되지 않는다.

    위 2개는 for loop에서도 사용 가능.
'''

#아래 2개의 while문의 결과는 같다.
x = 1
while x <= 10:
    print('%d' % x, end = ' ')
    x += 1

print()
x = 1
while True:
    print('%d' % x, end = ' ')
    x += 1
    if x > 10: break

# 위 두개 반복문의 결과도 같다.
print()
x = 1
while x <= 10:
    x += 1
    if x % 2 == 1: continue
    print('%d' % x, end = ' ')

print()
for x in range(1, 100):
    if x % 2 == 1: continue
    if(x > 10): break
    print('%d' % x, end = ' ')