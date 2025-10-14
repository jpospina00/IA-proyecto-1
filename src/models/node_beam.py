from utils.heuristics import manhattan_distance

class Node:
    def __init__(self, state, parent=None, heuristic=0):
        self.state = state
        self.parent = parent
        self.heuristic = heuristic
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def get_path(self):
        node = self
        path = []
        while node:
            path.append(node.state)
            node = node.parent
        return list(reversed(path))
