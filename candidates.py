# A Monte Carlo simulation to predict the candidates tournament
import random

# Ratings are from the June 2022 list, Magnus Carlsen is rated 2864 if you wish
# to include him
players = {
    #"Ian Nepomniachtchi": 2766,
    "Teimour Radjabov": 2753,
    "Jan-Kryzsztof Duda": 2750,
    "Alireza Firouzja": 2793,
    "Fabiano Caruana": 2783,
    "Hikaru Nakamura": 2760,
    "Richard Rapport": 2764,
    "Ding Liren": 2806,
    "Magnus Carlsen": 2864
}

winners = {
    #"Ian Nepomniachtchi": 0,
    "Teimour Radjabov": 0,
    "Jan-Kryzsztof Duda": 0,
    "Alireza Firouzja": 0,
    "Fabiano Caruana": 0,
    "Hikaru Nakamura": 0,
    "Richard Rapport": 0,
    "Ding Liren": 0,
    "Magnus Carlsen": 0
}

# Percentages for ourcomes of games from Lichess masters database
# 43% of games end in draws, white wins 33% and black wins 24%
draw = 0.43
white_edge = 33/24
num_simulations = 100000


def get_outcome(A, B):
    if A == B:
        return None
    QA = 10**(players[A] / 400) * white_edge
    QB = 10**(players[B]/400)
    p = random.uniform(0, 1)
    if p <= draw:
        return "draw"
    else:
        p = random.uniform(0, 1)
        if p < QA / (QA + QB):
            return A
        else:
            return B


def simulate_tournament():
    scores = {
        #"Ian Nepomniachtchi": 0,
        "Teimour Radjabov": 0,
        "Jan-Kryzsztof Duda": 0,
        "Alireza Firouzja": 0,
        "Fabiano Caruana": 0,
        "Hikaru Nakamura": 0,
        "Richard Rapport": 0,
        "Ding Liren": 0,
        "Magnus Carlsen": 0
    }
    for k, v in players.items():
        for K, V in players.items():
            if k == K:
                pass
            else:
                outcome = get_outcome(k, K)
                if outcome == "draw":
                    scores[k] += 0.5
                    scores[K] += 0.5
                else:
                    scores[outcome] += 1
    winner = None
    max_score = float("inf") * (-1)
    for k, v in scores.items():
        if v > max_score:
            winner = k
            max_score = v
    winners[winner] += 1


for i in range(num_simulations):
    simulate_tournament()

print("\n")
for k, v in winners.items():
    print(f"{k} : {round((100 * v) / sum(winners.values()), 2)}")
