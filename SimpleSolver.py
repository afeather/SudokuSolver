#!/usr/bin/python

import logging

def solve(p, rStart = 0):

  for row, col in ((r, c) for r in range(rStart, p.size) for c in range(p.size)):
    if p.cells[row][col]: continue
    
    for valid in p.getValid(row, col):
      logging.debug("Trying {} in ({}, {})".format(valid, row, col))
      p.cells[row][col] = valid
      
      if solve(p, row): return p
    
    logging.debug("No solution found, backtracking...")
    p.cells[row][col] = 0
    return False
  
  logging.info("Valid value found for all cells")
  return p

if __name__ == "__main__":

  from Puzzle import Puzzle

  test = """002051009
000008000
600000200
000600003
700035010
005800000
040000070
000300000
006092001"""

  p = Puzzle.fromString(test)
  print(solve(p))
