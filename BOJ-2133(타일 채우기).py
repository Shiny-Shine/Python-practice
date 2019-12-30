'''
    2019-12-30 BOJ-2133(타일 채우기)

    오늘도 삽질!
    점화식은 찾았으나 예외 변수를 생각하지못해 질문검색을 했고
    점화식이 완성되어 잘 돌아가는 듯 하니 틀렸다 나와서 c++ 코드로 옮겨봤는데
    c++은 맞고 파이썬은 틀리다... 값이 다른 이유는 단순히 for문 range에 + 1을 안해줘서 이다
    와 ! 삽질 !
'''
d = [0] * 31

def dp(n):
    if n == 0:  return 1
    if n == 1:  return 0
    if n == 2:  return 3
    if d[n] != 0:   return d[n]
    result = 3 * dp(n - 2)
    for i in range(3, n + 1):
        if i % 2 == 0:  result += 2 * dp(n - i)
    d[n] = result
    return d[n]

num = int(input())
print(dp(num))
