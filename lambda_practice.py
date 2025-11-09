square = lambda x:x*x
# print(square(5))

# Example 2: Lambda with Multiple Arguments

add = lambda a,b:a+b
# print(add(3,4))


# Example 3: Using Lambda Inside Another Function

def power(num):
    return lambda x:x**num

square = power(2)
cube = power(3)

# print(square(3))
# print(cube(3))


nums = [1,2,3,4]
squares = list(map(lambda x:x**2,nums))
# print(squares)

