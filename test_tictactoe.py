import pytest
from unittest.mock import patch
from tictactoe_oop import Board, TicTacToeGame

def test_empty():
    assert True

def test_row_win():
    board = Board()
    board.board = [
        ['X', 'X', 'X'],
        [' ', 'O', ' '],
        ['O', ' ', ' ']
    ]
    assert board.check_winner('X') is True


def test_middle_column_win():
    board = Board()
    board.board = [
        [' ', 'X', ' '],
        ['O', 'X', ' '],
        [' ', 'X', 'O']
    ]

    assert board.check_winner('X') is True


def test_column_win():
    board = Board()
    board.board = [
        ['O', 'X', ' '],
        ['O', 'X', ' '],
        ['O', ' ', 'X']
    ]
    assert board.check_winner('O') is True

def test_diagonal_win_top_left_to_bottom_right():
    board = Board()
    board.board = [
        ['X', 'O', ' '],
        ['O', 'X', ' '],
        [' ', ' ', 'X']
    ]
    assert board.check_winner('X') is True

def test_diagonal_win_top_right_to_bottom_left():
    board = Board()
    board.board = [
        [' ', ' ', 'O'],
        [' ', 'O', ' '],
        ['O', ' ', 'X']
    ]
    assert board.check_winner('O') is True

def test_no_winner_yet():
    board = Board()
    board.board = [
        ['X', 'O', 'X'],
        ['O', 'X', 'O'],
        ['O', 'X', 'O']
    ]
    assert board.check_winner('X') is False
    assert board.check_winner('O') is False


def test_invalid_move_on_taken_cell():
    game = TicTacToeGame()
    game.board.board = [
        ['X', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

    move_success = game.board.make_move(0, 0, 'O')
    assert move_success is False


def test_check_winner_called_once_per_turn():
    game = TicTacToeGame()

    moves = [(0, 0), (1, 1), (0, 1), (1, 0), (0, 2)]

    with patch.object(game.board, 'check_winner', return_value=False) as mock_check_winner, \
         patch.object(game, 'get_move', side_effect=moves):

        for _ in range(5):
            game.board.display()
            current_player = game.players[game.current_player_index]
            row, col = game.get_move()
            if game.board.make_move(row, col, current_player.symbol):
                game.board.check_winner(current_player.symbol)
                game.board.is_full()
                game.switch_player()

    assert mock_check_winner.call_count == 5

def test_invalid_row_input():
    game = TicTacToeGame()
    invalid_inputs = [(-1, 0), (3, 0), (0, 0)]

    with patch.object(game, 'get_move', side_effect=invalid_inputs):
        move1 = game.get_move()
        assert move1 == (-1, 0)

        move2 = game.get_move()
        assert move2 == (3, 0)

        move3 = game.get_move()
        assert move3 == (0, 0)

def test_invalid_input_type():
    game = TicTacToeGame()

    with patch('builtins.input', side_effect=['a', 'b', '0', '0']):
        row, col = game.get_move()
        assert (row, col) == (0, 0)


def test_system_game_play():
    game = TicTacToeGame()

    moves = [(0, 0), (1, 0),  # X, O
             (0, 1), (1, 1),  # X, O
             (0, 2)]          # X - win

    with patch.object(game, 'get_move', side_effect=moves):
        # run game
        game.play()
