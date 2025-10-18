import heapq
from models.node_dw import NodeDW
from utils.heuristics import manhattan_distance
from utils.neighbors import get_neighbors

COST_BASE = 4.0
COST_POISON = 10.0


def dynamic_weighted_a_star(grid_size: tuple, start: tuple, goal: tuple, poisons: list, epsilon: float = 1.0,
                            allow_poison_pass: bool = False):
    print("#" * 40)
    print("=== Inicia el Algoritmo Dynamic Weighted A* ===")
    print(f"Inicio:{start}")
    print(f"Meta: {goal}")
    print(f"Venenos: {len(poisons)}")
    print(f"Epsilon (ε): {epsilon}")
    print("#" * 40)

    rows, cols = grid_size
    h_initial = manhattan_distance(start, goal)
    N = max(int(h_initial * 1.3), 10)

    print(f"   • Heurística inicial h(start): {h_initial}")
    print(f"   • N estimado: {N}")
    print(f"   • Peso inicial w(0): {1.0 + epsilon * (1.0 - 0 / N):.1f}")

    poison_set = set(poisons) if poisons else set()

    h_start = manhattan_distance(start, goal)
    start_node = NodeDW(start, g_cost=0, h_cost=h_start)
    weight_initial = 1.0 + epsilon * (1.0 - 0 / N)

    # Cálculo inicial de f_cost
    start_node.f_cost = start_node.g_cost + weight_initial * start_node.h_cost

    open_list = [(start_node.f_cost, start_node)]
    closed_list = set()
    g_scores = {start: 0}
    iteration = 0

    while open_list:
        iteration += 1
        f_current, current_node = heapq.heappop(open_list)
        current_state = current_node.state
        print(f"==== Iteracion: {iteration} ====")
        if current_state == goal:
            print("¡META ALCANZADA!")
            print(f"Estadísticas finales:")
            print(f"   • Iteraciones: {iteration}")
            print(f"   • Nodos expandidos: {len(closed_list)}")
            print(f"   • Longitud del camino: {current_node.get_path()}")
            print(f"   • Costo total: {current_node.g_cost:.1f}")
            return current_node.get_path()

        if current_state in closed_list:
            continue

        closed_list.add(current_state)
        depth = len(current_node.get_path()) - 1
        depth_ratio = min(1.0, max(0.0, depth / N))
        current_weight = 1.0 + epsilon * (1.0 - depth_ratio)

        print(f" g(n) = {current_node.g_cost:6.2f} - h(n) = {current_node.h_cost:6.2f} - f(n) = {f_current:6.2f}")
        print(f" depth = {depth:3d} - w(n) = {current_weight:6.2f} - ratio = {depth_ratio:5.2f}")
        print(f" Camino actual: {''.join(str(p) for p in current_node.get_path()[:5])}")
        if len(current_node.get_path()) > 5:
            print(f"... {current_node.get_path()[-1]}")

        if allow_poison_pass:
            r, c = current_state
            candidates = [
                (r - 1, c),
                (r + 1, c),
                (r, c - 1),
                (r, c + 1),
            ]
            neighbors = [
                (nr, nc)
                for (nr, nc) in candidates
                if 0 <= nr < rows and 0 <= nc < cols
            ]
        else:
            neighbors = get_neighbors(current_state, grid_size, poison_set)
        if neighbors:
            print(f" Explorando {len(neighbors)} vecinos:")
        # Generar sucesores
        for idx, new_state in enumerate(neighbors, 1):
            if allow_poison_pass and new_state in poison_set:
                step_cost = COST_POISON
            else:
                step_cost = COST_BASE

            new_g_cost = current_node.g_cost + step_cost
            if new_g_cost >= g_scores.get(new_state, float('inf')):
                print(f"  {idx}. {new_state} Descartado (ya existe mejor camino)")
                continue

            new_h_cost = manhattan_distance(new_state, goal)
            print(f"Nuevo costo (h): {new_h_cost}")
            new_node = NodeDW(new_state, current_node, new_g_cost, new_h_cost)
            new_depth = depth + 1
            depth_ratio = min(1.0, max(0.0, new_depth / N))
            weigth_factor = 1.0 + epsilon * (1.0 - depth_ratio)
            new_node.f_cost = new_node.g_cost + weigth_factor * new_node.h_cost
            g_scores[new_state] = new_g_cost
            heapq.heappush(open_list, (new_node.f_cost, new_node))

    return None
