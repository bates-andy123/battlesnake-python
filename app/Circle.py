class lazyMove(gameData):
  head = getHead(gameData)[0]
  x_head = head[0]
  y_head = head[1]
  def __init__(self):
    self.loopState = 5
    self.lastDirection = "north"
    self.ldID = 0
  def move(self):
    if loopState > 5:
      if self.ldID == 0:
        if gameData['gameBoard'][x_head][y_head-1] == "E" || gameData['gameBoard'][x_head][y_head-1] == "G" ||gameData['gameBoard'][x_head][y_head-1] == "F":
          return lastDirection
      if self.ldID == 1:
        if gameData['gameBoard'][x_head+1][y_head] == "E" || gameData['gameBoard'][x_head+1][y_head] == "G" ||gameData['gameBoard'][x_head+1][y_head] == "F":
          return lastDirection
      if self.ldID == 2:
        if gameData['gameBoard'][x_head][y_head+1] == "E" || gameData['gameBoard'][x_head][y_head+1] == "G" ||gameData['gameBoard'][x_head][y_head+1] == "F":
          return lastDirection
      if self.ldID == 3:
        if gameData['gameBoard'][x_head-1][y_head] == "E" || gameData['gameBoard'][x_head-1][y_head] == "G" ||gameData['gameBoard'][x_head-1][y_head] == "F":
          return lastDirection
    if self.ldID != 0:
      if gameData['gameBoard'][x_head][y_head-1] == "E" || gameData['gameBoard'][x_head][y_head-1] == "G" ||gameData['gameBoard'][x_head][y_head-1] == "F":
          self.lastDirection = "north"
          self.ldID = 0
          loopState =5
          return lastDirection
    if self.ldID != 1:
      if gameData['gameBoard'][x_head+1][y_head] == "E" || gameData['gameBoard'][x_head+1][y_head] == "G" ||gameData['gameBoard'][x_head+1][y_head] == "F":
          self.lastDirection = "east"
          self.ldID = 1
          loopState =5
          return lastDirection
    if self.ldID != 2:
        if gameData['gameBoard'][x_head][y_head+1] == "E" || gameData['gameBoard'][x_head][y_head+1] == "G" ||gameData['gameBoard'][x_head][y_head+1] == "F":
          self.lastDirection = "south"
          self.ldID = 2
          loopState =5
          return lastDirection
    if self.ldID != 3:
        if gameData['gameBoard'][x_head-1][y_head] == "E" || gameData['gameBoard'][x_head-1][y_head] == "G" ||gameData['gameBoard'][x_head-1][y_head] == "F":
          self.lastDirection = "east"
          self.ldID = 3
          loopState =5
          return lastDirection
    if self.ldID == 0:
      if gameData['gameBoard'][x_head][y_head-1] == "E" || gameData['gameBoard'][x_head][y_head-1] == "G" ||gameData['gameBoard'][x_head][y_head-1] == "F":
          self.lastDirection = "north"
          self.ldID = 0
          loopState =5
          return lastDirection
    if self.ldID == 1:
      if gameData['gameBoard'][x_head+1][y_head] == "E" || gameData['gameBoard'][x_head+1][y_head] == "G" ||gameData['gameBoard'][x_head+1][y_head] == "F":
          self.lastDirection = "east"
          self.ldID = 1
          loopState =5
          return lastDirection
    if self.ldID == 2:
        if gameData['gameBoard'][x_head][y_head+1] == "E" || gameData['gameBoard'][x_head][y_head+1] == "G" ||gameData['gameBoard'][x_head][y_head+1] == "F":
          self.lastDirection = "south"
          self.ldID = 2
          loopState =5
          return lastDirection
    if self.ldID == 3:
        if gameData['gameBoard'][x_head-1][y_head] == "E" || gameData['gameBoard'][x_head-1][y_head] == "G" ||gameData['gameBoard'][x_head-1][y_head] == "F":
          self.lastDirection = "east"
          self.ldID = 3
          loopState =5
          return lastDirection



def getHead(gameData):	
  snakes = gameData ["snakes"]
  for i in range(len(snakes)):
    if snakes[i]["id"] == "2daa46ee-4880-4285-8572-eeaf52dba551":
      return snakes[i]["coords"][0],snakes[i]["coords"][1]