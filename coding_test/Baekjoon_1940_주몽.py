# 문제 : https://www.acmicpc.net/problem/1940
# 문제 번호 : 1940

# 76ms
n = int(input())
m = int(input())
materials = sorted(list(map(int, input().split())))

count = 0
i = 0
j = n - 1

while i < j:
    tmp = materials[i] + materials[j]
    if tmp == m:
        count += 1
        i = i + 1
        j = j - 1
    elif tmp > m:
        j = j - 1
    elif tmp < m:
        i = i + 1

print(count)

'''
# 3184ms
n = int(input())
m = int(input())

count = 0

meterials = list(map(int, input().split()))
meterials.sort()

# m - 검사할 숫자가 리스트에 있으면 카운트 증가
for i in range(n):
    if m-meterials[i] in meterials:
        count += 1

print(int(count/2))
'''
