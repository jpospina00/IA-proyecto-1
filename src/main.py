import tkinter as tk
from  models.grid import Grid
from models.ant import Ant
from models.items import Mushroom, Poison
from gui.main_window import run_gui
from algortithms.beam_search import beam_search
from algortithms.dynamic_weighting import dynamic_weighted_a_star

ROWS, COLS = 5, 5

def setup_world():
    grid = Grid(ROWS, COLS)

    ant = Ant(0, 0)
    grid.set_cell(0, 0, 1)

    mushroom = Mushroom(4, 4)
    grid.set_cell(4, 4, 2)

    poisons = [Poison(1, 3), Poison(2, 2), Poison(3, 1)]
    for poison in poisons:
        grid.set_cell(poison.row, poison.col, 3)

    return grid, ant, mushroom, poisons

def run_beam_search():
    grid, ant, mushroom, poisons = setup_world()
    path = beam_search((ROWS, COLS), (ant.row, ant.col), (mushroom.row, mushroom.col), [(p.row, p.col) for p in poisons])
    run_gui((ROWS, COLS), (ant.row, ant.col), (mushroom.row, mushroom.col), [(p.row, p.col) for p in poisons], path)

def run_dynamic_weighted():
    grid, ant, mushroom, poisons = setup_world()
    path = dynamic_weighted_a_star((ROWS, COLS), (ant.row, ant.col), (mushroom.row, mushroom.col), [(p.row, p.col) for p in poisons])
    run_gui((ROWS, COLS), (ant.row, ant.col), (mushroom.row, mushroom.col), [(p.row, p.col) for p in poisons], path)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Seleccionar Algoritmo")

    tk.Label(root, text="¿Qué algoritmo desea ejecutar?", font=("Arial", 14)).pack(pady=10)
    tk.Button(root, text="Beam Search", command=lambda:[root.destroy(), run_beam_search()]).pack(pady=5)
    tk.Button(root, text="Dynamic Weighted A*", command=lambda:[root.destroy(), run_dynamic_weighted()]).pack(pady=5)

    root.mainloop()