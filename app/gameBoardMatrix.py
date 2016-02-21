def GameBoard(game, mode, turn, height, width, snakes, food, walls, gold):
  gameBoard = [['E' for x in range(height)] for x in range(width)] 
  #gameBoard[1][4] = 'E';
  for i in range(len(snakes)):
    for j in range(len(snakes[i].coords)):
      x = snakes[i].coords[j][0]
      y = snakes[i].coords[j][1]
      if (snakes[i].id == '2daa46ee-4880-4285-8572-eeaf52dba551'):
      	if (j == 0):
          gameBoard[x][y] = 'H'
      	else:
          gameBoard[x][y] = 'I'
      else:
        gameBoard[x][y] = 'S'
  for i in range(len(food)):
    x = food[i][0]
    y = food[i][1]
    gameBoard[x][y] = 'F'
  for i in range(len(walls)):
    x = walls[i][0]
    y = walls[i][1]
    gameBoard[x][y] = 'W'
  for i in range(len(gold)):
    x = gold[i][0]
    y = gold[i][1]
    gameBoard[x][y] = 'G'
  return gameBoard

