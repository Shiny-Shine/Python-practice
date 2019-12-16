#-*- coding: utf-8 -*-
'''
    2019-12-15 ~ 16 Python Study

    if elif else 2

    세가지의 논리 연산자이다, 아래 규칙에 따라 논리적인 연산을 수행한다.

    논리 연산자 and             논리 연산자 or            논리 연산자 not
    True and True : 참          True or True : 참         not True : 거짓 
    True and False : 거짓       True or False : 참        not False : 참 
    False and True : 거짓       False or True : 참
    False and False : 거짓      False or False : 거짓
'''

# and 연산
if True and True : print("code 1\n")
if True and False : print("code 2")
if False and True : print("code 3")
if False and False : print("code 4")

# or 연산
if True or True : print("code 1")
if True or False : print("code 2")
if False or True : print("code 3\n")
if False or False : print("code 4")

# not 연산
if not True : print("code 1")
if not False : print("code 2\n")