n = int(input("Ingrese el numero: "))
t = int(input("Ingrese la cantidad de terminos: "))

def sumatoria_serie(n, t):
    if n and t > 0:
        total = 0
        for i in range(t):
            a_sumar = int(concatenacion_n(n, i+1))
            print(a_sumar)
            total += int(a_sumar)
        return total
    else:
        print("ERROR, INGRESE NUMEROS ENTEROS")

def concatenacion_n(n, t):
    resul = str(n) * t
    return resul

resultado = sumatoria_serie(n, t)
print("El resultado es:", resultado)