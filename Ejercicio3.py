# Ejercicio 3: Suma de dígitos

def suma_digitos(n):
    # Escriba su codigo acontinuacion
    # Elimine el pass
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10)