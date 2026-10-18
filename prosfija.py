def evaluar_posfija(expresion):
    pila = []
    # Separamos la expresión por espacios para manejar números y operadores
    tokens = expresion.split()
    
    for token in tokens:
        # Verificamos si el token es un número (incluyendo negativos)
        try:
            numero = float(token)
            pila.append(numero)
        except ValueError:
            # Si no es un número, debe ser un operador
            if len(pila) < 2:
                raise ValueError("Expresión mal formada: faltan operandos.")
            
            b = pila.pop()  # Segundo operando
            a = pila.pop()  # Primer operando
            
            if token == '+':
                pila.append(a + b)
            elif token == '-':
                pila.append(a - b)
            elif token == '*':
                pila.append(a * b)
            elif token == '/':
                if b == 0:
                    raise ZeroDivisionError("Error: División entre cero.")
                pila.append(a / b)
            elif token == '^' or token == '**':
                pila.append(a ** b)
            else:
                raise ValueError(f"Operador desconocido: {token}")
                
    if len(pila) != 1:
        raise ValueError("Expresión mal formada: demasiados operandos.")
        
    return pila[0]

# --- Ejemplo de uso ---
# Expresión posfija: 3 4 + 2 * 7 / 
# Equivale en notación infija a: ((3 + 4) * 2) / 7
expresion = "3 4 + 2 * 7 /"
resultado = evaluar_posfija(expresion)
print(f"Expresión: {expresion}")
print(f"Resultado: {resultado}")