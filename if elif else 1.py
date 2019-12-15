#-*- coding: utf-8 -*-
'''
    2019-12-15 Python Study

    if elif else 1
'''

#if [참, 거짓으로 판단 가능한 코드]:
#   [조건이 '참'일경우 수행할 코드]

if (1 > 10):
    print('if code 1')
    print('condition is false')

if (1 < 10):
    print("if code 2")
    print("condition is true")

if False:
    print('condition is false')

if True:
    print("condition is true\n")

# 0 = 거짓, 0이아닌  양수,음수 = 참
if 0:
    print('code 1')
if 1:
    print("code 2")
if -2:
    print("code 3\n")

#변수에도 쌉가능
a = 2
if a : print("code 1")

a -= 1
if a : print("code 2")

a -= 1
if a : print("code 3")