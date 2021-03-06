# pylint: disable=C
import unittest

from chessgame.main.pawn import Pawn
from chessgame.main.exceptions import OutOfBoundsException
from chessgame.main.consts import GAME_SIZE
from chessgame.main.consts import COLOR_BLACK
from chessgame.main.consts import COLOR_WHITE


class PawnTest(unittest.TestCase):

    def test_get_pos(self):
        f = Pawn(0, 0, COLOR_BLACK)
        self.assertTrue(f.get_position() == (0, 0))
        f = Pawn(2, 2, COLOR_WHITE)
        self.assertTrue(f.get_position() == (2, 2))
        f = Pawn(0, 2, COLOR_WHITE)
        self.assertTrue(f.get_position() == (0, 2))

    def test_out_of_bounds(self):
        with self.assertRaises(OutOfBoundsException):
            Pawn(-1, -1, COLOR_BLACK)
        with self.assertRaises(OutOfBoundsException):
            Pawn(0, GAME_SIZE, COLOR_WHITE)
        with self.assertRaises(OutOfBoundsException):
            Pawn(100, 0, COLOR_BLACK)
        with self.assertRaises(OutOfBoundsException):
            Pawn(GAME_SIZE, GAME_SIZE, COLOR_WHITE)

    def test_move_not_allowed_b(self):
        f = Pawn(0, 0, COLOR_BLACK)
        self.assertFalse(f.move_to(0, 0, COLOR_WHITE))

        f = Pawn(1, 1, COLOR_BLACK)
        self.assertFalse(f.move_to(1, 1, COLOR_WHITE))
        self.assertFalse(f.move_to(1, 1, None))

        self.assertFalse(f.move_to(1, 0, None))
        self.assertFalse(f.move_to(0, 1, None))
        self.assertFalse(f.move_to(2, 1, None))

        self.assertFalse(f.move_to(1, 0, None))
        self.assertFalse(f.move_to(1, 0, COLOR_WHITE))

        self.assertFalse(f.move_to(1, 2, True))
        self.assertFalse(f.move_to(0, 2, None))
        self.assertFalse(f.move_to(2, 2, None))

        self.assertFalse(f.move_to(3, 3, COLOR_WHITE))
        self.assertFalse(f.move_to(3, 3, None))

        f = Pawn(2, GAME_SIZE-1, COLOR_BLACK)
        with self.assertRaises(OutOfBoundsException):
            self.assertFalse(f.move_to(2, GAME_SIZE, None))
        with self.assertRaises(OutOfBoundsException):
            self.assertFalse(f.move_to(1, GAME_SIZE, COLOR_WHITE))
        with self.assertRaises(OutOfBoundsException):
            self.assertFalse(f.move_to(1, -1, COLOR_WHITE))

        f = Pawn(1, 1, COLOR_BLACK)
        self.assertFalse(f.move_to(0, 2, COLOR_BLACK))

    def test_move_not_allowed_w(self):
        f = Pawn(0, 0, COLOR_WHITE)
        self.assertFalse(f.move_to(0, 0, COLOR_BLACK))

        f = Pawn(1, 1, COLOR_WHITE)
        self.assertFalse(f.move_to(1, 1, COLOR_BLACK))
        self.assertFalse(f.move_to(1, 1, None))

        self.assertFalse(f.move_to(1, 2, None))
        self.assertFalse(f.move_to(0, 1, None))
        self.assertFalse(f.move_to(2, 1, None))

        self.assertFalse(f.move_to(1, 2, None))
        self.assertFalse(f.move_to(1, 2, COLOR_BLACK))

        self.assertFalse(f.move_to(1, 0, COLOR_BLACK))
        self.assertFalse(f.move_to(0, 0, None))
        self.assertFalse(f.move_to(2, 0, None))

        self.assertFalse(f.move_to(3, 0, COLOR_BLACK))
        self.assertFalse(f.move_to(3, 0, None))

        f = Pawn(2, 0, COLOR_WHITE)
        with self.assertRaises(OutOfBoundsException):
            self.assertFalse(f.move_to(2, -1, None))
        with self.assertRaises(OutOfBoundsException):
            self.assertFalse(f.move_to(1, -1, COLOR_BLACK))

        f = Pawn(1, GAME_SIZE-2, COLOR_WHITE)
        self.assertFalse(f.move_to(0, GAME_SIZE-3, COLOR_WHITE))

    def test_move_allowed_b(self):
        f = Pawn(1, 1, COLOR_BLACK)
        self.assertTrue(f.move_to(1, 2, None))
        self.assertTrue(f.get_position() == (1, 2))

        f = Pawn(1, 1, COLOR_BLACK)
        self.assertTrue(f.move_to(0, 2, COLOR_WHITE))
        self.assertTrue(f.get_position() == (0, 2))

        f = Pawn(1, 1, COLOR_BLACK)
        self.assertTrue(f.move_to(2, 2, COLOR_WHITE))
        self.assertTrue(f.get_position() == (2, 2))

    def test_move_allowed_w(self):
        f = Pawn(1, GAME_SIZE-2, COLOR_WHITE)
        self.assertTrue(f.move_to(1, GAME_SIZE-3, None))
        self.assertTrue(f.get_position() == (1, GAME_SIZE-3))

        f = Pawn(1, GAME_SIZE-2, COLOR_WHITE)
        self.assertTrue(f.move_to(0, GAME_SIZE-3, COLOR_BLACK))
        self.assertTrue(f.get_position() == (0, GAME_SIZE-3))

        f = Pawn(1, GAME_SIZE-2, COLOR_WHITE)
        self.assertTrue(f.move_to(2, GAME_SIZE-3, COLOR_BLACK))
        self.assertTrue(f.get_position() == (2, GAME_SIZE-3))

    def test_move_double_at_start_b(self):
        f = Pawn(1, 1, COLOR_BLACK)
        self.assertTrue(f.move_to(1, 3, None))
        self.assertTrue(f.get_position() == (1, 3))

        f = Pawn(1, 1, COLOR_BLACK)
        self.assertFalse(f.move_to(1, 3, COLOR_WHITE))
        self.assertTrue(f.get_position() == (1, 1))

        f = Pawn(1, 2, COLOR_BLACK)
        self.assertFalse(f.move_to(1, 4, None))
        self.assertTrue(f.get_position() == (1, 2))

    def test_move_double_at_start_w(self):
        f = Pawn(1, GAME_SIZE-2, COLOR_WHITE)
        self.assertTrue(f.move_to(1, GAME_SIZE-4, None))
        self.assertTrue(f.get_position() == (1, GAME_SIZE-4))

        f = Pawn(1, GAME_SIZE-2, COLOR_WHITE)
        self.assertFalse(f.move_to(1, GAME_SIZE-4, COLOR_BLACK))
        self.assertTrue(f.get_position() == (1, GAME_SIZE-2))

        f = Pawn(1, GAME_SIZE-3, COLOR_WHITE)
        self.assertFalse(f.move_to(1, GAME_SIZE-5, None))
        self.assertTrue(f.get_position() == (1, GAME_SIZE-3))
