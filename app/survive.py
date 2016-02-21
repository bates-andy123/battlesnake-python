class survive(object):
  data = 0
  head = 0
  prev = 0
  height = 0
  width = 0

  def __init__(self, data, head):
    self.data = data
    self.head,self.prev = self.getHead()
    self.height,self.width = self.data.height,self.data.width

  def survive(self,board):
    moves = ["north","east","west","south"] 		
    headPos,prev = self.head,self.prev
    noWin = 0

    #Eliminate Tail case
    if headPos[0] - prev[0] < 0:
      moves.remove("south")
      noWin = "north"
    if headPos[0] - prev[0] > 0:
      moves.remove("north")
      noWin = "south"
    if headPos[0] - prev[0] == 0:
      if headPos[1] - prev[1] > 0:
        moves.remove("west")
        noWin = "east"
      else:
        moves.remove("east")
        noWin = "west"

    #Eliminate wall case
    if headPos[0] == 0:
    	move.remove("west")
    elif headPos[0] == width:
    	move.remove("east")
    if headPos[1] == 0:
    	move.remove("north")
    elif headPos[1] == height:
    	move.remove("south")

    for i in move:
      if i == "north":
        if board[head[0]-1][head[1]] == "e" or board[head[0]-1][head[1]] == "f" or board[head[0]-1][head[1]] == "g":
          pass
        else:
          move.remove("north")
      if i == "east":
        if board[head[0]][head[1]+1] == "e" or board[head[0]][head[1]+1] == "f" or board[head[0]][head[1]+1] =="g":
          pass
        else:
          move.remove("east")
      if i == "south":
        if board[head[0]+1][head[1]] == "e" or board[head[0]+1][head[1]] == "f" or board[head[0]+1][head[1]] == "g":
          pass
        else:
          move.remove("south")
      if i == "west":
        if board[head[0]][head[1]-1] == "e" or board[head[0]][head[1]-1] == "f" or board[head[0]][head[1]-1] == "g":
          pass
        else:
          move.remove("west")

    #No Good moves
    if not move:
      return noWin

    else:
      return move[0]


  def getHead(self):	
    snakes = self.data ["snakes"]
    for i in snakes:
      if snakes[i]["id"] == "2daa46ee-4880-4285-8572-eeaf52dba551":
        return snakes[i]["coords"][0],snakes[i]["coords"][1]

