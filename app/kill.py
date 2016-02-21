class kill(object)
	def __init__(self, data, head):
		self.data = data
		self.ourSnake = getOurSnake(self)
		self.targetsCoord = getTargetHeads(self)
		self.obstacles = data["walls"]

	def getOurSnake(self):	
		snakes = self.data["snakes"]
		for i in snakes:
			if snakes[i]["id"] == "2daa46ee-4880-4285-8572-eeaf52dba551":
				return snakes[i]

	def getTargetHeads(self):
		snakes = self.data["snakes"]
		targetHeadList = []
		for i in snakes:
			if snakes[i]["id"] != "2daa46ee-4880-4285-8572-eeaf52dba551":
				targetHeadList.appennd(snakes[i]["cords"][0],snakes[i]["cords"][1])
		return targetHeadList

	def killSnakeInFrontOfYou(self):
		#check all directions around
		neck = self.ourSnake["coords"][1]
		head = self.ourSnake["coords"][0]
		direction = ""

		north = lambda coords: coords[0],coords[1]+1
		west = lambda coords: coords[0]-1,coords[1]
		east = lambda coords: coords[0]+1,coords[1]
		south = lambda coords: coords[0],coords[1]-1

		if neck[0] = head[0] and neck[1] = head[1]+1:
			direction = "down"
		elif neck[0]+1 = head[0] and neck[1] = head[1]:
			#snake is travelling right
			direction = "right"
		elif neck[0] = head[0]+1 and neck[1] = head[1]:
			#snake is travelling left
			direction = "left"
		elif neck[0] = head[0] and neck[1]+1 = head[1]:
			direction = "up"

		if direction is "down" and south(head) not in self.obstacles:
			return "west",":) :) :) :)"
		if direction is "right" and east(head) not in self.obstacles:
			return "south", "suhhhhhh"
		if direction is "left" and west(head) not in self.obstacles:
			return "north","dude asuh"
		if direction is "up" and north(head) not in self.obstacles:
			return "east", "suh dude"

		return ("",":/")



