import bottle
import json

current = 'right'

def circle():
	global current

	if current == 'right':
		current = 'down'
	elif current == 'down':
		current = 'left'
	elif current == 'left':
		current = 'up'
	elif current == 'up':
		current = 'right'

def move(num):
	if num % 4 == 0:
		return 'right';
	elif num % 4 == 1:
		return 'down';
	elif num % 4 == 2:
		return 'left';
	elif num % 4 == 3:
		return 'south';

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
    
    return json.dumps({
        'name': 'battlesnake-python',
        'color': '#00ff00',
        'head_url': 'http://battlesnake-python.herokuapp.com',
        'taunt': 'battlesnake-python!'
    })


@bottle.post('/move')
def move():
    data = bottle.request.json
    print data['turn']
    move(data['turn'])
    global current

    return json.dumps({
        'move': move(data['turn']),
        'taunt': move(data['turn'])
    })


@bottle.post('/end')
def end():
    data = bottle.request.json

    return json.dumps({})


# Expose WSGI app
application = bottle.default_app()
