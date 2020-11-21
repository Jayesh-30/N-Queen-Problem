import random
 
def generateEmptyBoard():
 board = [None]*n
 for x in range(n): board[x] = [0]*n
 return board
 
n = 40
board = generateEmptyBoard()
 
def randomRestart():
 for i in range(n):
   for j in range(n):
     board[i][j] = 0
 for row in board: row[random.randint(0,n-1)] = 1
 
 
def conflicts(x,y):
 attacking = 0
 def inc(value): return value+1;
 def dec(value): return value-1;
 
 # Up
 i,j = x,y
 while (dec(i) >= 0):
   i-=1
   attacking += board[i][j]
 # Down
 i,j= x,y
 while (inc(i) < n):
   i+=1
   attacking += board[i][j]
 
 # Diagonals
 # Top Left
 i,j = x,y
 while (dec(i) >= 0 and dec(j) >= 0):
   i-=1
   j-=1
   attacking += board[i][j]
 # Top Right
 i,j = x,y
 while (dec(i) >= 0 and inc(j) < n):
   i-=1
   j+=1
   attacking += board[i][j]
 # Bottom Left
 i,j = x,y
 while (inc(i) < n and dec(j) >= 0):
   i+=1
   j-=1
   attacking += board[i][j]
 # Bottom Right
 i,j = x,y
 while (inc(i) < n and inc(j) < n):
   i+=1
   j+=1
   attacking += board[i][j]
 
 return attacking
 
def generateTotalConflicts():
 totalConflicts = 0
 for indexA,row in enumerate(board):
   for indexB in range(n):
     if(row[indexB]): totalConflicts += conflicts(indexA,indexB)
 return totalConflicts/2
 
def hillClimbing():
 totalConflicts = generateTotalConflicts();
 count = 0;
 while (totalConflicts != 0 and count <= 10):
   for indexA,row in enumerate(board):
     values = []
     for indexB in range(n):
       if(row[indexB]): board[indexA][indexB] = 0
       values.append(conflicts(indexA,indexB))
     minConflictIndex = values.index(min(*values))
     board[indexA][minConflictIndex] = 1
   totalConflicts = generateTotalConflicts()
   count+=1
 
 
def init():
 print('Init')
 boards = []
 allTotalConflicts = []
 restart = 10
 while(restart > 0):
   randomRestart()
   hillClimbing()
   boards.append(board)
   totalConflicts = generateTotalConflicts();
   allTotalConflicts.append(totalConflicts)
   restart-=1
 
 minTotalConflicts = min(*allTotalConflicts);
 result = boards[allTotalConflicts.index(minTotalConflicts)];
 print(minTotalConflicts)
 print(result)
 
init()
