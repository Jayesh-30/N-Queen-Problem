import random

class State: 
  def _init_(self,n):
    self.n = n
    self.value = 0
  # Generate Empty State
  def generateEmptyState(self):
    self.state = [self.value]*self.n

  # Generate Randomize State
  def generateRandomizeState(self):
    for index in range(self.n):
      self.state[index] = random.randint(0,self.n-1)
