# -*- coding: UTF-8 -*-
import random
from Player import Player
import time

"""
Author: William Østensen
Name: Tic-Tac-Toe

A game of Tic-Tac-Toe with simple AI.
"""

try:
	humans = int(raw_input("How many humans are playing? Choose between 0-2: "))
except ValueError:
	print "Not even a number!"

if humans not in [0,1,2]:
	print "You cannot play with {0} humans".format(humans)
else:
	# Could use shortening
	if humans == 2:
		p1_input = raw_input("Player 1, which letter would you like?")
		player1 = Player('human', p1_input)
		p2_input = 'x' if p1_input == 'o' else 'o'
		print "Player 2, you get {0}!".format(p2_input)
		player2 = Player('human', p2_input)
	elif humans == 1:
		# For one player only
		p1_input = raw_input("Player 1, which letter would you like?")
		player1 = Player('human', p1_input)
		p2_input = 'x' if p1_input == 'o' else 'o'
		player2 = Player('cpu', p2_input)
	else:
		# For two cpus, this will be implemented later
		p1_input = random.choice(['x', 'o'])
		player1 = Player('cpu', p1_input)
		p2_input = 'x' if p1_input == 'o' else 'o'
		player2 = Player('cpu', p2_input)

# Creates the board
board = [['-' for x in range(3)] for y in range (3)]

# The possible board positions
possible = {
		'top-left': board[0][0], 'top-center': board[0][1], 'top-right': board[0][2],
		'left': board[1][0], 'center': board[1][1], 'right': board[1][2],
		'bottom-left': board[2][0], 'bottom-center': board[2][1], 'bottom-right': board[2][2]
	   }

# Winner combinations
# But how tho 

# Turn number
turn = 0

# Check if you are playing or not
playing = True

def boardFormat():
	return '''
	{0} | {1} | {2}
	{3} | {4} | {5}
	{6} | {7} | {8}'''.format(board[0][0], board[0][1], board[0][2], board[1][0], board[1][1], board[1][2], board[2][0], board[2][1], board[2][2])

# Place a mark if it's possible
def place(place, letter):
	try:
		if place == 'o' or place == 'x':
			print "You cannot place something there!"
			return 0
		else:
			place = letter
			return 1
	except NameError:
		print "Invalid formatting! Your input was {0}.".format(place)

while playing:
	if turn % 2 != 0:
		current_player = player1
	elif turn % 2 == 0:
		current_player = player2
	turn += 1
	print "Turn: {0}".format(turn)
	print boardFormat()

	if current_player.role == "human":

		position = raw_input("Where would you like to put a mark? Top or bottom, right, left or center?\n> ")
		try:
			while place(possible[position], current_player.letter) == 0:
				# Make sure that I input a valid command.
				position = raw_input("Try again!\n> ")
			place(possible[position], current_player.letter)
		except NameError:
			# Will this interact with the above code, or is it restricted to except?
			while position not in possible:
				position = raw_input("{0} is not a command! Try again.\n> ")

	else:
		pass
	# I do not know how to do this yet!


