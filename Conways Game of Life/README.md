# Conway's Game of Life _in Python3_
_A parody by Skye_


## Table of contents
- [Table of contents](#table-of-contents)
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)


## Description
Conway's Game of Life is a zero player game, once the user sets the initial state it plays itself.
The game is made up of a grid, each cell in the grid is either active or inactive. The state of a cell may change depending on the amount of active cells neighbouring it.  Neighbours are to the sides and the diagonals of a cell.

### Rules
**For active cells:**
- Each cell with **1** or **0** active neighbours will become inactive
- Each cell with **4 or more** active neighbours will become inactive
- Each cell with **2** or **3** active neighbours will stay active

**For inactive cells:**
- Each cell with **3** active neighbours will become active


## Installation
You will need Python3 to run this program ([How to install Python](https://www.ics.uci.edu/~pattis/common/handouts/pythoneclipsejava/python.html))

Clone this repository to your local pc.

_That's it! This project only uses modules that are built into Python3 so there is no need to install anything else._


## Usage
To use this program you will need an input file. This file contains **0**s  and **1**s indicating inactive and active cells respectively. This will be the starting configuration for Conway's Game of Life. _Sample input files can be found in the [patterns](patterns) directory._

1) Open your console application in the same directory as the `main.py` file.

2) To start the game, run the command `python main.py --input "[path to input file]"`. _The path can be a local or full path._

![Run command](https://imgur.com/z9DR4JU.gif)

3) _[OPTIONAL]_ There are other parameters you can play around with.
To view them, run the command `python main.py --help`.

![Help command](https://image.prntscr.com/image/zb7XkIX7RruIxIxQxv458w.png)

4) To end the program, press `Ctrl+c` or close the console window.


## License
[MIT License](LICENSE.md)

