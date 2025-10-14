def load_world_from_file(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file.readlines() if line.strip() and not line.startswith("#")]

    # Tamaño
    rows, cols = map(int, lines[0].split())

    # Hormiga
    ant_row, ant_col = map(int, lines[1].split())

    # Hongo
    mushroom_row, mushroom_col = map(int, lines[2].split())

    # Venenos
    poisons = [tuple(map(int, line.split())) for line in lines[3:]]

    return (rows, cols), (ant_row, ant_col), (mushroom_row, mushroom_col), poisons
