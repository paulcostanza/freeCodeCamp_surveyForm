def digits_recursion(n):
    if n < 10:
        return 1
    return digits_recursion(n // 10) + 1


print(digits_recursion(10))
print(digits_recursion(11))
print(digits_recursion(100))
print(digits_recursion(1000))