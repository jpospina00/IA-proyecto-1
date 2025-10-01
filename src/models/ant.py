class Ant:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.path = [(row, col)]  # historial de posiciones

    def move_to(self, row: int, col: int):
        self.row = row
        self.col = col
        self.path.append((row, col))
