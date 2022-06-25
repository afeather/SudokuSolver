
class Puzzle(object):

  @staticmethod
  def fromString(text):
    
    def tryParse(c):
      try:
        return int(c)
      except ValueError:
        return 0
    
    return Puzzle([[tryParse(char) for char in line] for line in text.splitlines()])
    
  def __init__(self, cells):
    self.cells     = cells
    self.size      = len(cells)
    self.blockSize = int(self.size ** 0.5)
  
  def __repr__(self):
    return "\n".join("".join(str(cell) for cell in row) for row in self.rows)
    
  @property
  def rows(self):
    return self.cells
  
  def getRow(self, row):
    return self.cells[row]
  
  @property
  def cols(self):
    return [self.getCol(i) for i in range(self.size)]
  
  def getCol(self, col):
    return [row[col] for row in self.rows]
  
  @property
  def blocks(self):
    return [self.getBlock(i, j) for i in range(0, self.size, self.blockSize)
                                for j in range(0, self.size, self.blockSize)]
  
  def getBlock(self, row, col):
    rowStart, colStart = row - (row % self.blockSize), col - (col % self.blockSize)
    
    return [self.cells[i][j] for i in range(rowStart, rowStart + self.blockSize) 
                             for j in range(colStart, colStart + self.blockSize)]
  
  def getValid(self, row, col):
    return [v for v in range(1, 10) if v not in set(self.getRow(row) + self.getCol(col) + self.getBlock(row, col))]
  
  def isSolved(self):
    return all(cell for row in self.cells for cell in row)
    
