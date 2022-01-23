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
