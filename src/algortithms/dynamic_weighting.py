# algortithms/dynamic_weighting.py (Versión MODIFICADA)

import heapq
from models.node_dw import NodeDW
from utils.heuristics import manhattan_distance
from utils.neighbors import get_neighbors

# Definición de movimientos: Arriba, Abajo, Izquierda, Derecha
# (dr, dc) = (delta_row, delta_col)
MOVEMENTS = [
    (-1, 0),  # Arriba
    (1, 0),   # Abajo
    (0, -1),  # Izquierda
    (0, 1)    # Derecha
]

# Definición de costos base
COST_BASE = 4.0  # Costo por moverse a una celda vacía
COST_POISON = 1.0 # Costo ALTO por moverse a una celda de veneno (Asumo un costo de 10)


def dynamic_weighted_a_star(grid_size: tuple, start: tuple, goal: tuple, poisons: list, epsilon: float = 1.0):
    """
    Algoritmo A* con peso dinámico.
    Permite el paso por venenos, pero con un costo/penalización.
    
    Args:
        grid_size: (rows, cols)
        start: Posición inicial (row, col)
        goal: Posición de la meta (row, col)
        poisons: Lista de posiciones de veneno [(row, col), ...]
        epsilon: Factor de peso para el término dinámico (ε).
    
    Returns:
        Una lista de tuplas representando el camino (path) o None si no se encuentra.
    """
    rows, cols = grid_size
    N = rows * cols  # Usamos el tamaño total del grid como una aproximación de N

    h_start = manhattan_distance(start, goal)
    start_node = NodeDW(start, g_cost=0, h_cost=h_start)
    
    # Cálculo inicial de f_cost
    start_node.f_cost = start_node.g_cost + start_node.h_cost * (1 + epsilon * (1 - 0/N))

    open_list = [(start_node.f_cost, start_node)]
    closed_list = set()
    g_scores = {start: 0}

    while open_list:
        f_current, current_node = heapq.heappop(open_list)
        current_state = current_node.state
        
        if current_state == goal:
            return current_node.get_path()

        if current_state in closed_list:
            continue
        
        closed_list.add(current_state)

        depth = len(current_node.get_path()) - 1
        
        # Generar sucesores
        for dr, dc in MOVEMENTS:
            new_row, new_col = current_state[0] + dr, current_state[1] + dc
            new_state = (new_row, new_col)

            # 1. Validar límites del grid (esto SÍ debe mantenerse)
            if not (0 <= new_row < rows and 0 <= new_col < cols):
                continue
            
            # 2. CALCULAR COSTO: Si puede pasar por venenos, usamos el costo apropiado
            step_cost = COST_POISON if new_state in poisons else COST_BASE
            new_g_cost = current_node.g_cost + step_cost
            
            # 3. Optimización A*: Si ya encontramos un mejor camino, descartar
            if new_g_cost >= g_scores.get(new_state, float('inf')):
                continue

            # 4. Crear el nuevo nodo y calcular costos
            new_h_cost = manhattan_distance(new_state, goal)
            new_node = NodeDW(new_state, current_node, new_g_cost, new_h_cost)
            
            # 5. Aplicar la fórmula Dynamic Weighted A*
            d_new = depth + 1
            weight_factor = 1.0 + epsilon * (1.0 - d_new / N)
            new_node.f_cost = new_node.g_cost + weight_factor * new_node.h_cost

            # 6. Actualizar g_score y añadir a la cola de prioridad
            g_scores[new_state] = new_g_cost
            heapq.heappush(open_list, (new_node.f_cost, new_node))
            
    return None