# models/node_dw.py

class NodeDW:
    def __init__(self, state: tuple, parent=None, g_cost: float = 0.0, h_cost: float = 0.0):
        self.state = state  # Posición (row, col)
        self.parent = parent
        self.g_cost = g_cost  # Costo real desde el inicio (g(n))
        self.h_cost = h_cost  # Costo heurístico a la meta (h(n))
        self.f_cost = g_cost + h_cost # Costo total (f(n))

    def get_path(self):
        """Reconstruye el camino desde el nodo inicial hasta este nodo."""
        node = self
        path = []
        while node:
            path.append(node.state)
            node = node.parent
        return list(reversed(path))

    # Para usarlo en PriorityQueue (comparación de nodos)
    def __lt__(self, other):
        """Define la comparación para la cola de prioridad, basada en f_cost."""
        return self.f_cost < other.f_cost