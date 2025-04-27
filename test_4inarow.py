import pytest
from unittest.mock import patch
from inarow import FourInARow

@pytest.fixture
def game():
    return FourInARow()

@pytest.fixture
def game_with_horizontal_win():
    game = FourInARow()
    game.board[0][0] = 'X'
    game.board[0][1] = 'X'
    game.board[0][2] = 'X'
    game.board[0][3] = 'X'
    return game

def test_entire_shortest_game_win():
    game = FourInARow()
    game.make_move(0)
    game.make_move(0)
    game.make_move(1)
    game.make_move(1)
    game.make_move(2)
    game.make_move(2)
    assert game.make_move(3)

def test_make_move(game):
    with patch.object(game, 'switch_players') as mock_switch_players:
        assert not game.make_move(0)
        assert game.board == [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                              [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                              [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                              [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                              [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                              ['X', ' ', ' ', ' ', ' ', ' ', ' ']]
        mock_switch_players.assert_called_once()

def test_get_next_empty_row(game):
    game.board[5][0] = 'X'
    game.board[4][0] = 'O'
    game.board[3][0] = 'X'
    assert game.get_next_empty_row(0) == 2

def test_check_horizontal_win(game_with_horizontal_win):
    assert game_with_horizontal_win.check_horizontal_win(0)

def test_check_vertical_win():
    game = FourInARow()
    game.board[0][0] = 'X'
    game.board[1][0] = 'X'
    game.board[2][0] = 'X'
    game.board[3][0] = 'X'
    assert game.check_vertical_win(0)

def test_check_positive_slope_diagonal_win():
    game = FourInARow()
    game.board[0][0] = 'X'
    game.board[1][1] = 'X'
    game.board[2][2] = 'X'
    game.board[3][3] = 'X'
    assert game.check_positive_slope_diagonal_win(3, 3)

def test_check_negative_slope_diagonal_win():
    game = FourInARow()
    game.board[5][0] = 'X'
    game.board[4][1] = 'X'
    game.board[3][2] = 'X'
    game.board[2][3] = 'X'
    assert game.check_negative_slope_diagonal_win(2, 3)

def test_check_tie():
    game = FourInARow()
    game.board = [['O', 'X', 'O', 'X', 'O', 'X', 'O'],
                  ['X', 'O', 'X', 'O', 'X', 'O', 'X'],
                  ['O', 'X', 'O', 'X', 'O', 'X', 'O'],
                  ['X', 'O', 'X', 'O', 'X', 'O', 'X'],
                  ['O', 'X', 'O', 'X', 'O', 'X', 'O'],
                  ['X', 'O', 'X', 'O', 'X', 'O', 'X']]
    assert game.check_tie()

def test_switch_players():
    game = FourInARow()
    game.current_player = 'X'
    game.switch_players()
    assert game.current_player == 'O'
    game.switch_players()
    assert game.current_player == 'X'
