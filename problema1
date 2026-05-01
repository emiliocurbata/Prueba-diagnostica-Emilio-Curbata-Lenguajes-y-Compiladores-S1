import re

def mostrar_reglas():
    """Imprime las reglas del problema según el enunciado."""
    print("=== REGLAS DEL PROBLEMA ===")
    print("1. NUMERO: Debe ser un entero o un real con '.' como decimal, sin signo.")
    print("2. OPERANDO: No debe tener espacios ni iniciar con un número (ej. VALOR, A, B).")
    print("3. OPERADOR: Debe ser alguno de los siguientes: +, -, *, /.")
    print("===========================")

def analizar_cadena(cadena):
    """Clasifica los componentes de la cadena según las reglas."""
    # Definición de tokens basada en los requerimientos
    token_specification = [
        ('NUMERO',    r'\d+(\.\d+)?'),           # Entero o real con punto, sin signo
        ('OPERATOR',  r'[\+\-\*/]'),             # Operadores definidos
        ('PAREN_IZQ', r'\('),                    # Paréntesis izquierdo
        ('PAREN_DER', r'\)'),                    # Paréntesis derecho
        ('OPERANDO',  r'[a-zA-Z_][a-zA-Z0-9_]*'), # No inicia con número, sin espacios
        ('MISMATCH',  r'\S+'),                   # Cualquier otra cosa es un ERROR
    ]
    
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    resultados = []
    
    for mo in re.finditer(tok_regex, cadena):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'MISMATCH':
            resultados.append(('ERROR', value))
        else:
            resultados.append((kind, value))
            
    return resultados

def main():
    mostrar_reglas()
    
    while True:
        print("\nIntroduce una expresión aritmética para analizar (o escribe 'salir' para terminar):")
        entrada = input("> ")
        
        if entrada.lower() == 'salir':
            print("Finalizando programa.")
            break
            
        # Ejecutar análisis
        tokens = analizar_cadena(entrada)
        
        print("\nSalida:")
        for tipo, valor in tokens:
            print(f"{tipo} {valor}", end=" ")
        print() # Salto de línea al final

if __name__ == "__main__":
    main()
