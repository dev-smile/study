# 문제 : https://www.acmicpc.net/problem/10709
# 문제 번호 : 10709

h, w = map(int, input().split())

pred = ''
for i in range(h):
    pred_n = 0
    for c in list(input()):
        if c == 'c':
            pred = pred + '0 '
            pred_n = 1
        elif pred_n > 0:
            pred = pred + str(pred_n) + ' '
            pred_n = pred_n + 1
        else:
            pred = pred + '-1 '
    pred = pred[:-1] + '\n'

print(pred)