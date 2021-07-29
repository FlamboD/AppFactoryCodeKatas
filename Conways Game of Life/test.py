import unittest
from main import *


class TestGameOfLife(unittest.TestCase):
    def test_newBoard(self):
        board = newBoard(5)
        self.assertEqual(
            board,
            [
                ["0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0"]
            ]
        )

    def test_center(self):
        board = [
            ["0", "0", "0"],
            ["0", "0", "0"],
            ["0", "0", "0"]
        ]

        self.assertEqual(
            center(board, ["1"]),
            [
                ["0", "0", "0"],
                ["0", "1", "0"],
                ["0", "0", "0"]
            ]
        )

    def test_cleanInput(self):
        cleaned = cleanInput(["0100\n", "001", "1110"])
        self.assertEqual(cleaned, ["01", "001", "111"])

    def test_getNeighbours(self):
        board = [
            ["0", "0", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "0"],
            ["0", "1", "1", "1", "0"],
            ["0", "0", "0", "0", "0"]
        ]

        self.assertEqual(
            getNeighbours(board, 2, 2),
            5
        )

    def test_nextIttr(self):
        board = [
            ["0", "0", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "0"],
            ["0", "1", "1", "1", "0"],
            ["0", "0", "0", "0", "0"]
        ]

        self.assertEqual(
            nextIter(board),
            [
                ["0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
                ["0", "1", "0", "1", "0"],
                ["0", "0", "1", "1", "0"],
                ["0", "0", "1", "0", "0"]
            ]
        )
