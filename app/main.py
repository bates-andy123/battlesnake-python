import bottle
import json

current = 'right'

class decide:
	def __init__(self, height, width):
		self.mHeight = height
		self.mWidth = width

	def circle(self, num):

		if num % 4 == 0:
			return 'right'
		elif num % 4 == 1:
			return 'down'
		elif num % 4 == 2:
			return 'left'
		elif num % 4 == 3:
			return 'up' 
	
	def findPos(self, board):
		xdex =0
		ydex= 0
		for x in board:
			ydex = 0
			for y in x:
				if y['state'] == 'head' and y['snake'] == 'golden_hamster':
					self.head = [xdex, ydex]
				ydex += 1
			xdex += 1
		print self.head

	def findDanger(self, board):

		self.findPos(board)
		dirs = {'up': 0, 'down': 0, 'right': 0, 'left': 0}

		xdex =0
		ydex= 0

		for x in board:
			ydex = 0
			for y in x:
				if y['state'] == 'snake':
					if(ydex < self.head[1] ):
						dirs['up'] += 1
					elif(ydex > self.head[1]):
						dirs['down'] += 1;
					if(xdex < self.head[0] ):
						dirs['left'] += 1
					elif(xdex > self.head[0]):
						dirs['right'] += 1;
				ydex += 1	
			xdex += 1

		if (dirs['up']) > dirs['down'] and (dirs['up']) > dirs['right'] and (dirs['up']) > dirs['left'] and isSafe('up'):
			return 'up'
		if (dirs['down']) > dirs['up'] and (dirs['down']) > dirs['right'] and (dirs['down']) > dirs['left'] and isSafe('down'):
			return 'down'
		if (dirs['right'] > dirs['up']) and (dirs['right'] > dirs['down']) and (dirs['right']) > dirs['left'] and isSafe('right'):
			return 'right'
		if (dirs['left'] > dirs['up']) and (dirs['left'] > dirs['down']) and (dirs['left'] > dirs['right']) and isSafe('left'):
			return 'left'
		if(isSafe('right')):		
			return 'right'
		if(isSafe('left')):
			return 'left'
		if(isSafe('down')):
			return 'down'
		return 'up'


think = None

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
    think = decide(data['height'], data['width'])

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
    print data['turn']
    think.findPos(data['board'])
    return json.dumps({
        'move': think.circle(data['turn']),
        'taunt': think.circle(data['turn'])
    })


@bottle.post('/end')
def end():
    data = bottle.request.json

    return json.dumps({})


# Expose WSGI app
application = bottle.default_app()
