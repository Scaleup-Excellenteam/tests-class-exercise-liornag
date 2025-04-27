# To Do -
# install pytest
# Create a separate test file. Remember to import pytest.
# Create an empty test and run it, just to make sure your setup is working.
# Write multiple unittests for Board.check_winner that tests all the edge cases - make sure to test all win cases
# Write a function that tests "TicTacToeGame" and checks that every turn, the Board::check_winner is being called exactly once
# Write a system test for the entire game. Youll have to mock TicTacToeGame::get_move to do so.


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def make_move(self, row, col, symbol):
        if self.board[row][col] == ' ':
            self.board[row][col] = symbol
            return True
        return False

    def is_full(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def check_winner(self, symbol):
        # Check rows
        for row in self.board:
            if all(cell == symbol for cell in row):
                return True
        # Check columns
        for col in range(3):
            if all(self.board[row][col] == symbol for row in range(3)):
                return True
        # Check diagonals
        if all(self.board[i][i] == symbol for i in range(3)) or all(self.board[i][2 - i] == symbol for i in range(3)):
            return True
        return False


class TicTacToeGame:
    def __init__(self):
        self.board = Board()
        self.players = [Player("Player 1", "X"), Player("Player 2", "O")]
        self.current_player_index = 0

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def play(self):
        while True:
            self.board.display()
            current_player = self.players[self.current_player_index]
            print(f"{current_player.name}'s turn ({current_player.symbol})")
            row, col = self.get_move()
            if self.board.make_move(row, col, current_player.symbol):
                if self.board.check_winner(current_player.symbol):
                    self.board.display()
                    print(f"{current_player.name} wins!")
                    break
                elif self.board.is_full():
                    self.board.display()
                    print("It's a tie!")
                    break
                self.switch_player()
            else:
                print("Invalid move, try again.")


    def get_move(self):
        while True:
            try:
                row = int(input("Enter the row (0, 1, or 2): "))
                col = int(input("Enter the column (0, 1, or 2): "))
                if 0 <= row < 3 and 0 <= col < 3:
                    return row, col
                else:
                    print("Invalid input. Please enter a number between 0 and 2.")
            except ValueError:
                print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
    game = TicTacToeGame()
    game.play()
