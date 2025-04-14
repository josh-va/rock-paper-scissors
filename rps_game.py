import random
from collections import Counter


def play(player1, player2, num_games, verbose=False):
    p1_prev_play = ""
    p2_prev_play = ""
    results = {"p1": 0, "p2": 0, "tie": 0}

    for _ in range(num_games):
        p1_play = player1(p2_prev_play)
        p2_play = player2(p1_prev_play)

        if p1_play == p2_play:
            results["tie"] += 1
            winner = "Tie."
        elif (p1_play == "P" and p2_play == "R") or (
                p1_play == "R" and p2_play == "S") or (p1_play == "S"
                                                       and p2_play == "P"):
            results["p1"] += 1
            winner = "Player 1 wins."
        elif p2_play == "P" and p1_play == "R" or p2_play == "R" and p1_play == "S" or p2_play == "S" and p1_play == "P":
            results["p2"] += 1
            winner = "Player 2 wins."

        if verbose:
            print("Player 1:", p1_play, "| Player 2:", p2_play)
            print(winner)
            print()

        p1_prev_play = p1_play
        p2_prev_play = p2_play

    games_won = results['p2'] + results['p1']

    if games_won == 0:
        win_rate = 0
    else:
        win_rate = results['p1'] / games_won * 100

    print("Final results:", results)
    print(f"Player 1 win rate: {win_rate}%")

    return (win_rate)

def quincy(prev_play, counter=[0]):

    counter[0] += 1
    choices = ["R", "R", "P", "P", "S"]
    return choices[counter[0] % len(choices)]


def mrugesh(prev_opponent_play, opponent_history=[]):
    opponent_history.append(prev_opponent_play)
    last_ten = opponent_history[-10:]
    most_frequent = max(set(last_ten), key=last_ten.count)

    if most_frequent == '':
        most_frequent = "S"

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[most_frequent]


def kris(prev_opponent_play):
    if prev_opponent_play == '':
        prev_opponent_play = "R"
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prev_opponent_play]


def abbey(prev_opponent_play,
          opponent_history=[],
          play_order=[{
              "RR": 0,
              "RP": 0,
              "RS": 0,
              "PR": 0,
              "PP": 0,
              "PS": 0,
              "SR": 0,
              "SP": 0,
              "SS": 0,
          }]):

    if not prev_opponent_play:
        prev_opponent_play = 'R'
    opponent_history.append(prev_opponent_play)

    last_two = "".join(opponent_history[-2:])
    if len(last_two) == 2:
        play_order[0][last_two] += 1

    potential_plays = [
        prev_opponent_play + "R",
        prev_opponent_play + "P",
        prev_opponent_play + "S",
    ]

    sub_order = {
        k: play_order[0][k]
        for k in potential_plays if k in play_order[0]
    }

    prediction = max(sub_order, key=sub_order.get)[-1:]

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prediction]


def human(prev_opponent_play):
    play = ""
    while play not in ['R', 'P', 'S']:
        play = input("[R]ock, [P]aper, [S]cissors? ")
        print(play)
    return play

def random_player(prev_opponent_play):
    return random.choice(['R', 'P', 'S'])

