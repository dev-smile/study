# 문제 : https://www.acmicpc.net/problem/1747
# 풀이과정 : https://velog.io/@dev-smile/백준-1747-소수팰린드롬

import sys
input = sys.stdin.readline

def checkPalindrome(i):
  number = list(str(i))
  for j in range(len(number)//2):
    if number[j] == number[len(number) -1 -j]: 
      pass
    else:
      return False
  return True

if __name__ == "__main__":
  N = int(input())
  # 1300000까지 리스트로 만들고 배수를 빼보자, 리스트로 쭉 만들어서 2의 배수 제거, 3의 배수 제거 5의 배수 제거, ...
  
  # 1003002까지 리스트 만들고 소수 제거
  # 1000000이 입력되면 출력 값은 1003002이다. 1000000보다 크거나 같은 소수도 찾아야 한다.
  numberList = [True] * 1003002
  numberList[0] = False
  numberList[1] = False
  for i in range(2, 1003002):
    if numberList[i] == True:
      for j in range(i+i, 1003002, i):
        numberList[j] = False

  # 소수 리스트 만들기
  primeList = []
  for i in range(2, 1003002):
    if numberList[i] == True:
      primeList.append(i)

  # 소수 리스트에서 N보다 크거나 같은 수 찾기
  for i in primeList:
    if i >= N:
      if checkPalindrome(i):
        print(i)
        break


      




