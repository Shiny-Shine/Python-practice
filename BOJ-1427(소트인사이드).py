'''
    2019-12-20 BOJ-1427(소트인사이드)
'''
list = list(input())
list.sort(reverse = True)
for i in list:
    print(i, end = '')
