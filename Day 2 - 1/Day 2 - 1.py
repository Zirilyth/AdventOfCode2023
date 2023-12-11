import re

file = open('input.txt', 'r')
readFile = file.readlines()
print(readFile)
total = 0
for line in readFile:
	# print(line)
	gameId = int(line[0 + len('Game') + 1: line.find(':')])
	print('Game ID: ', gameId)

	game = line[line.find(':') + 1:].strip('\n')
	print(game)

	rounds = game.split(';')
	print(rounds)
	roundValid = 1
	for round in rounds:
		print(round.strip())
		print('\n')

		boxes = round.split(',')
		red = 0
		blue = 0
		green = 0
		for color in boxes:
			if 'red' in color:
				red = re.findall(r'\b\d+\b', color)[0]
				print('Red:', red)
			if 'green' in color:
				green = re.findall(r'\b\d+\b', color)[0]
				print('Green:', green)
			if 'blue' in color:
				blue = re.findall(r'\b\d+\b', color)[0]
				print('Blue:', blue)

		if not (int(blue) <= 14 and int(red) <= 12 and int(green) <= 13):
			roundValid = 0
	if roundValid == 1:
		total = total + int(gameId)

print('\n')
print('\n')
print('\n')
print(total)
