import bottle
import os

moves = []

@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.get('/')
def index():
    head_url = '%s://%s/static/head.jpg' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    return {
        'color': '#00ff00',
        'head': head_url
    }


@bottle.post('/start')
def start():
    data = bottle.request.json

    # TODO: Do things with data

    return {
        'taunt': 'Please change!'
    }


@bottle.post('/move')
def move():
    import consume
    import gameBoardMatrix
    global moves
    data = bottle.request.json

    # TODO: Do things with data
    """
    nextMove = None
    if len(moves) > 0:
        nextMove = moves[0]
        moves = moves[1:]
    else:
        nextMove = 'west'
    """
    data['gameBoard'] =  gameBoardMatrix.GameBoard(data)
    print data
    for i in range(len(data['snakes'])):
        print data['snakes'][i]
    return {
        'move': consume.food70(data),
        'taunt': consume.food70(data)
    }


@bottle.post('/end')
def end():
    data = bottle.request.json

    # TODO: Do things with data

    return {
        'taunt': 'battlesnake-python!'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
