
stock = {
 '8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
 'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
 'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],}



def busqueda_precio():
    while True:
        try:
            precio_min = int(input('Ingrese el precio mínimo: '))
            precio_max = int(input('Ingrese el precio máximo: '))

            if precio_min < 249990:
                print('No hay notebooks en ese rango de precio')
            elif precio_max > 749990:
                print('No hay notebooks en ese rango de precio')
            else:
                modelos_encontrados = []
                for clave, valor in stock.items():
                    precio = valor[0]

                    if precio_min <= precio <= precio_max:
                        if clave in productos:
                            detalles_producto = productos[clave]
                            marca = detalles_producto[0]
                            almacenamiento = detalles_producto[4]
                            modelos_encontrados.append(f'Modelo: {clave} | Marca: {marca} | Almacenamiento: {almacenamiento} | Precio: {precio}')
                        else:
                            modelos_encontrados.append(f'Modelo: {clave} | Precio: {precio} (sin detalles en productos)')

                if modelos_encontrados:
                    print('Los notebooks entre los precios indicados son:')
                    for linea_modelo in modelos_encontrados:
                        print(linea_modelo)
                    break
                else:
                    print('No se encontraron modelos en ese rango de precio')
                    break
        except ValueError:
            print('Debe ingresar valores enteros!!')



def stock_marca():
    modelo = []
    total = 0
    marca = input("ingrese marca a consultar: ")
    for clav, valo in productos.items():
        if marca.lower() == valo[0].lower():
            modelo.append(clav)
    if not modelo:
        print(f"No se encontraron productos de la marca {marca}")
        return
    for modelo_actual in modelo:
        if modelo_actual in stock:
            cantidad, precio = stock[modelo_actual]
            total += cantidad
    print(f"El stock total para la marca {marca} es: {total}")



def mostrar():
    for compu, lista in productos.items():
        print(f'compu: {lista[0]} modelo: {compu} ram: {lista[2]} disco: {lista[4]}')





