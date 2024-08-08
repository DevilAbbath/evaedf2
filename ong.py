def factorial(n):
    if n < 0:
        return ValueError("No pueden ser numeros negativos")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def productoria(lista):
    if not lista:
        return 1
    result = 1
    for num in lista:
        result *= num
    return result

def controlcalculos(**kwargs):
    for k, v in kwargs.items():
        if 'fact' in k:
            factres = factorial(v)
            print(f"El Factorial de {v} es {factres}")
        elif 'prod' in k:
            prodres = productoria(v)
            print(f"La Produtoria de {v} es {prodres}")
        else:
            print(f"Argumento no reconocido: {k}")

if __name__ == '__main__':
    controlcalculos(fact1 = 5, prodt = [4,6,7,4,3], fact2 = 6)