def josh(opp_prev_play, opponent_history=[], my_prev_play='', my_history=[]):
    
    #Adjustable Attributes:
    #Depth that history will be checked against to search for patterns
    depth_a = 3 #Oppenent pattern matching
    depth_b = 3 #Opponent response to my pattern
    depth_c = 3 #Beating my own patterns
    #Chance to perform a purely random throw
    randomness = 0.05

    #Set up predictors and confidences
    conf_a = conf_b = conf_c = 0
    prediction_a = prediction_b = prediction_c = random_throw()

    #Set up prefixes
    my_prefix = 'my_'
    self_prefix = 'self_'

    #Set up Predictor C attributes
    if not hasattr(josh, 'scores'):
        josh.scores = {'A':0, 'B':0, 'C':0}
    if not hasattr(josh, 'last_prediction'):
        josh.last_prediction = {'A':None, 'B':None, 'C':None}
        
    #Clear all history if facing new player and make a random first throw, else add their last play to history
    if opp_prev_play == '':
        opponent_history.clear()
        my_history.clear()
        josh.scores = {'A':0, 'B':0, 'C':0}
        josh.last_prediction = {'A':None, 'B':None, 'C':None}
        clear_lists(josh)
        choice = random_throw()
        my_prev_play = choice
        my_history.append(my_prev_play)
        return choice
    else:
        for predictor in ['A','B','C']:
            prediction = josh.last_prediction[predictor]
            if prediction:
                josh.scores[predictor] += outcome(prediction, opp_prev_play)
        opponent_history.append(opp_prev_play)

    #Update Predictor A
    if len(opponent_history) > depth_a:
        opp_prev_play_code= ''.join(opponent_history[-depth_a-1:-1])
        if not hasattr(josh, opp_prev_play_code):
            setattr(josh, opp_prev_play_code, [opp_prev_play])
        else:
            getattr(josh, opp_prev_play_code).append(opp_prev_play)

    #Update Predictor B
    if len(my_history) > depth_b:
        raw_my_prev_pattern = ''.join(my_history[-depth_b-1:-1])
        my_prev_play_code= my_prefix + raw_my_prev_pattern
        if not hasattr(josh, my_prev_play_code):
            setattr(josh, my_prev_play_code, [opp_prev_play])
        else:
            getattr(josh, my_prev_play_code).append(opp_prev_play)

    #Update Predictor C
    if len(my_history) > depth_c:
        raw_my_prev_pattern = ''.join(my_history[-depth_c-1:-1])
        self_play_code = self_prefix + raw_my_prev_pattern
        if not hasattr(josh, self_play_code):
            setattr(josh, self_play_code, [my_history[-1]])
        else:
            getattr(josh, self_play_code).append(my_history[-1])

    #Fallback for early game
    if len(opponent_history) < min(depth_a, depth_b, depth_c):
        choice = random_throw()
        my_prev_play = choice
        my_history.append(my_prev_play)
        return choice

    #Random Throw
    if randomness > random.random():
        choice = random_throw()
        my_prev_play = choice
        my_history.append(my_prev_play)
        return choice


    #Predictor A
    opp_play_code = ''.join(opponent_history[-depth_a:])
    for i in range(depth_a):
        if hasattr(josh, opp_play_code[:depth_a-i]):
            if getattr(josh, opp_play_code[:depth_a-i]):
                counter = Counter(getattr(josh, opp_play_code[:depth_a-i]))
                prediction_a = counter.most_common(1)[0][0]
                josh.last_prediction['A'] = prediction_a
                conf_a = (counter.most_common(1)[0][1])/(sum(counter.values()))
                break

    #Predictor B
    raw_my_play_code = ''.join(my_history[-depth_b:])
    for i in range(depth_b):
        sliced_pattern = my_prefix + raw_my_play_code[:depth_b - i]
        if hasattr(josh, sliced_pattern):
            if getattr(josh, sliced_pattern):
                counter = Counter(getattr(josh, sliced_pattern))
                prediction_b = counter.most_common(1)[0][0]
                josh.last_prediction['B'] = prediction_b
                conf_b = (counter.most_common(1)[0][1])/(sum(counter.values()))
                break

    #Predictor C
    for i in range(depth_c):
        sliced_pattern = self_prefix + raw_my_play_code[:depth_c - i]
        if hasattr(josh, sliced_pattern):
            if getattr(josh, sliced_pattern):
                counter = Counter(getattr(josh, sliced_pattern))
                my_likely_play = counter.most_common(1)[0][0]
                prediction_c = beat(my_likely_play)
                josh.last_prediction['C'] = prediction_c
                conf_c = (counter.most_common(1)[0][1])/(sum(counter.values()))
                break

    # Predictor Picking

    total_player_scores = sum(josh.scores.values())
    if total_player_scores == 0:
        total_player_scores = 1
    adjusted_score_a = josh.scores['A']/total_player_scores
    adjusted_score_b = josh.scores['B']/total_player_scores
    adjusted_score_c = josh.scores['C']/total_player_scores

    composite_a = conf_a * adjusted_score_a
    composite_b = conf_b * adjusted_score_b
    composite_c = conf_c * adjusted_score_c

    if composite_c > composite_a and composite_c > composite_b:
        choice = beat(prediction_c)
    elif composite_b > composite_a:
        choice = beat(prediction_b)
    else:
        choice = beat(prediction_a)

    #Returns the choice
    my_prev_play = choice
    my_history.append(my_prev_play)
    return choice

def beat(play):
    if play == 'S':
        return 'R'
    elif play == 'R':
        return 'P'
    elif play == 'P':
        return 'S'

def outcome(my_prediction, actual):
    if my_prediction == actual:
        return 2
    elif beat(my_prediction) == actual:
        return 1
    else:
        return 0

def random_throw():
    choice = random.choice(['R', 'P', 'S'])
    return choice

def clear_lists(func):
    for key, value in func.__dict__.items():
        if isinstance(value, list):
            value.clear()