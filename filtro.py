import sys

# Diccionario de precios
prices = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}

def filterproducts(umbral, condicion='mayor'):
    if condicion not in ['mayor', 'menor']:
        return "error en la operacion"

    if condicion == 'mayor':
        productfilter = {k: v for k, v in prices.items() if v > umbral}
    else: # condicion == 'menor'
        productfilter = {k: v for k, v in prices.items() if v < umbral}

    return productfilter

def main():

    args = sys.argv[1:]

    if len(args) == 0:
        print("Uso: python filtro.py <umbral> [mayor/menor] ")
        return
    
    try:
        umbral = int(args[0]) # umbral
    except ValueError:
        print("El Umbral debe ser numero entero")  
        return
    
    if len(args) == 2:
        condicion = args[1]
    else:
        condicion = 'mayor'

    result = filterproducts(umbral, condicion)

    if result == "error en la operacion":
        print (result)
    else:
        product = ', '.join(result.keys())
        if condicion == 'mayor':
            print(f"Productos mayores al umbral son: {product}")
        else:
            print(f"Productos menores al umbral son: {product}")

if __name__ == "__main__":
    main()