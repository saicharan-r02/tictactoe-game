import random 
import math 
import tkinter as tk 
from tkinter import messagebox, ttk 
 
class TicTacToeGUI: 
    def __init__(self, root):
        self.root = root 
        self.root.title("Tic Tac Toe") 
        self.root.geometry("400x500") 
        self.root.resizable(False, False) 
         
        self.board = [[" " for _ in range(3)] for _ in range(3)] 
        self.current_player = "X" 
        self.game_over = False 
        self.scores = {"Wins": 0, "Losses": 0, "Draws": 0} 
        self.difficulty = "medium" 
        self.create_widgets() 
         
    def create_widgets(self): 
        title_frame = tk.Frame(self.root) 
        title_frame.pack(pady=10) 
         
        self.title_label = tk.Label( 
            title_frame,  
            text="Tic Tac Toe",  
            font=("Arial", 20, "bold") 
        ) 
        self.title_label.pack() 
         
        diff_frame = tk.Frame(self.root) 
        diff_frame.pack(pady=5) 
         
        tk.Label(diff_frame, text="Select Difficulty:").pack(side=tk.LEFT)
        self.diff_var = tk.StringVar(value=self.difficulty) 
        diff_menu = ttk.Combobox( 
            diff_frame,  
            textvariable=self.diff_var,  
            values=["easy", "medium", "hard"], 
            state="readonly", 
            width=8 
        ) 
        diff_menu.pack(side=tk.LEFT, padx=5) 
        diff_menu.bind("<<ComboboxSelected>>", self.change_difficulty) 
         
        score_frame = tk.Frame(self.root) 
        score_frame.pack(pady=5) 
         
        self.score_label = tk.Label( 
    score_frame, 
    text=f"Wins: {self.scores['Wins']}  Losses: {self.scores['Losses']}  Draws: {self.scores['Draws']}", 
    font=("Arial", 10) )
     
        self.score_label.pack()  
        self.board_frame = tk.Frame(self.root) 
        self.board_frame.pack(pady=10) 
         
        self.buttons=[] 
        for i in range(3): 
            row=[] 
            for j in range(3): 
                button=tk.Button( 
                    self.board_frame, 
                    text=" ", 
                    font=("Arial", 24, "bold"), 
                    width=4, 
                    height=2, 
                    command=lambda r=i, c=j: self.on_click(r, c) 
                ) 
                button.grid(row=i, column=j, padx=5, pady=5) 
                row.append(button) 
            self.buttons.append(row) 
         
        reset_frame=tk.Frame(self.root) 
        reset_frame.pack(pady=10) 
         
        reset_btn=tk.Button( 
            reset_frame, 
            text="New Game", 
            command=self.reset_game, 
            font=("Arial", 12), 
            width=10 
        ) 
        reset_btn.pack() 
     
    def change_difficulty(self, event): 
        self.difficulty = self.diff_var.get() 
        self.reset_game() 
     
    def on_click(self, row, col): 
        if self.game_over or self.board[row][col] != " ": 
            return 
        
        self.make_move(row, col, "X") 
         
        if self.check_winner("X"): 
            self.game_over = True 
            self.scores["Wins"] += 1 
            self.update_score() 
            messagebox.showinfo("Game Over", "Congratulations! You win!") 
            return 
         
        if self.is_draw(): 
            self.game_over = True 
            self.scores["Draws"] += 1 
            self.update_score() 
            messagebox.showinfo("Game Over", "It's a draw!") 
            return 
         
        self.root.after(500, self.ai_move)  
     
    def ai_move(self): 
        if self.game_over: 
            return 
             
        row, col = self.ai_move_logic(self.board, self.difficulty) 
        self.make_move(row, col, "O") 
         
        if self.check_winner("O"): 
            self.game_over = True 
            self.scores["Losses"] += 1 
            self.update_score() 
            messagebox.showinfo("Game Over", "Computer wins! Try again.") 
            return 
         
        if self.is_draw(): 
            self.game_over = True 
            self.scores["Draws"] += 1 
            self.update_score() 
            messagebox.showinfo("Game Over", "It's a draw!") 
     
    def make_move(self, row, col, player): 
        self.board[row][col] = player 
        self.buttons[row][col].config( 
            text=player,  
            state=tk.DISABLED, 
            fg="red" if player == "X" else "blue" 
        ) 
     
    def update_score(self): 
        self.score_label.config( 
            text=f"Wins: {self.scores['Wins']}  Losses: {self.scores['Losses']}  Draws: {self.scores['Draws']}" 
        ) 
     
    def reset_game(self): 
        self.board = [[" " for _ in range(3)] for _ in range(3)] 
        self.game_over = False 
         
        for i in range(3): 
            for j in range(3): 
                self.buttons[i][j].config(text=" ", state=tk.NORMAL, fg="black") 
     
    def check_winner(self, player): 
        for i in range(3): 
            if (all(self.board[i][j] == player for j in range(3)) or  
               all(self.board[j][i] == player for j in range(3))): 
                
                return True 
        if ( all(self.board[i][i] == player for i in range(3)) or  
           all(self.board[i][2 - i] == player for i in range(3)) ): 
            return True 
        return False 
 
    def is_draw(self): 
        return all(cell != " " for row in self.board for cell in row) 
 
    def get_available_moves(self, board): 
        return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "] 

    def easy_ai(self, board): 
        return random.choice(self.get_available_moves(board)) 
 
    def minimax(self, board, depth, is_maximizing):
     if self.check_winner_board(board, "O"):
      return 10 - depth
     if self.check_winner_board(board, "X"):
      return depth - 10
     if self.is_draw_board(board):
      return 0
     
     if is_maximizing:
         best_score = -math.inf
         for row, col in self.get_available_moves(board):
             board[row][col] = "O"
             score = self.minimax(board, depth + 1, False)
             board[row][col] = " "
             best_score = max(best_score, score)
         return best_score
     else:
         best_score = math.inf
         for row, col in self.get_available_moves(board):
             board[row][col] = "X"
             score = self.minimax(board, depth + 1, True)
             board[row][col] = " "
             best_score = min(best_score, score)
         return best_score 
         else: 
             best = math.inf 
             for row, col in self.get_available_moves(board): 
                 board[row][col] = "X" 
                 score = self.minimax(board, depth + 1, True) 
                 board[row][col] = " " 
                 best = min(best, score) 
             return best 
          
    def hard_ai(self, board): 
        best_score = -math.inf 
        best_move = None 
        for row, col in self.get_available_moves(board): 
            board[row][col] = "O" 
            score = self.minimax(board, 0, False) 
            board[row][col] = " " 
            if score > best_score: 
                best_score = score 
                best_move = (row, col) 
        return best_move 
 

    def medium_ai(self, board): 
        return self.easy_ai(board) if random.random() < 0.5 else self.hard_ai(board) 
 
    def ai_move_logic(self, board, difficulty): 
        if difficulty == "easy": 
            return self.easy_ai(board) 
        elif difficulty == "medium": 
            return self.medium_ai(board) 
        elif difficulty == "hard": 
            return self.hard_ai(board) 

if __name__ == "__main__": 
    r= tk.Tk() 
    game = TicTacToeGUI(r) 
    r.mainloop()
