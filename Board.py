class Board: 
  def __init__(self,n):
    self.n = n;
    self.noqueen = 0
    self.queen = 1
  
  def generateEmptyBoard(self):
    self.board = [self.noqueen]*self.n
    for index in range(self.n):
      self.board[index] = [self.noqueen]*self.n
  
  def placeQueen(self,indexA,indexB):
    self.board[indexA][indexB] = self.queen

  def placeNoQueen(self,indexA,indexB):
    self.board[indexA][indexB] = self.noqueen

  def isQueen(self,indexA,indexB):
    return self.board[indexA][indexB] == self.queen

  def generateQueenBoard(self,state):
    for [indexA,indexB] in enumerate(state):
      self.placeQueen(indexA,indexB)

  def generateConflicts(self, indexA,indexB):
    self.conflicts = 0
    def inc(value): return value+1
    def dec(value): return value-1
    # Up
    i,j = indexA,indexB
    while (dec(i) >= 0):
      i-=1
      self.conflicts += self.board[i][j]
    # Down
    i,j= indexA,indexB
    while (inc(i) < self.n):
      i+=1
      self.conflicts += self.board[i][j]
    
    # Diagonals
    # Top Left
    i,j = indexA,indexB
    while (dec(i) >= 0 and dec(j) >= 0):
      i-=1
      j-=1
      self.conflicts += self.board[i][j]
    # Top Right
    i,j = indexA,indexB
    while (dec(i) >= 0 and inc(j) < self.n):
      i-=1
      j+=1
      self.conflicts += self.board[i][j]
    # Bottom Left
    i,j = indexA,indexB
    while (inc(i) < self.n and dec(j) >= 0):
      i+=1
      j-=1
      self.conflicts += self.board[i][j]
    # Bottom Right
    i,j = indexA,indexB
    while (inc(i) < self.n and inc(j) < self.n):
      i+=1
      j+=1
      self.conflicts += self.board[i][j]
    return self.conflicts

  def generateTotalConflicts(self):
    self.totalConflicts = 0
    for indexA in range(self.n):
      for indexB in range(self.n):
        if(self.isQueen(indexA,indexB)): self.totalConflicts += self.generateConflicts(indexA,indexB)
    self.totalConflicts = self.totalConflicts/2
