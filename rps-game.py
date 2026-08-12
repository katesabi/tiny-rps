import tkinter as tk
from tkinter import ttk
import random
import winsound

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


# --- Style ---
def setup_style(style: ttk.Style) -> None:
    style.theme_use("clam")
    style.configure("TFrame", background=BG_COLOR)
    style.configure(
        "TLabel",
        background=BG_COLOR,
        foreground=TXT_COLOR,
        font=FONT_MAIN,
    )
    style.configure(
        "Header.TLabel",
        font=FONT_HEADER,
        foreground="#D81B60",
    )
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


# --- Sound Effects ---
def play_click() -> None:
    winsound.Beep(1000, 100)

def play_win() -> None:
    winsound.Beep(800, 200)
    winsound.Beep(1000, 200)
    winsound.Beep(1200, 300)

def play_lose() -> None:
    winsound.Beep(1200, 150)
    winsound.Beep(900, 150)
    winsound.Beep(600, 250)

def play_draw() -> None:
    winsound.Beep(900, 150)
    winsound.Beep(900, 150)


# --- Game Logic ---
def play_round(user_choice: str) -> None:
    choices = ["rock", "paper", "scissors"]
    comp_choice = random.choice(choices)

    if comp_choice == user_choice:
        MSG.set("🤝 It’s a draw this round!")
        play_draw()
    elif (
        (comp_choice == "rock" and user_choice == "paper")
        or (comp_choice == "paper" and user_choice == "scissors")
        or (comp_choice == "scissors" and user_choice == "rock")
    ):
        MSG.set(f"🎉 You win this round! I chose {comp_choice}")
        userScore.set(userScore.get() + 1)
        play_win()
    else:
        MSG.set(f"😔 You lost this round… I chose {comp_choice}")
        compScore.set(compScore.get() + 1)
        play_lose()


def reset_game() -> None:
    MSG.set("")
    compScore.set(0)
    userScore.set(0)
    play_click()


# --- Screen Switching ---
def show_screen(screen_name: str) -> None:
    for frame in [start_frame, rules_frame, game_frame]:
        frame.pack_forget()

    play_click()

    if screen_name == "start":
        start_frame.pack(fill="both", expand=True)
    elif screen_name == "rules":
        rules_frame.pack(fill="both", expand=True)
    elif screen_name == "game":
        game_frame.pack(fill="both", expand=True)


# --- Screens---
def build_start_screen() -> None:
    ttk.Label(
        start_frame,
        text="Rock, Paper, Scissors!",
        style="Header.TLabel",
    ).grid(column=0, row=0, pady=(40, 20))

    ttk.Label(
        start_frame,
        text="Ready for a fun battle?\nClick 'Play' and show who’s the champion!",
        justify="center",
        wraplength=350,
        font=FONT_MAIN,
    ).grid(column=0, row=1, pady=(0, 30))

    btn_frame = ttk.Frame(start_frame)
    btn_frame.grid(column=0, row=2, pady=10)

    ttk.Button(
        btn_frame,
        text="🎮 Play!",
        style="Sweet.TButton",
        command=lambda: show_screen("game"),
    ).pack(side="left", padx=15)

    ttk.Button(
        btn_frame,
        text="❓ How to Play",
        style="Sweet.TButton",
        command=lambda: show_screen("rules"),
    ).pack(side="left", padx=15)


def build_rules_screen() -> None:
    ttk.Label(
        rules_frame,
        text="How to Play",
        style="Header.TLabel",
    ).pack(pady=(30, 15))

    rules_text = (
        "• Rock beats Scissors\n"
        "• Scissors beats Paper\n"
        "• Paper beats Rock\n\n"
        "Pick your move and see if you beat the computer!"
    )

    ttk.Label(
        rules_frame,
        text=rules_text,
        justify="center",
        font=FONT_MAIN,
        background=BG_COLOR,
        foreground=TXT_COLOR,
    ).pack(pady=15)

    ttk.Button(
        rules_frame,
        text="🔙 Back",
        style="Sweet.TButton",
        command=lambda: show_screen("start"),
    ).pack(pady=20)


def build_game_screen() -> None:
    ttk.Label(
        game_frame,
        text="Let’s play!",
        style="Header.TLabel",
    ).grid(column=0, row=0, columnspan=3, pady=(20, 15))

    ttk.Label(
        game_frame,
        textvariable=MSG,
        wraplength=360,
        justify="center",
    ).grid(column=0, row=1, columnspan=3, pady=10)

    ttk.Label(
        game_frame,
        text="Make your move:",
        font=FONT_MAIN,
    ).grid(column=0, row=2, columnspan=3, pady=(0, 15))

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

    ttk.Label(
        score_frame,
        text="My Score",
        font=("Segoe UI", 10, "bold"),
    ).grid(column=0, row=0, padx=15)
    ttk.Label(
        score_frame,
        text="Your Score",
        font=("Segoe UI", 10, "bold"),
    ).grid(column=1, row=0, padx=15)

    ttk.Label(
        score_frame,
        textvariable=compScore,
        font=("Segoe UI", 12, "bold"),
        foreground=ACCENT_COLOR,
    ).grid(column=0, row=1, padx=15)
    ttk.Label(
        score_frame,
        textvariable=userScore,
        font=("Segoe UI", 12, "bold"),
        foreground=ACCENT_COLOR,
    ).grid(column=1, row=1, padx=15)

    ttk.Button(
        game_frame,
        text="🔄 Reset Game",
        style="Sweet.TButton",
        command=reset_game,
    ).grid(column=0, row=5, columnspan=3, pady=10, sticky="ew")


# --- Main ---
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Rock, Paper, Scissors! ✨")
    root.geometry("400x550")
    root.resizable(False, False)
    root.configure(bg=BG_COLOR)

    style = ttk.Style()
    setup_style(style)

    # Variables
    MSG = tk.StringVar()
    compScore = tk.IntVar(value=0)
    userScore = tk.IntVar(value=0)

    # Frames
    start_frame = ttk.Frame(root, padding="30 30 30 30")
    rules_frame = ttk.Frame(root, padding="30 30 30 30")
    game_frame = ttk.Frame(root, padding="20 20 20 20")

    # Screens
    build_start_screen()
    build_rules_screen()
    build_game_screen()

    # Screen
    start_frame.pack(fill="both", expand=True)

    root.mainloop()
