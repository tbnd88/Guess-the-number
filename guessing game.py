import random	

answerEasy = random.randrange(1,10)
answerMedium = random.randrange(1,100)
answerHard	= random.randrange(1,1000)
exit = 1
diff = input('Choose difficulty Easy, Medium or Hard\n')




if diff.lower() == 'easy':
	while exit != 'q':

		guess = int(input('0-10 or q to quit\n'))

		if guess == answerEasy:
			print('Correct!')
		elif guess < answerEasy:
			print('larger')
		elif guess > answerEasy:
			print('smaller')
		else:
			print('error')

elif diff.lower() == 'medium':
	while exit != 'q':

		guess = int(input('0-100 or q to quit\n'))

		if guess == answerMedium:
			print('Correct!')
		elif guess < answerMedium:
			print('larger')
		elif guess > answerMedium:
			print('smaller')
		else:
			print('error')
elif diff.lower() == 'hard':
	while exit != 'q':

		guess = int(input('0-1000 or q to quit\n'))

		if guess == answerHard:
			print('Correct!')
		elif guess < answerHard:
			print('larger')
		elif guess > answerHard:
			print('smaller')
		else:
			print('error')
else:
	print('Invalid Entry')