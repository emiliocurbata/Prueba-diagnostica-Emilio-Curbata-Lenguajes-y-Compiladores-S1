def collatz_secuencia(n):
    """Genera la secuencia de Collatz para un número n dado."""
    secuencia = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        secuencia.append(n)
    return secuencia

def main():
    print("=== VERIFICACIÓN DE CONJETURA DE COLLATZ ===")
    print("Nota: para aplicar la demostración debe cumplirse q >= 100p.")
    
    try:
        p = int(input("Introduce el valor de inicio (p): "))
        q = int(input("Introduce el valor final (q): "))
        
        # Validación de la regla según el PDF
        if q < 100 * p:
            print(f"\n[ERROR]: La condición q >= 100p no se cumple.")
            print(f"Para p={p}, q debe ser al menos {100 * p}.")
            return

        print(f"\nVerificando intervalo [{p}, {q}]...\n")
        
        # Procesar intervalo
        for n in range(p, q + 1):
            secuencia = collatz_secuencia(n)
            # Imprimir el resultado de la conjetura
            print(f"n={n}: {' -> '.join(map(str, secuencia))}")
            
        print("\nDemostración completada para el intervalo.")
        
    except ValueError:
        print("Error: Por favor, introduce números enteros válidos.")

if __name__ == "__main__":
    main()