def cargar_datos():
    articulos:[]
    precios:[]
    for x in range(5):
        ar = input("ingrese el nombre de los articulos:")
        articulos.append(ar)
        pre = int(input("ingrese el precio del dicho articulo:"))

        precios.append(pre)
        return [articulos,precios]

def imprimir (articulos,precios):
    print("listado completo de articulos y sus precios:")
    for x in range (len(articulos)):
        print(articulos[x], precios[x])

def precio_mayor(articulos, precios):
  may= precios[0]
  pos = 0
  for x in range (1, len(precios)):
      if precios[x] >may:
          may= precios[x]
          print("articulos con un precio mayor es:",articulos[pos],"su precio es:",may)

def consulta_precios(articulos, precios):
    valor= int(input("ingrese un importe para mostrar los articulos con un precio menor: "))
    for x in range (len(precios)):
        if precios[x] < valor:
            print(articulos[x], precios[x])


#bloqueprincipal
articulos,precios = cargar_datos()
imprimir(articulos,precios)
precio_mayor(articulos,precios)
consulta_precios(articulos,precios)

