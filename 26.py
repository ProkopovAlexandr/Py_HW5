def exponent(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)


print(exponent(2, 4))  # 32
print(exponent(3, 3))  # 27