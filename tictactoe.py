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
		p1_input = raw_input("Player 1, which letter would you like? ")
		player1 = Player('human', p1_input, 1)
		p2_input = 'x' if p1_input == 'o' else 'o'
		print "Player 2, you get {0}!".format(p2_input)
		player2 = Player('human', p2_input, 2)
	elif humans == 1:
		# For one player only
		p1_input = raw_input("Player 1, which letter would you like? ")
		player1 = Player('human', p1_input,1)
		p2_input = 'x' if p1_input == 'o' else 'o'
		player2 = Player('cpu', p2_input,2)
	else:
		# For two cpus, this will be implemented later
		p1_input = random.choice(['x', 'o'])
		player1 = Player('cpu', p1_input,1)
		p2_input = 'x' if p1_input == 'o' else 'o'
		player2 = Player('cpu', p2_input,2)

# Creates the board and flat board
board = [['*' for x in range(3)] for y in range (3)]
flat_board = [val for sublist in board for val in sublist]

# The possible board positions
possible = {
		'top-left': [0, 0], 'top-center': [0, 1], 'top-right': [0, 2],
		'left': [1, 0], 'center': [1, 1], 'right': [1, 2],
		'bottom-left': [2, 0], 'bottom-center': [2, 1], 'bottom-right': [2, 2]
	   }

# Winner combinations
# But how tho

def checkWin():
	# horizontal win 0,0 0,1 0,2;| 1,0 1,1 1,2;| 2,0 2,1 2,2
	for sub in board:
		return True if ''.join(sub) in ['xxx', 'ooo'] else False
	# vertical win 0,0,0;| 1,1,1;| 2,2,2
	for x in range(3):
		return True if ''.join(board[0][i], board[1][i], board[2][i]) in ['xxx', 'ooo'] else False
	# cross win ohow pls 0,0 1,1 2,2;| 2,0 1,1 0,2
	
	#draw
	if not flat_board in '-':
		print "Draw! No one wins!"
		playing = False

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
def place(letter, x, y):
	try:
		if board[x][y] == 'x' or board[x][y] == 'o':
			print "You cannot place something there!"
			return 0
		else:
			board[x][y] = letter
			return 1
	except NameError:
		print "Invalid formatting! Your input was {0}.".format(place)

while playing:
	if turn % 2 == 0:
		current_player = player1
	elif turn % 2 != 0:
		current_player = player2
	turn += 1
	print "Turn: {0}, Player: {1}".format(turn, current_player.num)
	print boardFormat()
	if checkWin():
		playing = False

	if current_player.role == "human":

		position = raw_input("Where would you like to put a mark? Top or bottom; right, left or center?\n> ")
		try:
			while place(current_player.letter, possible[position][0], possible[position][1]) == 0:
				# Make sure that I input a valid command.
				position = raw_input("Try again!\n> ")
			place(current_player.letter, possible[position][0], possible[position][1])
		except NameError:
			# Will this interact with the above code, or is it restricted to except?
			while position not in possible:
				print "Name Error"
				position = raw_input("{0} is not a command! Try again.\n> ").format(position)
		except KeyError:
			while position not in possible:
				print "Key Error"
				position = raw_input("{0} is not a command! Try again.\n >").format(position)

	else:
		pass
	# I do not know how to do this yet!


