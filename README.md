🎮 ## rock, paper, scissors game

this project is a sweet-themed rock, paper, scissors desktop game built with python and tkinter. the goal is to deliver a cozy, friendly ui with gentle colors, clear screens, and simple sound effects.

## key features
- ✅ multi-screen flow — start, rules, and game screens with smooth switching.  
- ✅ soft color palette — pale pink background with warm beige buttons and dusty rose accents.  
- ✅ built-in sound effects — simple beeps for clicks, wins, losses, and draws.  
- ✅ clear score tracking — separate counters for user and computer with highlighted accent color.  
- ✅ responsive grid layout — neatly aligned buttons and labels for all screen sizes.  

## what this project practices
- designing clean, themed ui with ttk styles.  
- managing multiple screens via pack_forget and pack.  
- using tk variables (stringvar, intvar) for dynamic ui updates.  
- adding basic audio cues with winsound for instant feedback.  
- organizing game logic and ui building in separate functions.  

## how to run
1. ensure you have python installed (3.x recommended).  
2. save the code as `rps_game.py`.  
3. run it from terminal: `python rps_game.py`.  
4. the app will launch with a fixed window size and the start screen.  

## how to play
1. on the start screen, click “🎮 Play!” to begin or “❓ How to Play” to see the rules.  
2. in the game screen, choose your move by clicking one of the buttons: “🪨 Rock”, “📄 Paper”, or “✂️ Scissors”.  
3. the computer will pick a random move; the result (win, loss, or draw) will be shown with a short sound effect.  
4. your scores and the computer’s scores update automatically after each round.  
5. use “🔄 Reset Game” to clear scores and start fresh.  
6. to return to the start screen from the rules, click “🔙 Back”.  

## notes
- the game uses a simple win/loss/draw logic based on classic rock, paper, scissors rules.  
- sound effects are minimal and use basic beeps; they work on windows systems with winsound.  
- if you click the move buttons very fast, multiple events might fire before the ui updates.  
- some unusual characters don’t affect this game (no text input), but the design is optimized for standard emoji and text.  
- the window size is fixed for a consistent look across systems.  

