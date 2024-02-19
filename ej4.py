# CI5651 - Diseño de Algoritmos I. Trimestre Enero - Marzo 2024
# Roberto Gamboa, 16-10394
# Tarea 4. Ejercicio 4

import sys

"""
Conocemos:
• La cantidad, n, de equipajes que se han caído. También sabes que 1 ≤ n ≤ 24.
• La posición (x, y) de cada equipaje. Además, dadas las dimensiones del aeropuerto,
sabes que |x| ≤ 100 y |y| ≤ 100 y que ambas dimensiones son números enteros.
• El avión está en la posición (0, 0) y es a donde quieres llevar todas las maletas que se han dispersado.
• Transitar entre dos puntos a y b, toma tanto tiempo como el cuadrado de la distancia cartesiana entre ellos.
• Solamente te puedes detener en la posición de una maleta o en la del avión, por temor a que te multen las autoridades del aeropuerto.
• Puedes cargar a lo sumo dos maletas a la vez (una en cada mano) y una vez que tomas
una maleta, solamente puedes soltarla en el avión.
"""

def tiempo_recoger_maletas(n, pos_maletas):
  # Inicializar la matriz distancias, que guarda las distancias desde el avion a cada maleta con infinito. 
  # Para representar que inicialmente no hay un tiempo conocido para recoger las maletas. 
  # La matriz tiene dimensiones n × 2^n por lo que la inicializacion toma tiempo O(n × 2^n)
  # n es el número de maletas, mientras que 2^n representa todos los posibles subconjuntos de maletas.
  distancias = [ [sys.maxsize - 1] * (2**n) for i in range(n)]
  
  # Función para calcular el cuadrado de la distancia cartesiana entre dos puntos
  def dist_cart(x, y):
    return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2
  
  # Se calcula la distancia desde el avion hasta cada maleta y se almacena en la matriz distancias
  for i in range(n):
    distancias[i][2**i] = dist_cart((0, 0), pos_maletas[i]) * 2
  
  # Recorremos todas las maneras de recoger las maletas. Tiempo: O(n × 2^n)
  # Se va guardando la distancia mínima para recoger las maletas en la matriz distancias.
  # De esta manera se aplica la programación dinámica para resolver el problema.
  for maletas in range(1, 2**n):
    # Recorremos todas las maletas. Tiempo: O(n)
    for i in range(n):
      # Se verifica si la maleta i está en el subconjunto de maletas.
      # Para ello se realiza un AND binario entre el subconjunto de maletas y 2^i.
      # Solo se obtiene un resultado distinto de cero si la maleta i está en el subconjunto de maletas.
      if maletas & (2**i):
        for j in range(n):
          # Se verifica si la maleta j está en el subconjunto de  maletas
          if maletas & (2**j):
            # Se actualiza la matriz con la distancia mínima para recoger las maletas.
            # Se utiliza la función min para obtener la distancia mínima entre recoger
            # la primera y la segunda maleta
            # Se realiza una operacion XOR binaria entre el subconjunto de maletas y 2^i
            # con el fin de obtener el subconjunto de maletas sin la maleta i.
            distancias[i][maletas] = min(distancias[i][maletas], 
                                          distancias[j][maletas ^ (2**i)] + dist_cart(pos_maletas[i], pos_maletas[j]))
  
  # Se busca el tiempo minimo entre recoger todas las maletas y llevarlas al avion. Tiempo: O(n)
  # Como ya se recorrieron todas las maneras de recoger las maletas, se busca el tiempo mínimo
  # y se considera tambien el tiempo que toma llevarlas al avion.
  min_time = min(distancias[i][(2**n) - 1] + dist_cart((0, 0), pos_maletas[i]) for i in range(n))
  
  return min_time

