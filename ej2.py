# CI5651 - Diseño de Algoritmos I. Trimestre Enero - Marzo 2024
# Roberto Gamboa, 16-10394
# Tarea 4. Ejercicio 2


def contar_subarreglos_buenos(A):
    n = len(A)

    # Array para guardar la cantidad de subarreglos buenos que terminan en la posición i
    # Tiene tamaño n + 1 para incluir el subarreglo vacío

    # Se utiliza el arreglo dp para almacenar el número de subarreglos buenos que terminan en cada posición i. 
    # De esta manera se evita recalcular el número de subarreglos buenos 
    # que terminan en cada posición en cada iteracion.
    # Se utiliza programacion dinamica de tipo bottom-up para resolver el problema
    # ya que se resuelven los subproblemas más pequeños primero (ver si cada numero es divisible por la cantidad de elementos en el subarreglo)
    # y se utilizan para resolver los subproblemas más grandes (ver si el subarreglo que termina en la posición i es bueno).
    subarreglos_buenos = [0] * (n + 1)
    
    # Inicializamos el primer elemento del array con 1, ya que el subarreglo vacío es bueno
    subarreglos_buenos[0] = 1

    # Recorremos el arreglo A, este ciclo toma tiempo O(n^2) ya que se ejecuta n veces
    # y en cada iteración se ejecuta un ciclo que se ejecuta hasta otras n veces
    for i in range(1, n + 1):
        # Inicializamos j con el valor de i. 
        # se utilizará para verificar si cada elemento anterior a i es divisible 
        # por el número de elementos en el subarreglo hasta ahora.
        j = i

        # Se itera mientras j sea mayor que 0 y el elemento acutal sea divisible 
        # por la cantidad de elementos en el subarreglo
        while j > 0 and A[i - 1] % (i - j + 1) == 0:
            # Se actualiza el valor de dp[i] sumando el valor de dp[j - 1]
            # Esto se debe a que si el subarreglo que termina en la posición i es bueno,
            # entonces los subarreglos que terminan en la posición j - 1 también lo son.
            subarreglos_buenos[i] += subarreglos_buenos[j - 1]
            j -= 1
        # Se resta 1 a la cantidad de subarreglos buenos para no considerar el arreglo vacio
    return sum(subarreglos_buenos) - 1


