'''
  2019-12-18 BOJ-4344(평균은 넘겠지)
  
  파이썬에 익숙치 않아 힘들었지만 로직 구현은 문제가 없었다.
'''
def average(list, len):
    return sum(list) / len

c = int(input())

for i in range(c):
    n = list(map(float, input().split()))
    num = n[0]
    score = n[1:]
    avg = average(score, num)
    cnt = 0.0

    for j in score:
        if float(j) >avg:   cnt += 1.0
    persent = cnt / float(num) * 100.0
    print("%.3f%%" % persent)
