import gameBoardMatrix

class snake:

    

    def __init__(self, row, id_in):
    	self.coords = [[row,0], [row,1], [row,2]] 
    	self.id = id_in 

if __name__ == '__main__':
    food = [[1, 1], [2, 3]]
    hiss = snake(0, "1")
    hisst = snake(2, "2daa46ee-4880-4285-8572-eeaf52dba551")
    gameBoard = gameBoardMatrix.GameBoard(1,1,1,5,7,[hiss,hisst],food,[[1,2]],[[4,3]])
    print(gameBoard);
