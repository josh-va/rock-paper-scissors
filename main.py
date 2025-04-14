# This is a simple Rock, Paper, Scissors game against a bot called Josh.
# Josh will try to find patterns in the opponent's moves and adjust its strategy accordingly.
# You can play against Josh manually or build your own bot to play against it.
# If playing manually, it is recommended to play at least a 100 game round to see the Josh's attempts to learn from your patterns.
# If you want to test your own bot, you can update the `your_bot` function with your bot's logic and return the move.

# These files are adapted from the FreeCodeCamp Rock, Paper, Scissors project.
# The original project can be found here: https://www.freecodecamp.org/learn/machine-learning-with-python/machine-learning-with-python-projects/rock-paper-scissors

# I have included the original bots from the FreeCodeCamp project - Mrugesh, Abbey, Quincy, Kris and Random_Player to be tested against your bot or Josh.

from rps_game import play, human, josh, mrugesh, abbey, quincy, kris, random_player
from your_bot import your_bot

#play(player1=human, player2=josh, num_games=100, verbose=True)

print('Playing against Quincy')
play(player1=your_bot, player2=quincy, num_games=1000)
print('Playing against Abbey')
play(player1=your_bot, player2=abbey, num_games=1000)
print('Playing against Kris')
play(player1=your_bot, player2=kris, num_games=1000)
print('Playing against Mrugesh')
play(player1=your_bot, player2=mrugesh, num_games=1000)
print('Playing against Josh')
play(player1=your_bot, player2=josh, num_games=1000)