import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe - GUI Game")
        self.master.geometry("400x500")
        self.master.resizable(False, False)
        self.turn = "X"
        self.board = [""] * 9
        self.buttons = []
        self.score = {"X": 0, "O": 0, "Draw": 0}

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.master, text="Tic Tac Toe", font=("Helvetica", 24, "bold"))
        self.title_label.pack(pady=10)

        self.status_label = tk.Label(self.master, text="Turn: Player X", font=("Helvetica", 14))
        self.status_label.pack(pady=5)

        self.board_frame = tk.Frame(self.master)
        self.board_frame.pack()

        for i in range(9):
            button = tk.Button(self.board_frame, text="", font=("Helvetica", 20), width=5, height=2,
                               command=lambda i=i: self.button_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

        self.reset_button = tk.Button(self.master, text="Reset Game", font=("Helvetica", 12), bg="lightblue",
                                      command=self.reset_game)
        self.reset_button.pack(pady=10)

        self.scoreboard = tk.Label(self.master, text=self.get_score_text(), font=("Helvetica", 12), justify="center")
        self.scoreboard.pack(pady=10)

        self.footer = tk.Label(self.master, text="Developed in Python using Tkinter", font=("Helvetica", 8))
        self.footer.pack(side="bottom", pady=10)

    def button_click(self, index):
        if self.buttons[index]["text"] == "" and not self.check_winner():
            self.buttons[index]["text"] = self.turn
            self.board[index] = self.turn

            if self.check_winner():
                self.end_game(f"Player {self.turn} wins!")
                self.score[self.turn] += 1
                self.update_scoreboard()
            elif "" not in self.board:
                self.end_game("It's a Draw!")
                self.score["Draw"] += 1
                self.update_scoreboard()
            else:
                self.turn = "O" if self.turn == "X" else "X"
                self.status_label.config(text=f"Turn: Player {self.turn}")

    def check_winner(self):
        b = self.board
        win_positions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
            (0, 4, 8), (2, 4, 6)              # Diagonal
        ]
        for pos in win_positions:
            if b[pos[0]] == b[pos[1]] == b[pos[2]] and b[pos[0]] != "":
                for i in pos:
                    self.buttons[i].config(bg="lightgreen")
                return True
        return False

    def end_game(self, result_msg):
        self.status_label.config(text=result_msg)
        messagebox.showinfo("Game Over", result_msg)

    def reset_game(self):
        self.board = [""] * 9
        self.turn = "X"
        self.status_label.config(text="Turn: Player X")
        for button in self.buttons:
            button.config(text="", bg="SystemButtonFace")

    def update_scoreboard(self):
        self.scoreboard.config(text=self.get_score_text())

    def get_score_text(self):
        return (f"Scoreboard\n"
                f"Player X: {self.score['X']}\n"
                f"Player O: {self.score['O']}\n"
                f"Draws: {self.score['Draw']}")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
