class food(object):
	def __init__(self, data, head):
		self.mFood = data['food']
		self.mHead = head

	def findClosetFood(self):
		closet = [0, 0]
		shortDist = 0 #can't actually equal zero
		for food in self.mFood:
			dist = abs(mHead[0] - food[0])
			dist += abs(mHead[1] - food[1])
			if(dist < shortDist or shortDist == 0):
				shortDist = dist
				closet = food

		print "findClosetFood: ", food
		return closet
