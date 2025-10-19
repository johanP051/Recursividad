def suma_n_a_m(n, m):
    if m == n:
        return n
    else:
        siguiente = m - 1
        valor = m + suma_n_a_m(n, m - 1)
        return valor

def main():
    while True:
        try:
            n = int(input("Inserte n: "))
            m = int(input("Inserte m: "))
        except Exception as e:
            print(e)
        if n > m:
            print("\nN debe ser mayor a m\n")
        else:
            break
        
    print(suma_n_a_m(n, m))

if __name__ == "__main__":
    main()