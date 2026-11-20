##ejercicio 1
def guardar_tabla():
    try:
        n = int(input("Ingrese un número entre 1 y 10: "))
        arch = open("tabla-%d.txt" % (n), "w")
        for i in range(1, 11):
            arch.write("%d x %d = %d\n" % (n, i, n * i))
        arch.close()
    except IOError:
        print("Error al escribir el archivo")


guardar_tabla()


##ejercicio 2
def mostrar_tabla():
    try:
        n = int(input("Ingrese un número entre 1 y 10: "))
        arch = open("tabla-%d.txt" % (n), "r")
        for linea in arch:
            if linea[-1] == "\n":
                linea = linea[:-1]
            print(linea)
        arch.close()
    except IOError:
        print("El archivo no existe")


mostrar_tabla()


##ejercicio 3
def mostrar_linea():
    try:
        n = int(input("Ingrese un número n entre 1 y 10: "))
        m = int(input("Ingrese un número m entre 1 y 10: "))
        arch = open("tabla-%d.txt" % (n), "r")
        contador = 0
        for linea in arch:
            contador += 1
            if contador == m:
                if linea[-1] == "\n":
                    linea = linea[:-1]
                print(linea)
        arch.close()
    except IOError:
        print("El archivo no existe")


mostrar_linea()
```[cite: 8, 9, 10, 11, 12, 14, 17, 18, 20, 24, 25, 28, 32]