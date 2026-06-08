import tkinter as tk
from tkinter import messagebox
# Import all necessary functions from the logic file
from tictactoe_logic import create_board, check_win, check_draw, is_game_over, find_best_move

class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        master.title("Tic-Tac-Toe AI")
        master.geometry("700x700") # Slightly larger for better spacing
        master.resizable(False, False) # Fixed size for simpler layout

        self.board = create_board()
        self.current_player = 'X' # Human player
        self.game_active = True

        self.buttons = []
        self.create_widgets()
        self.reset_game() # Initialize game state and GUI

    def create_widgets(self):
        # Title Label
        self.title_label = tk.Label(self.master, text="Tic-Tac-Toe AI", font=("Inter", 24, "bold"), fg="#333333")
        self.title_label.pack(pady=10)

        # Status Label
        self.status_label = tk.Label(self.master, text="Your turn (X)", font=("Inter", 14), fg="#007bff")
        self.status_label.pack(pady=5)

        # Board Frame
        self.board_frame = tk.Frame(self.master, bg="#666666", bd=5, relief=tk.RIDGE)
        self.board_frame.pack(pady=10)

        # Create 3x3 grid of buttons
        for i in range(9):
            button = tk.Button(self.board_frame, text=" ", font=("Inter", 36, "bold"),
                               width=4, height=2, bg="#e0e0e0", fg="#333333",
                               command=lambda i=i: self.make_move(i))
            button.grid(row=i // 3, column=i % 3, padx=2, pady=2)
            self.buttons.append(button)

        # Reset Button
        self.reset_button = tk.Button(self.master, text="Reset Game", command=self.reset_game,
                                      font=("Inter", 12, "bold"), bg="#ff6347", fg="white",
                                      activebackground="#e55337", activeforeground="white",
                                      relief=tk.FLAT, bd=0, padx=20, pady=10, cursor="hand2")
        self.reset_button.pack(pady=15)

    def reset_game(self):
        """Resets the game board and status for a new game."""
        self.board = create_board()
        self.current_player = 'X'
        self.game_active = True
        self.status_label.config(text="Your turn (X)", fg="#007bff")
        for i in range(9):
            self.buttons[i].config(text=" ", state=tk.NORMAL, bg="#e0e0e0", fg="#333333")

    def make_move(self, index):
        """Handles a player's move (human or AI)."""
        if self.board[index] == ' ' and self.game_active and self.current_player == 'X':
            # Human's move
            self.board[index] = 'X'
            self.buttons[index].config(text='X', fg="#007bff", state=tk.DISABLED)
            self.check_game_status()
            if self.game_active:
                self.current_player = 'O'
                self.status_label.config(text="AI's turn (O)", fg="#ff9900")
                self.master.after(500, self.ai_move) # AI makes move after a short delay

    def ai_move(self):
        """Calculates and executes the AI's move."""
        if self.game_active and self.current_player == 'O':
            ai_best_move = find_best_move(self.board)
            if ai_best_move != -1: # Ensure a valid move was found
                self.board[ai_best_move] = 'O'
                self.buttons[ai_best_move].config(text='O', fg="#ff9900", state=tk.DISABLED)
                self.check_game_status()
                if self.game_active:
                    self.current_player = 'X'
                    self.status_label.config(text="Your turn (X)", fg="#007bff")
            else:
                # This case should ideally not be reached in a playable game unless it's a draw
                self.check_game_status() # Re-check in case of unexpected state

    def check_game_status(self):
        """Checks if the game has ended and updates the GUI."""
        if check_win(self.board, 'X'):
            self.status_label.config(text="You Win!", fg="#28a745")
            self.game_active = False
            self.disable_all_buttons()
            messagebox.showinfo("Game Over", "Congratulations! You win!")
        elif check_win(self.board, 'O'):
            self.status_label.config(text="AI Wins!", fg="#dc3545")
            self.game_active = False
            self.disable_all_buttons()
            messagebox.showinfo("Game Over", "AI wins! Better luck next time.")
        elif check_draw(self.board):
            self.status_label.config(text="It's a Draw!", fg="#6c757d")
            self.game_active = False
            self.disable_all_buttons()
            messagebox.showinfo("Game Over", "It's a draw!")

    def disable_all_buttons(self):
        """Disables all game board buttons."""
        for button in self.buttons:
            button.config(state=tk.DISABLED)

# --- Main execution ---
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()
