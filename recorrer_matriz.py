import numpy as np

def recorrer_matriz_recursivo(m, filas, cols, i=0, j=0):
    if i == filas - 1 and j == cols - 1:
        return str(m[i][j])
    
    if j == cols - 1:
        return str(m[i][j]) + "\n" + recorrer_matriz_recursivo(m, filas, cols, i + 1, 0)
    else:
        return str(m[i][j]) + " " + recorrer_matriz_recursivo(m, filas, cols, i, j + 1)


def main():
    f = int(input("Ingrese número de filas: "))
    c = int(input("Ingrese número de columnas: "))
    matriz = np.random.randint(0, 100, size=(f, c))
    

    print("\nRecorrido recursivo:")
    print(recorrer_matriz_recursivo(matriz, f, c))


if __name__ == "__main__":
    main()