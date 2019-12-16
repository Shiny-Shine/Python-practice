#-*- coding: utf-8 -*-
'''
    2019-12-16 Python Study

    function

    def 함수명(매개인자들...) :
        [코드]

    1. [코드]를 함수호출시 실행시킨다.
    [코드] = :(콜론) 다음줄부터 '들여쓰기'된 모든 코드를 반복 실행.

    2. [매개인자들...]
    [코드] 가 실행될때 전달되어지는 값들에 대한 지역 변수들.
    함수 호출시 이 매개체들을 통해 값들이 함수 안으로 전달된다.
'''

def function1():
    print("hello")

def function2():
    print("python")

function1()
function2()
print()

def func_print(a, b):
    print("finc data : %d, %d" % (a, b))

func_print(10, 20)