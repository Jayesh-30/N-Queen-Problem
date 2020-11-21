from State import State
from Board import Board

def init():
  # Number of Queens
  n = 10
  # Initialize State
  state = State(n)
  # Generating Empty State
  state.generateEmptyState()
  # Randomized State
  state.generateRandomizeState()

  # Initialize Board
  board = Board(n)
  # Generating Empty Board
  board.generateEmptyBoard();
  # Generate Queen Board
  board.generateQueenBoard(state.state)
  # Generate Total Conflicts
  board.generateTotalConflicts();

  # Min Conflicts Hill Climbing
  max = 0;
  while (board.totalConflicts != 0 and max <= 10):
    for indexA,row in enumerate(board.board):
      board.placeNoQueen(indexA, state.state[indexA])
      state.state[indexA] = -1
      values = []
      for indexB in range(n):
        values.append(board.generateConflicts(indexA,indexB))
      minConflictIndex = values.index(min(*values))
      board.placeQueen(indexA,minConflictIndex)
      state.state[indexA] = minConflictIndex
    board.generateTotalConflicts();
    print(board.totalConflicts)
    print(board.board)
    max+=1

init()
