#-*- coding: utf-8 -*-
'''
    2019-12-16 Python Study

    list

    list = 여러 개의 데이터를 하나의 변수에 묶는다.
    
    1.  []대괄호(bracket)로 묶는다.
        리스트명 = [data1, d2, d3, ...]

    2. 인덱싱(indexing)
        0번부터 시작한다.  (zero-based)
        데이터를 index(일종의 목차)값을 통해 접근한다.
        리스트명[index값]
'''

# Test 1
a = [1, 2, 3, 4, 5]
print(a[0])
print(a[1] + a[4])
print()

# Test 2
for i in range(5): print(a[i], end = ',')
print()
# 역순 인덱싱, 인덱스에서 -1은 뒤에서 첫 번째를 뜻함, a[-1] == 5
for i in range(-1, -6, -1): print(a[i], end = ',')
# -1부터 -5까지, -1씩 감소
print()