import bottle
import json

current = 'right'

class decide:
	def __init__(self):
		print 'class created'

	def circle(self, num):
		if num % 4 == 0:
			return 'right'
		elif num % 4 == 1:
			return 'down'
		elif num % 4 == 2:
			return 'left'
		elif num % 4 == 3:
			return 'up' 


move = None

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
    global move
    move = decide()

    return json.dumps({
        'name': 'battlesnake-python',
        'color': 'red',
        'head_url': 'http://battlesnake-python.herokuapp.com',
        'taunt': 'battlesnake-python!'
    })


@bottle.post('/move')
def move():
    
    data = bottle.request.json
    global move
    print data['turn']

    return json.dumps({
        'move': move.circle(data['turn']),
        'taunt': move.circle(data['turn'])
    })


@bottle.post('/end')
def end():
    data = bottle.request.json

    return json.dumps({})


# Expose WSGI app
application = bottle.default_app()
