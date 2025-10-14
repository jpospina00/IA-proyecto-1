import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from matplotlib.patches import Rectangle
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.animation import FuncAnimation

# Definir colores
colors = {
    'empty': 'white',
    'ant': 'orange',
    'goal': 'green',
    'poison': 'red'
}

def load_and_resize(path, size=(64,64)):
    img = Image.open(path).convert("RGBA")
    img = img.resize(size, Image.LANCZOS)
    return np.array(img)

def run_gui(grid_size, ant_start, mushroom_pos, poisons, path):
    rows, cols = grid_size
    fig, ax = plt.subplots(figsize=(6, 6))

    for i in range(rows):
        for j in range(cols):
            cell_color = colors['empty']

            # Hormiga inicial
            if (i, j) == ant_start:
                cell_color = colors['ant']
            # Hongo
            elif (i, j) == mushroom_pos:
                cell_color = colors['goal']
            # Venenos
            elif (i, j) in poisons:
                cell_color = colors['poison']

            rect = Rectangle((j, rows-1-i), 1, 1,
                             linewidth=1, edgecolor='black', facecolor=cell_color)
            ax.add_patch(rect)

    ant_img = load_and_resize("src/assets/ant.png", size=(300,300))
    mushroom_img = load_and_resize("src/assets/mushroom.png", size=(300,300))
    poison_img = load_and_resize("src/assets/poison.png", size=(300,300))

    def place_image(image, x, y, zoom=0.08):
        im = OffsetImage(image, zoom=zoom)
        ab = AnnotationBbox(im, (x+0.5, y+0.5), frameon=False)
        ax.add_artist(ab)
        return ab

    # Hongo
    place_image(mushroom_img, mushroom_pos[1], rows-1-mushroom_pos[0], zoom=0.08)

    # Venenos
    for (r, c) in poisons:
        place_image(poison_img, c, rows-1-r, zoom=0.08)

    # Hormiga (animada)
    ant_artist = place_image(ant_img, ant_start[1], rows-1-ant_start[0], zoom=0.08)

    # --- Animación de la hormiga ---
    def update(frame):
        (row, col) = path[frame]
        ant_artist.xybox = (col+0.5, rows-1-row+0.5)
        return [ant_artist]

    ani = FuncAnimation(fig, update, frames=len(path), interval=700, blit=False, repeat=False)

    # --- Configuración del tablero ---
    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)
    ax.set_aspect('equal')
    plt.title("Problema de Búsqueda: Hormiga vs Venenos")
    plt.show()
