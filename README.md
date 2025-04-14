# 🪨📄✂️ Rock Paper Scissors 🪨📄✂️

This project lets you simulate and test Rock Paper Scissors bots against a variety of opponents — including your own custom AI or even yourself!
It's based on FreeCodeCamp’s Rock Paper Scissors ML project, with my bot Josh added to the mix.

This project builds on code provided by FreeCodeCamp.

## 🧠 Create Your Own Bot

You can develop your own bot by editing the your_bot.py file. The scaffold is ready to go — just implement logic in the your_bot() function to return either 'R', 'P', or 'S', based on the opponent's previous move.

## 🚀 Getting Started

Run the simulation using:

```bash
python main.py
```

By default, this will simulate 1000 games between your bot (your_bot) and each included bots.

Changes can be made to `main.py` to change what games are run.

## 🧾 Example Output

```yaml
Final results: { "p1": 385, "p2": 301, "tie": 314 }
Player 1 win rate: 56.12244897959183%
```

To see individual round outcomes, set verbose=True in the play() function inside main.py.

## 🎮 Manual Play

You can also play manually:

1. Set player1 to 'human' in `main.py`
2. Run the program
3. Input your move (R, P, or S) when prompted

Set `verbose=True` in the `play()` function in `main.py` to see feedback after each round.

## ⚙️ Customization

- Choose any of the included bots to test against (Josh, Abbey, etc.)
- Set the number of games to simulate
- Mix and match bot battles or pit human vs AI

## 📁 Included Bots

The repo includes several predefined bots adapted from the FreeCodeCamp project along with my own bot Josh.
Each bot has its own strategy — from random plays to pattern-based predictions.

### Josh

This is the bot that I developed.
Josh utilizes three predictive models and selects the most effective one to determine its next move.

- Predicting based on an opponent's patterns
- Predicting based on an opponent's response to it's own patterns
- Predicting based on opponents learning it's own patterns
  Josh will also occasionally perform a purely random play to throw off others.
  Josh's depth parameters and randomness factor are tunable for experimentation and performance optimization.
  Josh is expected to achieve over a 60% win rate against the other bots in games of at least 1000 rounds and becomes more reliable the longer the match goes on.

### Quincy

Developed by the FreeCodeCamp Team.
A predictable bot that cycles through a repeating pattern: "R", "R", "P", "P", "S". Good for testing how well your bot adapts to fixed strategies.

### Mrugesh

Developed by the FreeCodeCamp Team.
Tracks the opponent's last 10 moves and identifies the most frequently played move in that window. It then plays the move that would beat that most frequent choice. Adapts slowly but is solid against consistent patterns.

### Kris

Developed by the FreeCodeCamp Team.
Very simple strategy: always counters the opponent's last move directly. If it sees "R", it plays "P", and so on. Essentially acts as a reactive mirror.

### Abbey

Developed by the FreeCodeCamp Team.
A more advanced pattern recognizer. Tracks pairs of consecutive moves made by the opponent and uses frequency data to predict the next likely move based on the last observed move. Counters that prediction. More adaptive and tends to perform better in longer matches.

## 📦 Requirements

This project uses Python3, standard library modules and no external dependencies.

## 🙌 Credits

FreeCodeCamp for the base project and the Quincy, Abbey, Kris and Mrugesh bots.
