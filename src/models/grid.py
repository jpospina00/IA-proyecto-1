class Grid:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        # Representación simple: 0 vacío, 1 hormiga, 2 hongo, 3 veneno
        self.cells = [[0 for _ in range(cols)] for _ in range(rows)]

    def is_valid_position(self, row: int, col: int) -> bool:
        return 0 <= row < self.rows and 0 <= col < self.cols

    def set_cell(self, row: int, col: int, value: int):
        if self.is_valid_position(row, col):
            self.cells[row][col] = value

    def get_cell(self, row: int, col: int) -> int:
        if self.is_valid_position(row, col):
            return self.cells[row][col]
        return -1
