# 문제 : https://www.acmicpc.net/problem/2870

import sys
import re

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())

    numbers = []
    while n > 0:
        line = sys.stdin.readline().strip()

        # 받은 문장에서 1 ~ 100자의 숫자 뽑아내기
        numbers.extend(list(map(int, re.findall(r'\d{1,100}', line))))
        n -= 1

    numbers = sorted(numbers)

    for number in numbers:
        print(number)
