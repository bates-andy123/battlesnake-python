def food70( gameData):
  foodScanMax = 2
  head = getHead()[0]
  x_head = head[0]
  y_head = head[1]
  if(x_head <foodScanMax):
    x_min = 0
  else:
    x_min = x_head - foodScanMax
  if(y_head <foodScanMax):
    y_min = 0
  else:
    y_min = y_head - foodScanMax
  if(x_head + foodScanMax > gameData.width):
    x_max = gameData.width
  else:
    x_max = x_head + foodScanMax
  if(y_head + foodScanMax > gameData.height):
    y_max = 0
  else:
    y_max = y_head + foodScanMax
  for i in range (x_min, x_max):
    for j in range(y_min, y_max):
      if gameData.gameBoard[i][j] == "F":
          variance = fabs(x_head - i) + fabs(y_head - j)
          if (variance <= foodScanMax):
            if(fabs(x_head - i) >= fabs(y_head - j)):
              if (x_head - i < 0):
                if gameData.gameBoard[x_head-1][y_head] == "E":
                  return "west"
              else:
                if gameData.gameBoard[x_head+1][y_head] == "E":
                  return "east"

            if(fabs(x_head - i) <= fabs(y_head - j)):
              if (x_head - j < 0):
                if gameData.gameBoard[x_head][y_head-1] == "E":
                  return "north"
              else:
                if gameData.gameBoard[x_head][y_head+1] == "E":
                  return "south"
  return


def getHead(self):	
  snakes = self.gameData ["snakes"]
  for i in snakes:
    if snakes[i]["id"] == "2daa46ee-4880-4285-8572-eeaf52dba551":
      return snakes[i]["cords"][0],snakes[i]["cords"][1]
