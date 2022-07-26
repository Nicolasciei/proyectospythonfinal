def carga_enteros():
    lista_enteros=[]
    for i in range(10):
        entero=int(input("Ingrese un entero(+ y -) : "))
        lista_enteros.append(entero)
    print("La lista de 10 ENTEROS es : ",lista_enteros)
    return lista_enteros

#  Generar dos listas a partir de la primera.
# En una guardar los valores positivos y en otra los negativos.
def generar_listas(lista_10_enteros):
    lista_posit=[]
    lista_neg=[]
    for i in range(10):
        if lista_10_enteros[i]>=0:
            lista_posit.append(lista_10_enteros[i])
        else:
            lista_neg.append(lista_10_enteros[i])

#  Imprimir las dos listas generadas.
    print("La lista de ENTEROS POSITIVOS es : ",lista_posit)
    print("La lista de ENTEROS NEGATIVOS es : ",lista_neg)



# Prog ppal.
# 1- Llamada a 'carga_enteros()'
lista_10_enteros=carga_enteros()

# 2- Llamada a 'generar_listas()'
dos_listas=generar_listas(lista_10_enteros)