def get_neighbors(state, grid_size, poisons):
    rows, cols = grid_size
    r, c = state
    candidates = [
        (r - 1, c),  # arriba
        (r + 1, c),  # abajo
        (r, c - 1),  # izquierda
        (r, c + 1),  # derecha
    ]

    valid = [
        (nr, nc)
        for (nr, nc) in candidates
        if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in poisons
    ]
    return valid
