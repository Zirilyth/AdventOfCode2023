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
	maxRed = 0
	maxGreen = 0
	maxBlue = 0

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
		if int(red) > int(maxRed):
			maxRed = red
		if int(green) > int(maxGreen):
			maxGreen = green
		if int(blue) > int(maxBlue):
			maxBlue = blue
	total = total + int(maxRed) * int(maxGreen) * int(maxBlue)

print('\n')
print('Total:', total)
