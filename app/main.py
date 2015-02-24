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
