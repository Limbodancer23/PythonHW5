# Посчитать факториал (произведение 1 до N) и треугольное число (сумма чисел от 1 до N) для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов
n = int(input("Enter number: "))
def operation(n, fac, product):
    if n == 1 or n == 0:
        return print(f"factorial = {fac}, summ = {product}")
    if n > 1:
        product+=n
        fac*=n 
        operation(n-1, fac , product)
    return fac, product
operation(n, 1 , 1)