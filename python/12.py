class TicTacToe:
    def __init__(self):
        self.board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        self.current_marker = 'X'
        self.current_player = 1

    def draw_board(self):
        for row in self.board:
            print(" ", " | ".join(row), " ")
            print("---|---|---")

    def place_marker(self, slot):
        row = (slot - 1) // 3
        col = (slot - 1) % 3
        if self.board[row][col] not in ['X', 'O']:
            self.board[row][col] = self.current_marker
            return True
        else:
            return False

    def check_winner(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2]:
                return self.current_player
        
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col]:
                return self.current_player
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.current_player
        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.current_player
        
        return 0

    def swap_player_and_marker(self):
        if self.current_marker == 'X':
            self.current_marker = 'O'
            self.current_player = 2
        else:
            self.current_marker = 'X'
            self.current_player = 1

    def play_game(self):
        self.draw_board()
        player_won = 0
        
        for _ in range(9):
            print(f"It's player {self.current_player}'s turn. Enter your slot: ", end="")
            slot = int(input())
            
            if slot < 1 or slot > 9:
                print("Invalid slot! Choose another slot!")
                continue
            
            if not self.place_marker(slot):
                print("Slot is occupied! Choose another slot!")
                continue
            
            self.draw_board()
            player_won = self.check_winner()
            if player_won:
                print(f"Player {player_won} wins!")
                break
            
            self.swap_player_and_marker()
        
        if player_won == 0:
            print("It's a tie!")

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()