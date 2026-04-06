import tkinter as tk
from tkinter import messagebox
import random
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

class MemoryGame:
    def __init__(self, root):
        try:
            self.root = root
            self.root.title("Python Memory Matching Game")
            self.root.state('zoomed')
            self.root.resizable(True, True)

            self.cards, self.buttons = [], []
            self.card_faces = []
            self.first_guess = self.second_guess = None
            self.matches_found = self.attempts = 0
            self.can_click = True

            self.load_images()

            self.setup_background()
            self.setup_ui()
            self.start_new_game()

        except FileNotFoundError as e:
            messagebox.showerror("Missing File", f"Required image file not found:\n{e}")
        except tk.TclError as e:
            messagebox.showerror("Image Error", f"Failed to load image:\n{e}")
        except Exception as e:
            messagebox.showerror("Startup Error", f"Failed to initialize the game:\n{e}")

    def load_images(self):
        try:
            self.img_back  = tk.PhotoImage(file=os.path.join(SCRIPT_DIR, "card_back.png"))
            self.img_bg    = tk.PhotoImage(file=os.path.join(SCRIPT_DIR, "game_bg.png"))
            
            cards_dir = os.path.join(SCRIPT_DIR, "cards")
            if os.path.exists(cards_dir):
                for f in os.listdir(cards_dir):
                    if f.endswith(".png"):
                        full_img = tk.PhotoImage(file=os.path.join(cards_dir, f))
                        self.card_faces.append(full_img)
            
            if not self.card_faces:
                raise FileNotFoundError("Could not find any card face images in the 'cards' directory.")

        except FileNotFoundError as e:
            raise FileNotFoundError(f"Image file missing: {e}")
        except tk.TclError as e:
            raise tk.TclError(f"Cannot read image file: {e}")

    def setup_background(self):
        try:
            self.root.configure(bg="#2a0a0a")
            bg_label = tk.Label(self.root, image=self.img_bg, bg="#2a0a0a")
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            print(f"Warning: Background setup failed: {e}")
            self.root.configure(bg="#2a0a0a")

    def setup_ui(self):
        try:
            tk.Label(self.root, text="Memory Matching Game", font=("Helvetica", 24, "bold"),
                     bg="#3a0a0a", fg="#ffd700", padx=15, pady=5).pack(pady=(15, 5))

            info = tk.Frame(self.root, bg="#3a0a0a")
            info.pack(pady=5)

            self.attempts_label = tk.Label(info, text="Attempts: 0", font=("Helvetica", 14, "bold"),
                                           bg="#3a0a0a", fg="#ffd700")
            self.attempts_label.pack(side=tk.LEFT, padx=20)

            tk.Button(info, text="Restart", font=("Helvetica", 12, "bold"), bg="#ff5722", fg="white",
                      relief=tk.FLAT, padx=12, pady=2, cursor="hand2",
                      command=self.start_new_game).pack(side=tk.LEFT, padx=10)

            tk.Button(info, text="Exit", font=("Helvetica", 12, "bold"), bg="#c62828", fg="white",
                      relief=tk.FLAT, padx=12, pady=2, cursor="hand2",
                      command=self.root.destroy).pack(side=tk.LEFT, padx=10)

            self.grid_frame = tk.Frame(self.root, bg="#1a0505", bd=3, relief=tk.RIDGE)
            self.grid_frame.pack(expand=True, pady=20)

        except Exception as e:
            messagebox.showerror("UI Error", f"Failed to set up the UI:\n{e}")

    def start_new_game(self):
        try:
            self.first_guess = self.second_guess = None
            self.matches_found = self.attempts = 0
            self.matched_indices = set()
            self.can_click = True
            if hasattr(self, 'attempts_label'):
                self.attempts_label.config(text="Attempts: 0")

            for w in self.grid_frame.winfo_children():
                w.destroy()
            self.buttons.clear()

            self.cards = list(range(len(self.card_faces))) * 2
            random.shuffle(self.cards)

            total_cards = len(self.cards)
            cols = 4 
            
            for i in range(total_cards):
                btn = tk.Button(self.grid_frame, image=self.img_back, bg="#1a0505",
                                activebackground="#1a0505", relief=tk.FLAT, bd=8, highlightthickness=0,
                                command=lambda idx=i: self.on_card_click(idx))
                btn.grid(row=i // cols, column=i % cols, padx=7, pady=7)
                self.buttons.append(btn)

        except Exception as e:
            messagebox.showerror("Game Error", f"Failed to start a new game:\n{e}")

    def on_card_click(self, idx):
        try:
            if not self.can_click:
                return
            btn = self.buttons[idx]
            if idx in getattr(self, 'matched_indices', set()) or self.first_guess == idx:
                return

            face_img_id = self.cards[idx]
            
            btn.config(image=self.card_faces[face_img_id], bg="#1a0505")

            if self.first_guess is None:
                self.first_guess = idx
            else:
                self.second_guess = idx
                self.attempts += 1
                self.attempts_label.config(text=f"Attempts: {self.attempts}")
                self.can_click = False
                self.root.after(800, self.check_match)

        except IndexError:
            print("Error: Card index out of range!")
        except Exception as e:
            print(f"Card click error: {e}")

    def check_match(self):
        try:
            i1, i2 = self.first_guess, self.second_guess

            if self.cards[i1] == self.cards[i2]:
                for i in (i1, i2):
                    self.buttons[i].config(bg="#4caf50", relief=tk.RIDGE, bd=8)
                    if hasattr(self, 'matched_indices'):
                        self.matched_indices.add(i)
                self.matches_found += 1
                
                if self.matches_found == len(self.card_faces):
                    messagebox.showinfo("Congratulations!",
                                        f"You won in {self.attempts} attempts!\nPlay again?")
                    self.start_new_game()
            else:
                for i in (i1, i2):
                    self.buttons[i].config(image=self.img_back, bg="#1a0505")

            self.first_guess = self.second_guess = None
            self.can_click = True

        except IndexError:
            print("Error: Invalid card index during match check!")
            self.first_guess = self.second_guess = None
            self.can_click = True
        except TypeError:
            print("Error: Card selection was incomplete!")
            self.first_guess = self.second_guess = None
            self.can_click = True
        except Exception as e:
            print(f"Match check error: {e}")
            self.can_click = True

if __name__ == "__main__":
    try:
        root = tk.Tk()
        MemoryGame(root)
        root.mainloop()
    except Exception as e:
        print(f"Failed to run the game: {e}")
