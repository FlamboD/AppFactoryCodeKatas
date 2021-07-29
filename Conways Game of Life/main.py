from os import system, name
import time
import argparse

parser = argparse.ArgumentParser()
requiredArguments = parser.add_argument_group("required arguments")
symbolArguments = parser.add_argument_group("symbol arguments")


def clear():
	system("cls" if name == "nt" else "clear")


def newBoard(size):
	return [[blank] * size] * size


def cleanInput(inp):
	cleaned = inp[:]

	while all(len(_) and _[0] == "0" for _ in cleaned):
		for i in range(len(cleaned)):
			cleaned[i] = cleaned[i][1:]

	for i in range(len(cleaned)):
		cleaned[i] = cleaned[i].replace("\n", "")
		while not cleaned[i][-1] or cleaned[i][-1] == "0": cleaned[i] = cleaned[i][:-1]
		cleaned[i] = cleaned[i]\
			.replace("0", blank)\
			.replace("1", active)

	if cleaned:
		while not cleaned[0] and cleaned:
			cleaned = cleaned[1:]

	if cleaned:
		while not cleaned[-1] and cleaned:
			cleaned = cleaned[:-1]

	return cleaned


def center(_board, _obj):
	start = [(len(_board) - len(max(_obj)))//2, (len(_board) - len(_obj))//2]
	for i in range(len(_obj)):
		_board[start[1] + i] = _board[start[1]+i][:start[0]] + list(_obj[i]) + _board[start[1]+i][start[0]+len(_obj[i]):]
	return _board


def getNeighbours(board, y, x):
	n = 0
	for ne in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
		ny = y + ne[0]
		nx = x + ne[1]
		if ny < 0 or nx < 0: continue
		try:
			if board[ny][nx] == active: n += 1
		except IndexError:
			pass
	return n


def nextIter(board):
	nextBoard = [[*_] for _ in board]
	for y in range(len(board)):
		for x in range(len(board[y])):
			n = getNeighbours(board, y, x)

			if board[y][x] == active:
				nextBoard[y][x] = active if n == 2 or n == 3 else blank
			else:
				nextBoard[y][x] = active if n == 3 else blank
	return nextBoard


def display(board):
	out = [" ".join(_) for _ in board]
	clear()
	print(*out, sep="\n")


def main(*, _input, size, delay):
	_inp = cleanInput(_input)
	if not all(char in (blank, active) for line in _inp for char in line): raise Exception("Invalid Input")
	board = center(newBoard(size), _inp) if _inp else newBoard(size)
	while True:
		display(board)
		board = nextIter(board)
		time.sleep(delay)


if __name__ == "__main__":
	requiredArguments.add_argument("-i", "--input", default="patterns/glider.txt", help="path to input file")
	parser.add_argument("-d", "--delay", default=1, help="time delay in seconds between each iteration", type=float)
	parser.add_argument("-s", "--size", default=20, help="the size of the board", type=int)
	symbolArguments.add_argument("-a", "--active", default="o", help="character to display in active cells")
	symbolArguments.add_argument("-b", "--blank", default=" ", help="character to display in blank cells")
	args = parser.parse_args()

	if len(args.blank) != 1 or len(args.active) != 1: raise Exception(
		"Active and blank cells can only be a single character each")

	blank = args.blank
	active = args.active

	if args.input:
		with open(args.input, "r") as f:
			userInput = f.readlines()

		height = len(userInput)
		try: width = len(max(userInput))
		except ValueError: raise Exception("Input is empty")

		if height > args.size: raise Exception(f"Input height({height}) is larger than board size({args.size})")
		if width > args.size: raise Exception(f"Input width({width}) is larger than board size({args.size})")
	else:
		userInput = ""
	main(_input=userInput, size=args.size, delay=args.delay)
	pass
else:
	blank = "0"
	active = "1"
