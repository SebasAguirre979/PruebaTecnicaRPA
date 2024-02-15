valores = input("Ingrese los numeros del arreglo separados por comas: ")
arreglo = valores.split(',')

def modificar_arreglo (arreglo):
    indice = 0
    resultado_final = []
    while arreglo:
        elemento = arreglo.pop(indice)
        resultado_elemento = comparar(elemento, arreglo)
        resultado_final.append(resultado_elemento)
    return resultado_final

def comparar(numero, arreglo):
    resul = [numero]
    for elemento in arreglo[:]:
        if elemento == numero:
            resul.append(elemento)
            arreglo.remove(elemento)
    return resul

resultado_final2 = modificar_arreglo(arreglo)
print("Resultado: ", resultado_final2)