import numpy as np

class Recursividad:
    def suma_n_a_m(self, n, m):
        if m == n:
            return n
        else:
            siguiente = m - 1
            valor = m + self.suma_n_a_m(n, m - 1)
            return valor
    def potencia(self, base, exponente):
        if exponente < 0:
            return 1 / self.potencia(base, -1 * exponente)
        if exponente == 0:
            return 1
        if exponente == 1:
            return base
        else:
            siguiente = exponente - 1
            valor = base * self.potencia(base, exponente - 1)
            return valor
        
    def recorrer_matriz_recursivo(self, m, filas, cols, i=0, j=0):
        if i == filas - 1 and j == cols - 1:
            return str(m[i][j])
        
        if j == cols - 1:
            return str(m[i][j]) + "\n" + self.recorrer_matriz_recursivo(m, filas, cols, i + 1, 0)
        else:
            return str(m[i][j]) + " " + self.recorrer_matriz_recursivo(m, filas, cols, i, j + 1)
        
def main():
    recursividad = Recursividad()
    
    opciones = {
        1: "Sumar desde N a m",
        2: "Potenciación",
        3: "Recorrer matriz",
        4: "Invertir número",
        5: "Determinar palíndromo",
        6: "Buscar en array",
        7: "Salir"
    }
    while True:
        print(f"\nOpciones: \n {opciones}")
        opcion = int(input("\nInserte una opcion: "))

        match opcion:
            case 1:
                try:
                    n = int(input("Inserte n: "))
                    m = int(input("Inserte m: "))
                except Exception as e:
                    print(e)
                if n > m:
                    print("\nN debe ser mayor a m\n")
                else:
                    print(recursividad.suma_n_a_m(n, m))
            case 2:
                try:
                    base = float(input("Inserte el valor de la base: "))
                    exponente = int(input("Inserte el valor del exponente (entero): "))
                    print(recursividad.potencia(base, exponente))
                except Exception as e:
                    print(e)

            case 3:
                try: 
                    f = int(input("Ingrese número de filas: "))
                    c = int(input("Ingrese número de columnas: "))
                except Exception as e:
                    print(e)
                if f <= 0 or c <= 0:
                    print("Debe ingresar valores mayores a 0")
                else:
                    matriz = np.random.randint(0, 100, size=(f, c))
                    print("\nRecorrido recursivo:")
                    print(recursividad.recorrer_matriz_recursivo(matriz, f, c))
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass

            case 7:
                exit("\nAdiós")
            case _:
                print("\nIntente insertando una opción válida")

if __name__ == "__main__":
    main()