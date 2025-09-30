import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
import matplotlib.patches as mpatches
# Esto es un ejemplo base de como representar la matriz grafica del problema de busqueda
# Se puede hacer con animation que hace parte de matplotlib (Consultar con el docente las preguntas en base a esta solución)
# Preguntas:
"""
1. ¿Cómo puedo representar una matriz gráfica en Python?
    bibliotecas Matplotlib para crear una representación visual de una matriz gráfica.
2. ¿Cómo puedo representar diferentes elementos en la matriz gráfica?
    usar diferentes colores o símbolos para representar distintos elementos en la matriz gráfica.
3. ¿Cómo puedo hacer que las posiciones de los elementos sean aleatorias? 
    Randomizar las posiciones de los elementos en la matriz gráfica.
4. ¿Se debe simular el movimiento de la hormiga?
    Se se debe simular entonces la librería Animation de Matplotlib puede ser útil. (veremos)
5. ¿Se debe construir el arbol de búsqueda?
    Si esto es verdadero entonces se debe usar alguna librería para representar árboles (veremos)

"""
# Crear la figura y el eje
fig, ax = plt.subplots(figsize=(8, 8))

# Definir el grid (5x5)
# Estas definición debe cambiar para que la matriz sea de tamaño n x n
grid_size = 5

# Definir colores
colors = {
    'empty': 'white',
    'ant': 'orange',
    'goal': 'green', 
    'poison': 'red'
}

# Crear el grid base
for i in range(grid_size):
    for j in range(grid_size):
        rect = Rectangle((j, grid_size-1-i), 1, 1, 
                        linewidth=2, edgecolor='black', 
                        facecolor='white')
        ax.add_patch(rect)

# Agregar elementos específicos
# Hormiga (inicio)
# La hormiga empieza en la esquina superior izquierda (este seria el ejemplo base del problema de busqueda)
# La hormiga no debe estar en la misma posicion que la meta (goal), ni en la misma posicion que los venenos (obstaculos)
# pero puede estar en cualquier posicion, solo hay que cambiar las coordenadas
ant_rect = Rectangle((0, 4), 1, 1, facecolor=colors['ant'])
ax.add_patch(ant_rect)

# Hay que especificar la meta (goal), pero debe esta en un randon para corresponder al probelema de busqueda
# La meta no puede estar en la misma posicion que la hormiga, ni en la misma posicion que los venenos
# Meta (goal)
goal_rect = Rectangle((4, 0), 1, 1, facecolor=colors['goal'])
ax.add_patch(goal_rect)

# Venenos (obstáculos)
# Los venenos pueden estar en cualquier posicion, solo hay que cambiar las coordenadas
# En este caso, los venenos estan en posiciones fijas para el ejemplo
# Debemos hacer un randon para que los venenos esten en posiciones aleatorias
# pero asegurandonos que no esten en la misma posicion que la hormiga o la meta
poison_positions = [(1,3), (0,2), (2,2), (1,1), (2,0)]
for pos in poison_positions:
    poison_rect = Rectangle(pos, 1, 1, facecolor=colors['poison'])
    ax.add_patch(poison_rect)

ax.set_xlim(0, grid_size)
ax.set_ylim(0, grid_size)
ax.set_aspect('equal')
ax.set_title('Problema de Búsqueda: Hormiga vs Venenos')


legend_elements = [
    mpatches.Patch(color=colors['ant'], label='Inicio (Hormiga)'),
    mpatches.Patch(color=colors['goal'], label='Meta (Hoja)'),
    mpatches.Patch(color=colors['poison'], label='Obstáculo (Veneno)')
]
ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1.3, 1))

plt.show()