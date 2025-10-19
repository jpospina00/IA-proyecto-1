import tkinter as tk
from  models.grid import Grid
from models.ant import Ant
from models.items import Mushroom, Poison
from gui.main_window import run_gui
from algortithms.beam_search import beam_search
from algortithms.dynamic_weighting import dynamic_weighted_a_star
from utils.load_file import load_world_from_file

(grid_size, beta, ant_start, mushroom_pos, poisons_pos) = load_world_from_file("src/assets/data.txt")

def setup_world():
    # Alternativamente, cargar desde archivo:
    print(f"Cargando mundo desde archivo: {grid_size}, {beta}, {ant_start}, {mushroom_pos}, {poisons_pos}")
    grid = Grid(grid_size[0], grid_size[1])

    ant = Ant(ant_start[0], ant_start[1])
    grid.set_cell(ant.row, ant.col, 1)

    mushroom = Mushroom(mushroom_pos[0], mushroom_pos[1])
    grid.set_cell(mushroom.row, mushroom.col, 2)

    poisons = [Poison(p[0], p[1]) for p in poisons_pos]
    for poison in poisons:
        grid.set_cell(poison.row, poison.col, 3)

    return grid, ant, mushroom, poisons

def run_beam_search():
    grid, ant, mushroom, poisons = setup_world()
    path = beam_search((grid_size[0], grid_size[1]), (ant.row, ant.col), (mushroom.row, mushroom.col), [(p.row, p.col) for p in poisons], beam_width=beta)
    run_gui((grid_size[0], grid_size[1]), (ant.row, ant.col), (mushroom.row, mushroom.col), [(p.row, p.col) for p in poisons], path)

def run_dynamic_weighted():
    grid, ant, mushroom, poisons = setup_world()
    path = dynamic_weighted_a_star((grid_size[0], grid_size[1]), (ant.row, ant.col), (mushroom.row, mushroom.col), [(p.row, p.col) for p in poisons])
    run_gui((grid_size[0], grid_size[1]), (ant.row, ant.col), (mushroom.row, mushroom.col), [(p.row, p.col) for p in poisons], path)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Seleccionar Algoritmo")

    tk.Label(root, text="¿Qué algoritmo desea ejecutar?", font=("Arial", 14)).pack(pady=10)
    tk.Button(root, text="Beam Search", command=lambda:[root.destroy(), run_beam_search()]).pack(pady=5)
    tk.Button(root, text="Dynamic Weighted A*", command=lambda:[root.destroy(), run_dynamic_weighted()]).pack(pady=5) 

    root.mainloop()