#-*- coding: utf-8 -*-
'''
    2019-12-16 Python Study

    ternary operator(3항 연산자)

    ['참'일 때의 값] if [조건] else ['거짓'일때의 값]

    '값'에 대한 표현식.
    해당 표현식에 조건에 대한 내용을 추가시켜서
    일종의 '양자택일'이 가능한 형태로 표현한 수식이다.
'''

# 1 ~ N까지의 짝수 개수 구하기.
cnt = 0
N = 100
for x in range(1, N + 1):
    cnt += 1 if x % 2 == 0 else 0
    # [cnt += 1] if [x % 2 == 0] else [0]
print(cnt)
print()

# 간단한 별찍기
for x in range(10):
    print('*' if x % 2 == 0 else ' ', end = '')
print()

for x in range(10):
    print(' ' if x % 2 == 0 else '*', end = '')
print()