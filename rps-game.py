import tkinter as tk
from tkinter import ttk
import random

# --- Colors & Fonts ---
BG_COLOR = "#FFF0F5"
BTN_BG_COLOR = "#FFE4B5"
BTN_FG_COLOR = "#5C4033"
BTN_HOVER_COLOR = "#FFDAB9"
ACCENT_COLOR = "#FFB6C1"
TXT_COLOR = "#4A4A55"

FONT_HEADER = ("Segoe UI", 20, "bold")
FONT_MAIN = ("Segoe UI", 12)
FONT_SMALL = ("Segoe UI", 9)


def setup_style(style: ttk.Style) -> None:
    style.theme_use("clam")
    style.configure("TFrame", background=BG_COLOR)
    style.configure("TLabel", background=BG_COLOR, foreground=TXT_COLOR, font=FONT_MAIN)
    style.configure("Header.TLabel", font=FONT_HEADER, foreground="#D81B60")

    style.configure(
        "Sweet.TButton",
        font=("Segoe UI", 11),
        background=BTN_BG_COLOR,
        foreground=BTN_FG_COLOR,
        cursor="hand2",
        focuscolor="none",
    )
    style.map(
        "Sweet.TButton",
        background=[("active", BTN_HOVER_COLOR)],
    )


# --- Game Logic ---
def play_round(user_choice: str) -> None:
    choices = ["rock", "paper", "scissors"]
    comp_choice = random.choice(choices)

    if comp_choice == user_choice:
        MSG.set("🤝 It’s a draw this round!")
    elif (
        (comp_choice == "rock" and user_choice == "paper")
        or (comp_choice == "paper" and user_choice == "scissors")
        or (comp_choice == "scissors" and user_choice == "rock")
    ):
        MSG.set(f"🎉 You win this round! I chose {comp_choice}")
        userScore.set(userScore.get() + 1)
    else:
        MSG.set(f"😔 You lost this round… I chose {comp_choice}")
        compScore.set(compScore.get() + 1)


def reset_game() -> None:
    MSG.set("")
    compScore.set(0)
    userScore.set(0)


# --- UI Helpers ---
def show_how_to_play() -> None:
    popup = tk.Toplevel(root)
    popup.title("How to Play")
    popup.geometry("350x250")
    popup.resizable(False, False)
    popup.configure(bg=BG_COLOR)

    ttk.Label(popup, text="How to Play", style="Header.TLabel").pack(pady=(20, 15))

    rules_text = (
        "• Rock beats Scissors\n"
        "• Scissors beats Paper\n"
        "• Paper beats Rock\n\n"
        "Pick your move and see if you beat the computer!"
    )

    ttk.Label(
        popup,
        text=rules_text,
        justify="center",
        font=FONT_MAIN,
        background=BG_COLOR,
        foreground=TXT_COLOR,
    ).pack(pady=10)

    ttk.Button(popup, text="Close", style="Sweet.TButton", command=popup.destroy).pack(pady=20)


def switch_to_start() -> None:
    for w in game_frame.winfo_children():
        w.destroy()
    build_start_screen()
    game_frame.pack(fill="both", expand=True)


def switch_to_game() -> None:
    for w in start_frame.winfo_children():
        w.destroy()
    build_game_screen()
    start_frame.pack_forget()
    game_frame.pack(fill="both", expand=True)


def build_start_screen() -> None:
    ttk.Label(start_frame, text="Rock, Paper, Scissors!", style="Header.TLabel").grid(
        column=0, row=0, pady=(40, 20)
    )

    ttk.Label(
        start_frame,
        text="Ready for a fun battle?\nClick 'Play' and show who’s the champion!",
        justify="center",
        wraplength=350,
        font=FONT_MAIN,
    ).grid(column=0, row=1, pady=(0, 30))

    ttk.Button(
        start_frame, text="🎮 Play!", style="Sweet.TButton", command=switch_to_game
    ).grid(column=0, row=2, pady=10, ipadx=20, ipady=8)

    ttk.Button(
        start_frame, text="❓ How to Play", style="Sweet.TButton", command=show_how_to_play
    ).grid(column=0, row=3, pady=5, ipadx=10, ipady=5)


def build_game_screen() -> None:
    ttk.Label(game_frame, text="Let’s play!", style="Header.TLabel").grid(
        column=0, row=0, columnspan=3, pady=(20, 15)
    )

    ttk.Label(game_frame, textvariable=MSG, wraplength=360, justify="center").grid(
        column=0, row=1, columnspan=3, pady=10
    )

    ttk.Label(game_frame, text="Make your move:").grid(
        column=0, row=2, columnspan=3, pady=(0, 15)
    )

    moves = [
        ("🪨 Rock", "rock"),
        ("📄 Paper", "paper"),
        ("✂️ Scissors", "scissors"),
    ]

    for col, (label, choice) in enumerate(moves):
        ttk.Button(
            game_frame,
            text=label,
            style="Sweet.TButton",
            command=lambda c=choice: play_round(c),
        ).grid(column=col, row=3, padx=5, pady=5, sticky="ew")

    score_frame = ttk.Frame(game_frame)
    score_frame.grid(column=0, row=4, columnspan=3, pady=20)

    ttk.Label(score_frame, text="My Score", font=("Segoe UI", 10, "bold")).grid(
        column=0, row=0, padx=15
    )
    ttk.Label(score_frame, text="Your Score", font=("Segoe UI", 10, "bold")).grid(
        column=1, row=0, padx=15
    )

    ttk.Label(
        score_frame, textvariable=compScore, font=("Segoe UI", 12, "bold"), foreground=ACCENT_COLOR
    ).grid(column=0, row=1, padx=15)
    ttk.Label(
        score_frame, textvariable=userScore, font=("Segoe UI", 12, "bold"), foreground=ACCENT_COLOR
    ).grid(column=1, row=1, padx=15)

    ttk.Button(
        game_frame, text="🔄 Reset Game", style="Sweet.TButton", command=reset_game
    ).grid(column=0, row=5, columnspan=3, pady=10, sticky="ew")


# --- Main ---
root = tk.Tk()
root.title("Rock, Paper, Scissors! ✨")
root.geometry("400x500")
root.resizable(False, False)
root.configure(bg=BG_COLOR)

style = ttk.Style()
setup_style(style)

MSG = tk.StringVar()
compScore = tk.IntVar(value=0)
userScore = tk.IntVar(value=0)

start_frame = ttk.Frame(root, padding="30 30 30 30")
game_frame = ttk.Frame(root, padding="20 20 20 20")

build_start_screen()
start_frame.pack(fill="both", expand=True)

root.mainloop()
