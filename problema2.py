import re

def validar_fen(cadena):
    """
    Valida si una cadena sigue el formato FEN.
    La estructura consta de:
    1. Colocación de piezas (8 filas)
    2. Color activo (w/b)
    3. Disponibilidad de enroque
    4. Objetivo de en passant
    5. Reloj de medio movimiento
    6. Número de movimiento completo
    """
    # Expresión regular ajustada para la estructura FEN
    fen_pattern = (
        r'^([pnbrqkPNBRQK1-8]{1,8}/){7}[pnbrqkPNBRQK1-8]{1,8}\s' # Tablero
        r'[wb]\s'                                               # Color activo
        r'(-|[KQkq]{1,4})\s'                                    # Enroque
        r'(-|[a-h][36])\s'                                      # En passant
        r'\d+\s\d+$'                                            # Relojes
    )
    
    return bool(re.match(fen_pattern, cadena))

def main():
    print("--- Validador de Notación FEN (Forsyth-Edwards) ---")
    print("Introduce la cadena FEN para validar (o 'salir' para terminar):")
    
    while True:
        entrada = input("\nFEN > ")
        
        if entrada.lower() == 'salir':
            print("Cerrando validador.")
            break
            
        if validar_fen(entrada):
            print("✅ La cadena es VÁLIDA según la notación FEN.")
        else:
            print("❌ La cadena NO es válida. Asegúrate de incluir los 6 campos requeridos.")

if __name__ == "__main__":
    main()
