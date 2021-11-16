# 문제 : https://www.acmicpc.net/problem/2447
# 문제 번호 : 2447

def append_star(n):
    if n == 1:
        return ['*']

    Stars = append_star(n//3)
    L = []
    for S in Stars:
        L.append(S*3)
    for S in Stars:
        L.append(S+' '*(n//3)+S)
    for S in Stars:
        L.append(S*3)
    return L

print('\n'.join(append_star(int(input())))) 

# ex) 9 입력 : 9//3 = 3
# Stars = append_star(3) // Stars : ['*']  
#   -> Stars = append_star(1) // Stars : ['*'] 
#   -> for문을 수행하면 // L: ['***', '* *', '***']
#   -> return L
# ***
# * *
# ***

# Stars = append_star(3) // Stars : ['***', '* *', '***'] 
#   -> 첫번째 for문을 수행하면 // L : ['*********', '* ** ** *', '*********']
# *********
# * ** ** *
# *********
#   -> 두번째 for문을 수행하면 // L: ['*********', '* ** ** *', '*********', '***   ***', '* *   * *', '***   ***']
# *********
# * ** ** *
# *********
# ***   ***
# * *   * *
# ***   ***
#   -> 세번째 for문을 수행하면 // L: ['*********', '* ** ** *', '*********', '***   ***', '* *   * *', '***   ***', '*********', '* ** ** *', '*********']
# *********
# * ** ** *
# *********
# ***   ***
# * *   * *
# ***   ***
# *********
# * ** ** *
# *********


# 출처 : https://cotak.tistory.com/38