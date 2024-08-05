from kandinsky import fill_rect, set_pixel
from time import sleep

class Matrice:
  def __init__(self, P: set, length: int = 50, width: int = 50): self.P, self.first_gen, self.length, self.width = P, P, length, width
  def __getitem__(self, ij) -> int: return 1 if (ij) in self.P else 0
  def neighbors(self, cell: tuple) -> set[tuple]: return {(cell[0]-1,cell[1]-1),(cell[0]-1,cell[1]),(cell[0]-1,cell[1]+1),(cell[0],cell[1]-1),(cell[0],cell[1]+1),(cell[0]+1,cell[1]-1),(cell[0]+1,cell[1]),(cell[0]+1,cell[1]+1)}
  def count_neighbors(self, cell: tuple) -> int: return len([C for C in self.neighbors(cell) if self[C] == 1])
  def restart(self): self.P = self.first_gen.copy()
  def is_in(self, position: tuple[int, int], cell: tuple[int, int], taille_cell: int, decal: int) -> bool: return position[0]+cell[0]*(taille_cell+decal) < position[0]+((taille_cell+decal)*self.length) and position[0]+cell[0]*(taille_cell+decal) > position[0]-1 and position[1]+cell[1]*(taille_cell+decal) < position[1]+((taille_cell+decal)*self.width) and position[1]+cell[1]*(taille_cell+decal) > position[1]-1

  def show(self, position: tuple = (0,0), color: str | tuple = "green", taille_cell: int = 5, decal: int = 0):
#    set_pixel(position[0]-1,position[1]-1,"red") ; set_pixel(position[0]+(taille_cell+decal)*self.length,position[1]+(taille_cell+decal)*self.width,"red")
    for cell in self.P: fill_rect(position[0]+cell[0]*(taille_cell+decal),position[1]+cell[1]*(taille_cell+decal),taille_cell,taille_cell,color) if self.is_in(position,cell,taille_cell,decal) else None

  def update(self):
    new_P = self.P.copy()
    for cell in self.P:
      if not (1 < self.count_neighbors(cell) <= 3): new_P.remove(cell)
      for cell_ in self.neighbors(cell): new_P.add(cell_) if self[cell_] == 0 and self.count_neighbors(cell_) == 3 else None
    self.P = new_P ; del new_P

  def run(self, generation: int | None = None, position: tuple = (0,0), color: str | tuple = "green", taille_cell: int = 5, decal: int = 0, color_back: str | tuple = "1", time: int | float = 0.1):
    self.restart() ; self.g = 0 ; sleep(time)
    while self.g != generation: 
      for cell in self.P: fill_rect(position[0]+cell[0]*(taille_cell+decal),position[1]+cell[1]*(taille_cell+decal),taille_cell,taille_cell,color_back) if self.is_in(position,cell,taille_cell,decal) else None
      self.update() ; self.show(position,color,taille_cell,decal) ; self.g += 1 ; sleep(time)
