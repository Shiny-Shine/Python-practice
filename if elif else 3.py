#-*- coding: utf-8 -*-
'''
    2019-12-16 Python Study

    if elif else 3

    if ['참/거짓'으로 판단가능한 코드] : 
       [위 조건이 '참(True)'일 경우 수행할 코드]

    elif ['참/거짓'으로 판단가능한 코드] : 
       [위 조건이 '참(True)'일 경우 수행할 코드]

    else : 
       [모든 조건이 거짓(False)일 경우 수행할 코드]

    1. 위에서 부터 순차적으로 조건을 검색하며 내려온다.
    2. 모든 구문이 하나의 구문으로 묶여 있다.
       즉, 위 3개의 수행코드 중 '하나'의 코드만 수행한다.
'''

# 비교 연산자의 결과값을 출력하면 True/False가 나온다.
x = 10
y = 20
print(x > y)
print()

# 조건이 참이면 if, 거짓이면 else문 수행.
y = 5
for x in range(10):
    if x < y:
        print("small")
    else:
        print("big")
print()

score = 75
# if문들 중 하나만 수행됨. (처음으로 조건에 맞는 if문 수행)
if score >= 90: print("A")
elif score >= 80: print("B")
elif score >= 70: print("C\n")
elif score >= 60: print("D")
else: print("F")

score = 88
# 조건에 맞는 if문들 전부 수행됨.
if score >= 90: print("A")
if score >= 80: print("B")
if score >= 70: print("C")
if score >= 60: print("D\n")
else: print("F")