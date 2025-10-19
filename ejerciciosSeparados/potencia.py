def potencia(base, exponente):
    if exponente < 0:
        return 1 / potencia(base, -1 * exponente)
    if exponente == 0:
        return 1
    if exponente == 1:
        return base
    else:
        siguiente = exponente - 1
        valor = base * potencia(base, exponente - 1)
        return valor
    
def main():
    base = float(input("Inserte el valor de la base: "))
    exponente = int(input("Inserte el valor del exponente (entero): "))

    print(potencia(base, exponente))

if __name__ == "__main__":
    main()