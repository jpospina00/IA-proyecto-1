def load_world_from_file(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file.readlines() if line.strip() and not line.startswith("#")]

    # Tamaño
    rows, cols = map(int, lines[0].split())

    # Beta
    beta = int(lines[1])
    # Hormiga
    ant_row, ant_col = map(int, lines[2].split())

    # Hongo
    mushroom_row, mushroom_col = map(int, lines[3].split())

    # Venenos
    poisons = [tuple(map(int, line.split())) for line in lines[4:]]

    return (rows, cols), beta, (ant_row, ant_col), (mushroom_row, mushroom_col), poisons
