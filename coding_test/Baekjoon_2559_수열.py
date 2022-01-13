# 문제 : https://www.acmicpc.net/problem/2559
# 문제 번호 : 2559

term, days = map(int, input().split())
temp = list(map(int, input().split()))

for i in range(term+1-days):
    if i == 0:
        sumtemp = sum(temp[i:i+int(days)])
        max = sumtemp
    elif i > 0:
        sumtemp = sumtemp-temp[i-1]+temp[i+days-1]
        if sumtemp > max: max = sumtemp
    
print(max)