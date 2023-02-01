import random
import time
import sys

def easy_mode():
	score = 100
	answerEasy = random.randrange(1,11)
	while True:

		guess = input('1-10 or q to quit\n')
		if guess.isdigit():

			if int(guess) == answerEasy:
				print('Correct! Your score was', score)
				play_again()
			elif int(guess) < answerEasy:
				print('larger')
				if score > 0:
					score = score - 10
				else:
					score = 0
			elif int(guess) > answerEasy:
				print('smaller')
				if score > 0:
					score = score - 10
				else:
					score = 0
		elif guess.lower() == 'q':
				return end()
		else:
			print('Invaid input')
			easy_mode()

def medium_mode():
	score = 100
	answerMedium = random.randrange(1,101)

	while True:
		guess = input('1-100 or q to quit\n')
		if guess.isdigit():

			if int(guess) == answerMedium:
				print('Correct! Your score was', score)
				play_again()
			elif int(guess) < answerMedium:
				print('larger')
				if score > 0:
					score = score - 5
				else:
					score = 0
			elif int(guess) > answerMedium:
				print('smaller')
				if score > 0:
					score = score - 5
				else:
					score = 0
		elif guess.lower() == 'q':
				return end()
		else:
			print('Invalid input')
			medium_mode()

def hard_mode():
	score = 100
	answerHard	= random.randrange(1,1001)

	while True:
		guess = input('1-1000 or q to quit\n')
		if guess.isdigit():

			if int(guess) == answerHard:
				print('Correct! Your score was', score)
				play_again()
			elif int(guess) < answerHard:
				print('larger')
				if score > 0:
					score = score - 1
				else:
					score = 0
			elif int(guess) > answerHard:
				print('smaller')
				if score > 0:
					score = score - 1
				else:
					score = 0
		elif guess.lower() == 'q':
			return end()
		else:
			print('Invalid input')
			hard_mode()

def end():
	print('Thanks for playing!')
	time.sleep(2)
	sys.exit()

def play_again():
	playAgain = input('Would you like to play again?')
	if playAgain == 'y' or playAgain.lower == 'yes':
		main()
	elif playAgain == 'n' or playAgain.lower == 'no':
		end()
	else:
		print('Please choose y or n')
		play_again()

def main():
	chooseMode = int(input("Choose a difficulty: 1,2,3\n"))

	if chooseMode == 1:
		easy_mode()
	elif chooseMode == 2:
		medium_mode()
	elif chooseMode == 3:
		hard_mode()
	else:
		print("enter valid mode")

while True:
	main()