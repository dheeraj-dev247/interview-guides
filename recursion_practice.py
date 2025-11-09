# Factorial using recursion

def fact(num):
    if num == 1:
        return num
    return num * fact(num-1)


# print(fact(5))

def fibo(num):
    if num <= 1:
        return num
    return fibo(num-1)+fibo(num-2)

print(fibo(6))