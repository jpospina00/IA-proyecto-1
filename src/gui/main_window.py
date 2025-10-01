import matplotlib
matplotlib.use("TkAgg")   # 👈 fuerza a usar Tkinter en Windows

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle
from matplotlib.animation import FuncAnimation

colors = {
    'empty': 'white',
    'ant': 'orange',
    'goal': 'green',
    'poison': 'red'
}

def run_gui(grid_size, ant_start, mushroom_pos, poisons, path):
    rows, cols = grid_size
    fig, ax = plt.subplots(figsize=(6, 6))

    # Dibujar grid base
    for i in range(rows):
        for j in range(cols):
            rect = Rectangle((j, rows - 1 - i), 1, 1,
                             linewidth=1, edgecolor='black', facecolor=colors['empty'])
            ax.add_patch(rect)

    # Meta (goal)
    goal_rect = Rectangle((mushroom_pos[1], rows - 1 - mushroom_pos[0]), 1, 1, facecolor=colors['goal'])
    ax.add_patch(goal_rect)

    # Venenos
    for (r, c) in poisons:
        poison_rect = Rectangle((c, rows - 1 - r), 1, 1, facecolor=colors['poison'])
        ax.add_patch(poison_rect)

    # Hormiga inicial
    ant_rect = Rectangle((ant_start[1], rows - 1 - ant_start[0]), 1, 1, facecolor=colors['ant'])
    ax.add_patch(ant_rect)

    # Animación: mover la hormiga por el path
    def update(frame):
        (row, col) = path[frame]
        ant_rect.set_xy((col, rows - 1 - row))
        return [ant_rect]

    # 👇 guardamos en variable global
    ani = FuncAnimation(fig, update, frames=len(path), interval=700, blit=True, repeat=False)

    # Leyenda
    legend_elements = [
        mpatches.Patch(color=colors['ant'], label='Hormiga'),
        mpatches.Patch(color=colors['goal'], label='Hongo Mágico'),
        mpatches.Patch(color=colors['poison'], label='Veneno')
    ]
    ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1.3, 1))

    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)
    ax.set_aspect('equal')
    plt.title("Problema de Búsqueda: Hormiga vs Venenos")

    plt.show()
