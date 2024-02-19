# CI5651 - Diseño de Algoritmos I. Trimestre Enero - Marzo 2024
# Roberto Gamboa, 16-10394
# Tarea 4. Ejercicio 3

# Retorna true si se ha inicializado la posicion i del arreglo T
# Toma tiempo Θ(1) ya que solo se realizan tres comparaciones
def verificar(a,b,contador,i):
    if 1 <= b[i] and b[i] <= contador:
        if a[b[i]] == i:
            return True
    return False

# Crear a y b toma tiempo Θ(n), pero a la larga toma orden amortizado Θ(1) 
# por todas las otras operaciones que se realizan
n = int(input("Ingrese el valor de n: "))
a = [-1] * n
b = [-1] * n
contador = 0

while True:

    accion = input("\nIngrese la accion a realizar: ").split(' ')

    if accion[0] == "ASIGNAR":
        # Se verifica si la casilla ya se encuentra inicializada
        # o si la casilla a inicializar se encuentra fuera del rango
        if len(accion) == 3:
            pos = int(accion[1])
            val = int(accion[2])

            if pos > n-1:
                print("Posicion no valida en el arreglo")
            else:
                if not verificar(a,b,contador,pos):
                    a[contador] = pos
                    b[pos] = contador
                    contador += 1
                    print(f"Se ha incializado la posicion {pos}")
                else:
                    print(f"La posicion {pos} ya ha sido inicializada")
        else:
            print("Error con los argumentos de la accion ASIGNAR")
            print("La accion ASIGNAR toma dos argumentos: la posicion y el valor a asignar")
            print("Ejemplo: ASIGNAR 3 5")
    elif accion[0] == "CONSULTAR":
        if len(accion) == 2:
            pos = int(accion[1])
            if pos > n-1:
                print("Posicion no valida en el arreglo")
            else:
                if verificar(a,b,contador,pos):
                    print(f"La posicion {pos} ha sido inicializada")
                else:
                    print(f"La posicion {pos} no ha sido inicializada")
        else:
            print("Error con los argumentos de la accion CONSULTAR")
            print("La accion CONSULTAR toma un argumento: la posicion a consultar")
            print("Ejemplo: CONSULTAR 3")
    elif accion[0] == "LIMPIAR":
        #Se reinician los arreglos y el contador
        a = [-1] * n
        b = [-1] * n
        contador = 0
        print("Se ha limpiado la tabla")
    elif accion[0] == "SALIR":
        exit()
    pass