# 문제 : https://www.acmicpc.net/problem/2870

import sys
import re

if __name__ == "__main__":
    numbers = []
    for _ in range(int(sys.stdin.readline().strip())):
        line = sys.stdin.readline().strip()

        # 받은 문장에서 1 ~ 100자의 숫자 뽑아내기
        numbers.extend(list(map(int, re.findall(r'\d{1,100}', line))))

    numbers = sorted(numbers)

    for number in numbers:
        print(number)

'''
# 정규식 없이 풀기
# https://www.acmicpc.net/source/37255315

n = []
for _ in range(int(input())):
    t = ''
    for i in input():
        if i.isalpha() and t:
            n.append(int(t))
            t = ''
        elif i.isdigit():
            t += i
    if t:
        n.append(int(t))
n.sort()
for i in n:
    print(i)
'''
