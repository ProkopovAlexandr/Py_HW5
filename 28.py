def summ(num1, num2):
    if num1 == 0:
        return num2
    elif num2 == 0:
        return num1
    elif num1 > 0:
        return summ(num1 - 1, num2 + 1)

print(summ(3,7))