from utils.heuristics import manhattan_distance

def dynamic_weighted_a_star(grid_size, start, goal, poisons, epsilon=2.0, N_max=None):
    """
    Dynamic Weighted A* que devuelve un camino como lista de posiciones [(fila,col)].
    Por ahora es solo un ejemplo con un camino fijo.
    f(n) = g(n) + h(n) + ε * (1 - d(n)/N) * h(n)
    donde:
    - g(n): costo real desde inicio hasta n
    - h(n): heurística (costo estimado desde n hasta meta)
    - ε: parámetro de peso inicial (típicamente entre 1 y 5)
    - d(n): profundidad del nodo n en el árbol de búsqueda
    - N: profundidad máxima estimada o anticipada
    """

    man_dis = manhattan_distance(start, goal)
    N_max = max(int(man_dis * 1.3), 10)

    poisons_set = set(poisons) if poisons else set()
    epsilon_set = set(epsilon) if epsilon else set()
    
    open_list = []
    closed_set: Set[Tuple[int, int]] = set()
    g_costs: Dict[Tuple[int, int], float] = {start: 0.0}
    depths: Dict[Tuple[int, int], int] = {start: 0}
    parents: Dict[Tuple[int, int], Optional[Tuple[int, int]]] = {start: None}

    nodes_expanded = 0
    nodes_generated = 0
    counter = 0

    h_start = manhattan_distance(start, goal)

    if N_max is None:
        depth_ratio_start = 0.0
        weight_start = 1.0 + epsilon * (1.0 - depth_ratio_start)

    else:
        weight_start = 1.0 + epsilon

    f_start = 0 + weight_start * h_start

    heapq.heappush(open_list, (f_start, counter, 0, 0, start))
    counter += 1
    nodes_generated += 1

    while open_list:
        f_current, _, g_current, depth_current, current = heapq.heappop(open_list)

        if current in closed_set:
            continue

        closed_set.add(current)
        nodes_expanded += 1

        if current == goal:
            path = []
            pos = goal
            while pos is not None:
                path.append(pos)
                pos = parents[pos]
            path.reverse()

    #### aqui va el llamado a los stats ###
    