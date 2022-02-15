def factorial_recursive(n):
    print("n의 값 :", n)
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

print(factorial_recursive(5))

'''
5 * factorial_recursive(4)
    4 * factorial_recursive(3)
        3 * factorial_recursive(2)
            2 * factorial_recursive(1)
= 5 * 4 * 3 * 2 * 1
'''