productos = {



 "8475HD": ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'], #notebook hp $387990, 10
 '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'], #notebook acer $327990, 4
 'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'], #notebook asus $424990, 1
 'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'], #notebook hp i $664990,21
 'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'], #notebook asus $749990, 2
 '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'], #notebook acer i $290890, 32
 '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'], #notebook acer $444990, 7
 'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'], #notebook dell $349990, 1

}
stock = {


 '8475HD': [387.990,10], '2175HD': [327.990,4], 'JjfFHD': [424.990,1],
 'fgdxFHD': [664.990,21], '123FHD': [290.890,32], '342FHD': [444.990,7],
 'GF75HD': [749.990,2], 'UWU131HD': [349.990,1], 'FS1230HD': [249.990,0],
 }




def busqueda_precio():
  precio = float(input("ingrese el precio a consultar: "))
  model = []
  for clav,val in product.items():
    if val[0] <= precio:
      model.append(clav)
      if model:
        print(f"los modelos que cumplen son: {model}")
      else:
        print("no hay modelos que cumplan con el precio ingresado")
        return model
    else:
      print("no hay modelos que cumplen con el precio")
      return model 



def stock_marca():
     modelo = []
     total = 0
     marca = input("ingrese marca a consultar: ")
     for clave, valor in productos.items():
         if marca  == valor[0]:
          modelo.append(clave)
     for modelo_actual in modelo:
         if modelo_actual in stock:
           precio, cantidad = stock[modelo_actual]
           total+= cantidad
     print(f"El stock es: {total}")


def mostrar():
 for compu, lista in productos.items():
   print(f'compu: {lista[0]} modelo: {compu[0]} ram: {lista[2]} disco: {lista[4]}')




while True:
 print("***MENU PRINCIPAL***")
 print("1. Stock marca")

 print("2. Busqueda por precio")
 print("3. Listado de productos")
 print("4. Salir")
 opc=input("ingrese opcion: ")
 if opc=="1":
  stock_marca()
 elif opc=="2":
  busqueda_precio()
 elif opc=="3":
   mostrar()
 elif opc=="4":
   print("Programa Finalizado")
   break
 else:
   print("Debe seleccionar una opcion valida!!")