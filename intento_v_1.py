#promedio y desviacion estandar
a=input("dame una lista de numero:\n")
lista=a.split(",")

def promedio_std(lista):
    suma = 0
    for elemento in lista:
        suma += int(elemento) 
        promedio=suma/len(lista)
    from math import sqrt
    sigma=0
    for elemento in lista:
        sigma += (float(elemento)-promedio)**2
        desv=sqrt(sigma/len(lista))
    return ("el promedio de los numeros dados es:",promedio," la desviacion estandar de los numeros dados es:",desv)
print(promedio_std(lista))
input("")

print("primer cambio")
print("segunda modificación")
print("desde rama alterna")
print("modificacion desde rama confilcto")