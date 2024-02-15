valores = input("Ingrese los numeros del arreglo separados por comas: ")
arreglo = valores.split(',')

def filtro_lista(arreglo):
    resultado = []
    for elemento in arreglo:
        if (divisible(int(elemento)) == True) and (int(elemento) <= 600):
            resultado.append(elemento)
        elif (int(elemento) > 600) and (int(elemento) < 1000):
            continue
        elif int(elemento) > 1000:
            break
    return resultado

def divisible(numero):
    if numero % 5 == 0:
        return True
    else:
        return False

resultado_final = filtro_lista(arreglo)
print("Resultado: ", resultado_final)