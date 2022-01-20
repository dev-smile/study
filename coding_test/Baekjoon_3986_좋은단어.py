# 문제 : https://www.acmicpc.net/problem/3986
# 문제 번호 : 3986

n = int(input())

good = 0

while n > 0:
    word = list(input())
    i = 0
    w_stack = []
    for w in word:
        if len(w_stack) > 0:
            t = w_stack[-1]
            tt = w
            if w_stack[-1] == w:
                w_stack.pop()
            else:
                w_stack.append(w)
        else:
            w_stack.append(w)
    if len(w_stack) == 0:
        good += 1
    n -= 1

print(good)