from os import system, name
import time
import argparse

parser = argparse.ArgumentParser()
requiredArguments = parser.add_argument_group("required arguments")
symbolArguments = parser.add_argument_group("symbol arguments")

requiredArguments.add_argument("-i", "--input", required=True, help="path to input file")
parser.add_argument("-d", "--delay", default=1, help="time delay in seconds between each iteration", type=float)
parser.add_argument("-s", "--size", default=20, help="the size of the board", type=int)
symbolArguments.add_argument("-a", "--active", default="o", help="character to display in active cells")
symbolArguments.add_argument("-b", "--blank", default=" ", help="character to display in blank cells")
args = parser.parse_args()

if len(args.blank) != 1 or len(args.active) != 1: raise Exception("Active and blank cells can only be a single character each")

blank = args.blank
active = args.active
clear = lambda: system("cls" if name == "nt" else "clear")
newBoard = lambda size: [[blank]*size]*size


def cleanInput(inp):
	cleaned = []
	for line in inp:
		while not line[-1]: line = line[:-1]
		line = line.replace("0", blank)
		line = line.replace("1", active)
		cleaned.append(line.replace("\n", ""))

	if cleaned:
		while not cleaned[0] and cleaned:
			cleaned = cleaned[1:]
	if cleaned:
		while not cleaned[-1] and cleaned:
			cleaned = cleaned[:-1]
	return cleaned


def center(_board, _obj):
	start = [(len(_board) - len(max(_obj)))//2,(len(_board) - len(_obj))//2]
	for i in range(len(_obj)):
		_board[start[1] + i] = _board[start[1]+i][:start[0]] + list(_obj[i]) + _board[start[1]+i][start[0]+len(_obj[i]):]
	return _board


def nextIter(board):
	nextBoard = [[*_] for _ in board]
	for y in range(len(board)):
		for x in range(len(board[y])):
			n = 0
			for ne in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
				ny = y + ne[0]
				nx = x + ne[1]
				if ny < 0 or nx < 0: continue
				try:
					if board[ny][nx] == active: n += 1
				except IndexError: pass

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
	if not all(_ in (blank, active) for l in _inp for _ in l): raise Exception("Invalid Input")
	board = center(newBoard(size), _inp) if _inp else newBoard(size)
	while True:
		display(board)
		board = nextIter(board)
		time.sleep(delay)


if __name__ == "__main__":
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
