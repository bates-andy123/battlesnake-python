import bottle
import json
import food

print "Script start"

class decide(object):
	def __init__(self):
		print "Class was created successfully, so now echoing hello world"

	def initialize(self, height, width):
		self.mHeight = height
		self.mWidth = width
		print "Just intialized, w: ", self.mWidth, " h: ", self.mHeight

	def circle(self, num):

		if num % 4 == 0:
			return 'right'
		elif num % 4 == 1:
			return 'down'
		elif num % 4 == 2:
			return 'left'
		elif num % 4 == 3:
			return 'up' 
	
	def findPos(self):
		xdex =0
		ydex= 0
		for x in self.mBoard:
			ydex = 0
			for y in x:
				if y['state'] == 'head' and y['snake'] == 'golden_hamster':
					self.mHead = [xdex, ydex]
				ydex += 1
			xdex += 1
		

	def setBoard(self, width, height):
		self.mWidth = width
		self.mHeight = height

	def init(self, data):
		self.mBoard = data['board']
		self.mTurn = data['turn']
		self.mSnakes = data['snakes']
		self.mFood = data['food']
		self.mWidth = len(data["board"])
		self.mHeight = len(data["board"][0])
		self.mData = data #To simpfly the passing to other objects
		self.findPos()

	def pratice(self):
		foodCalc = food.food(self.mData, self.mHead)
		print foodCalc.findClosetFood()

	def isSafe(self, direction):
		location = []
		if(direction == "up"):
			location.append(self.mHead[0])
			location.append((self.mHead[1] - 1))
		elif(direction == "down"):
			location.append(self.mHead[0])
			location.append((self.mHead[1] + 1))
		elif(direction == "right"):
			location.append((self.mHead[0] + 1))
			location.append(self.mHead[1])
		elif(direction == "left"):
			location.append((self.mHead[0] - 1))
			location.append(self.mHead[1])
		if(location[0] < 0 or location[1] < 0):
			return False
		elif(location[0] > self.mWidth - 1 or location[1] > self.mHeight - 1):
			return False
		elif(self.mBoard[location[0]][location[1]]['state'] == "head"):
			return False
		elif(self.mBoard[location[0]][location[1]]['state'] == "body"):
			return False
		elif(self.mBoard[location[0]][location[1]]['state'] == "food"):
			return True
		elif(self.mBoard[location[0]][location[1]]['state'] == "empy"):
			return True
		return True

		

	def findDanger(self, board):
		
		dirs = {'up': 0, 'down': 0, 'right': 0, 'left': 0}

		xdex =0
		ydex= 0

		for x in board:
			ydex = 0
			for y in x:
				if y['state'] == 'body' or  y['state'] == 'head':
					if(ydex < self.mHead[1] ):
						dirs['up'] += 1
					elif(ydex > self.mHead[1]):
						dirs['down'] += 1;
					if(xdex < self.mHead[0] ):
						dirs['left'] += 1
					elif(xdex > self.mHead[0]):
						dirs['right'] += 1;
				ydex += 1	
			xdex += 1
		print dirs
		if (dirs['up']) < dirs['down'] and (dirs['up']) < dirs['right'] and (dirs['up']) < dirs['left'] and self.isSafe('up'):
			return json.dumps({
				'move':'up',
				'taunt':'Avoid danger up'
			})
		if (dirs['down']) < dirs['up'] and (dirs['down']) < dirs['right'] and (dirs['down']) < dirs['left'] and self.isSafe('down'):
			return json.dumps({
				'move':'down',
				'taunt':'Avoid danger down'
			})
		if (dirs['right'] < dirs['up']) and (dirs['right'] < dirs['down']) and (dirs['right']) < dirs['left'] and self.isSafe('right'):
			return json.dumps({
				'move':'right',
				'taunt':'Avoid danger right'
			})
		if (dirs['left'] < dirs['up']) and (dirs['left'] < dirs['down']) and (dirs['left'] < dirs['right']) and self.isSafe('left'):
			return json.dumps({
				'move':'left',
				'taunt':'Avoid danger left'
			})
		if(self.isSafe('right')):		
			return json.dumps({
				'move':'right',
				'taunt':'isSafe right'
			})
		if(self.isSafe('left')):
			return json.dumps({
				'move':'left',
				'taunt':'isSafe left'
			})
		if(self.isSafe('down')):
			return json.dumps({
				'move':'down',
				'taunt':'isSafe down'
			})
		return json.dumps({
			'move':'right',
			'taunt':'isSafe right'
		})

width = 10
height = 10
think = decide()

@bottle.get('/')
def index():
    return """
        <a href="https://github.com/sendwithus/battlesnake-python">
            battlesnake-python
        </a>
    """


@bottle.post('/start')
def start():
    data = bottle.request.json
    global think
    global height
    global width
    print type(think)
    print "The height is " + str(height)
    print "The width is " + str(width)
    think.initialize(data['width'], data['height'])

    return json.dumps({
        'name': 'golden_hamster',
        'color': 'red',
        'head_url': 'https://peaceandpeanutbutterdotcom.files.wordpress.com/2013/08/smiley-face.jpg',
        'taunt': 'battlesnake-python!'
    })


@bottle.post('/move')
def move():
    
    data = bottle.request.json
    global think
   
    print data

    think.init(data)
    think.pratice()
    return think.findDanger(data['board'])


@bottle.post('/end')
def end():
    data = bottle.request.json

    return json.dumps({})


# Expose WSGI app
application = bottle.default_app()
