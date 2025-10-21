def load_world_from_file(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file.readlines() if line.strip() and not line.startswith("#")]

    # Tamaño
    rows, cols = map(int, lines[0].split())

    # Beta
    beta = int(lines[1])

     # Epsilon
    epsilon = float(lines[2])

    # Paso por Venenos
    poisons_pass = bool(lines[3])
    # Hormiga
    ant_row, ant_col = map(int, lines[4].split())

    # Hongo
    mushroom_row, mushroom_col = map(int, lines[5].split())

    # Venenos
    poisons = [tuple(map(int, line.split())) for line in lines[6:]]



    return (rows, cols), beta, epsilon, (ant_row, ant_col), (mushroom_row, mushroom_col), poisons, poisons_pass
