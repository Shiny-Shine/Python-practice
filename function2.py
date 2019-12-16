#-*- coding: utf-8 -*-
'''
    2019-12-16 Python Study

    function

    반환값 (return)을 가지는 함수는 매개체를 통해 들어온 값을 기반으로
    연산을 수행하고 힘의의 결과값을 만들어 생산한다. (반환값을 가진다)

    그렇지 않는 함수는 자신에게 구성된 코드만 수행하고 종료된다.  (반환값을 가지지 않는다)
'''

def sum(a, b):
    res = a + b
    return res

a =10
b = 10
c = sum(a, b)

print(a, b, c)

def func1():
    print("hi python")
def func2(a, b):
    print("%d + %d = %d" % (a, b, a + b))

func1()
func2(50, 60)