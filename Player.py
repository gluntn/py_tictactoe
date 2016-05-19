from random import randint

class Player(object):
	def __init__(self, role, letter, num):
		self.role = role
		self.letter = letter
		self.num = num
	
	# Intended for the CPU
	def cpu_calculate(self, array, choices):
		flattened = [val for sublist in choices for val in sublist]
		# This will find the best possible move to do, currently, it just finds a random place.
		if ['x', 'o'] not in flattened:
			# Place it in the middle, if the board is empty
			return array[1][1]
		else:
		#occupied = False
		#while not occupied:
		#if ['x','o'] in array[randint(0,2), randint(0,2)]:
			pass

				
	def _occupied_space(array, x, y):
		return True if ['x', 'o'] in array[x][y] else False
