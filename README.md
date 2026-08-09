🎮  rock, paper, scissors! ✨

a cute and simple gui game built with python and tkinter. play against the computer, track your score, and enjoy a sweet, pastel-themed interface.

📋 how to run

1. make sure you have python 3.6 or higher installed.
2. save the code as rps_game.py.
3. open a terminal or command prompt.
4. navigate to the folder where the file is saved.
5. run:
   python rps_game.py
6. enjoy the game! 🎉

🕹️ how to play

- click “🎮 play!” to start the game.
- choose your move: rock, paper, or scissors.
- the game will tell you if you won, lost, or it’s a draw.
- your score and the computer’s score are tracked in real time.
- click “🔄 reset game” to reset the scores at any time.
- click “❓ how to play” to see the rules in a popup window.

🎨 features

- cute pastel ui with custom colors and fonts.
- score tracking for both you and the computer.
- how to play popup with simple rules.
- reset button to restart scoring anytime.
- clean separation of ui and game logic.
- designed for a small, fixed window for a cozy feel.

🧠 what i practiced while building this

- tkinter gui development: labels, buttons, frames, and dynamic updates with stringvar and intvar.
- event handling: button commands and logical flow between screens.
- game logic: simple win/draw/lose conditions.
- ui structure: switching between start screen and game screen by destroying and rebuilding widgets.
- styling with ttk: customizing themes, fonts, colors, and hover effects.
- user experience: clear feedback, intuitive buttons, and a “how to play” helper.

⚠️ known issues

- if you click the move buttons very fast, multiple events might fire before the ui updates.
- some unusual characters don’t affect this game (no text input), but the design is optimized for standard emoji and text.
- the window size is fixed for a consistent look across systems.

🛠️ tech stack

- language: python 3.6+
- gui framework: tkinter + ttk
- randomization: random module

🤝 license

this project is open for learning and experimentation. feel free to fork, modify, and improve it!
