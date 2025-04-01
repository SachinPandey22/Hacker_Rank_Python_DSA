# Problem 1: Calculate Tournament Placement
# In the Player class below, each player has a race_outcomes attribute which 
# holds a list of integers describing what place they came in for each race in a tournament.

# Write a method get_tournament_place() that takes in one parameter, opponents, 
# a list of other player objects also participating in the tournament, and returns the place in the overall tournament.

# Rank in the tournament is determined by the lowest average race outcome. (1st place is better than 2nd!)
# Each opponent in opponents is guaranteed to have participated in the same number of races as the current player.
class Player:
    def __init__(self, character, kart, outcomes):
        self.character = character
        self.kart = kart
        self.items = []
        self.race_outcomes = outcomes

    def get_tournament_place(self, opponents):
        self_avg = sum(self.race_outcomes) / len(self.race_outcomes)
        rank = 1
        for opponent in opponents:
            oop_avg = sum(opponent.race_outcomes) / len(opponent.race_outcomes)
            if oop_avg < self_avg:
                rank += 1
        return rank
            


player1 = Player("Mario", "Standard", [1, 7, 1, 1, 3])
player2 = Player("Luigi", "Standard", [2, 1, 3, 2, 2])
player3 = Player("Peach", "Standard", [3, 3, 2, 3, 1])

opponents = [player2, player3]
print(player1.get_tournament_place(opponents))
# Example Output:

# 1 
# Explanation: Mario/player1's average place is 1.6, Luigi's is 2.0, and Peach's is 2.4