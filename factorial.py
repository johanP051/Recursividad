n = int(input("Inserte n: "))

def factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    else:
        siguiente = n - 1
        valor = n * factorial(n - 1)
        return valor

print(factorial(n))
