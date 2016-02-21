class food40(object):
  head = 0
  data = 0
  #coords of food positions
  foodPos = 0
  #number of moves to get to each food item
  moves = 0
  #position of each enemy snake
  enSnakes = 0
  #number of moves for each enemy snake to each food item
  enSnakesMoves = 0
  #an array defining if own snake is the closest of all snakes to each food item
  closest = 0

  def _init_(self, data, gameBoard):
    move = 0
    self.data = data
    self.head = self.getHead()
    self.foodPos = self.getFood()
    self.moves = self.getMoves()
    self.enSnakes = self.getEnemySnakes()
    self.enSnakeMoves = self.getEnSnakeMoves()
    val = self.evalClosest()
    if val < 0:
      return
    return moveTo(val)
 #gets position of own snake head
  def getHead(self):
    snakes= self.data ["snakes"]
    for i in snakes:
      if snakes[i]["id"]=="2daa46ee-4880-4285-8572-eeaf52dba551":
        self.head=snakes[i]["coords"][0]
  def getFood(self):
    board=self.gameBoard
    item = 0
    for i in board:
      for j in board[i]:
        if board[i][j] == "F":
          foodPos[item][0] = i
          foodPos[item][1] = j
          item += 1
  #moves for own snake to get to each food item
  def getMoves(self):
    for i in foodPos:
      moves[i]=abs(head[0]-foodPos[i][0])+abs(head[1]-foodPos[i][1])
  #position of each other snake
  def getEnemySnakes(self):
    board = self.gameBoard
    item = 0
    for i in board:
      for j in board[i]:
        if board[i][j] == "S":
          enSnakes[item][0] = i
          enSnakes[item][1] = j
          item += 1
  # distance of each other snake to each food item
  def getEnSnakeMoves(self):
    for i in foodPos:
      for j in enSnakes:
        enSnakeMoves[i][j]=abs(enSnakes[j][0] - foodPos[i][0])+abs(enSnakes[j][1] - foodPos[i][1])
  # finds if own snake is the closest to each food item
  def evalClosest(self):
  	#this will be the **INDEX** of the smallest move, used to find the food item to go to
    smallestMove = 1000
    for i in foodPos:
      for j in enSnakeMoves[i][j]:
        if moves[i] < enSnakesMoves[i][j]:
          closest[i] = y
        else:
          closest[i] = n
      for x in closest:
        if closest[x] == y:
          if moves[x] < smallestMove:
            smallestMove = moves[x]
    if smallestMove == 1000:
      return -1
    else:
      return smallestMove

  def moveTo(self, item):
    food_x = foodPos[item][0]
    food_y = foodPos[item][1]
    board = self.gameBoard
    if board[head[0]+1][head[1]] != "W" or "S":
      if (head[0]+1) <= food_x:
        return "east"
    if board[head[0]-1][head[1]] != "W" or "S":
      if (head[0]-1) >= food_x:
        return "west"
    if board[head[0]][head[1]+1] != "W" or "S":
      if (head[1]+1) <= food_y:
        return "south"
    if board[head[0]][head[1]-1] != "W" or "S":
      if (head[1]-1) >= food_y:
        return "north"
    else:
      return "north"