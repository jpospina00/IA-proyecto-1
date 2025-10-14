from heapq import nsmallest
from models.node_beam import Node
from utils.heuristics import manhattan_distance
from utils.neighbors import get_neighbors

def get_heuristic(node):
    return node.heuristic

def beam_search(grid_size, start, goal, poisons, beam_width=2):
    print("=== INICIO DEL BEAM SEARCH ===")
    print(f"Inicio: {start}, Meta: {goal}, Beam width = {beam_width}")
    print("-" * 50)

    root = Node(state=start, parent=None, heuristic=manhattan_distance(start, goal))
    frontier = [root]
    step = 1

    while frontier:
        print(f"\n🔹 Iteración {step}")
        step += 1
        new_frontier = []

        for node in frontier:
            print(f" Explorando nodo {node.state} (h = {node.heuristic})")

            if node.state == goal:
                print(f"\nMeta alcanzada en {node.state}!")
                print("Camino final:", node.get_path())
                return node.get_path()

            children = []
            for neighbor in get_neighbors(node.state, grid_size, poisons):
                h = manhattan_distance(neighbor, goal)
                child = Node(state=neighbor, parent=node, heuristic=h)
                node.add_child(child)
                new_frontier.append(child)
                children.append((neighbor, h))

            if children:
                print(f"   Hijos generados desde {node.state}:")
                for (c, h) in children:
                    print(f"     - {c} (h = {h})")
            else:
                print(f"  {node.state} no tiene hijos válidos (bloqueado o visitado)")
        if new_frontier:
            sorted_frontier = sorted(new_frontier, key=get_heuristic)
            selected = nsmallest(beam_width, new_frontier, key=get_heuristic)

            print("\nNodos candidatos ordenados por heurística:")
            for n in sorted_frontier:
                print(f"   {n.state} (h = {n.heuristic})")

            print(f"Nodos seleccionados para la siguiente iteración:")
            for s in selected:
                print(f"   {s.state} (h = {s.heuristic})")

            frontier = selected
        else:
            print("\nNo hay más nodos por explorar. Fin del algoritmo.")
            return []

        print("-" * 50)

    print("\nNo se encontró camino hacia la meta.")
    return []
