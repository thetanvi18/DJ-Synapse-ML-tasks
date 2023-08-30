# task 1.4: Once up-pawn a time…
# Ref: w3schools
import random

class ChessPlayer:
    def __init__(self, name, age, elo, tenacity, is_boring):
        self.name = name
        self.age = age
        self.elo = elo
        self.tenacity = tenacity
        self.is_boring = is_boring
        self.tournament_score = 0  # initialize score as zero

    
    def simulateMatch(player1, player2):
        elo_diff = abs(player1.elo - player2.elo)
        ten_diff = player1.tenacity - player2.tenacity

        # case a: ELO difference is more than 100
        if elo_diff > 100:
            # the player with higher ELO wins
            if player1.elo > player2.elo:
                return player1
            else:
                return player2

        # case b: ELO difference is between 100 and 50
        elif 100 >= elo_diff >= 50:
            # the player with lower ELO has a chance to win based on tenacity
            if player1.elo < player2.elo:
                lower_elo_player = player1
                higher_elo_player = player2
            else:
                lower_elo_player = player2
                higher_elo_player = player1

            # generate a random factor between 1 and 10
            random_factor = random.randint(1, 10)

            # multiply it by the lower-ELO player's tenacity
            product = random_factor * lower_elo_player.tenacity

            # compare it to the higher-ELO player's ELO
            if product > higher_elo_player.elo:
                # the lower-ELO player wins
                return lower_elo_player
            else:
                # the higher-ELO player wins
                return higher_elo_player

        # case c: ELO difference is less than 50
        elif elo_diff < 50:
            # compare only the tenacity of each player
            if ten_diff > 0:
                # the player with higher tenacity wins
                return player1
            elif ten_diff < 0:
                # the player with lower tenacity wins
                return player2

        # case d: one player is boring and ELO difference is not more than 100
        if (player1.is_boring or player2.is_boring) and elo_diff <= 100:
            # the match is a draw
            return None

# create some ChessPlayer objects
p1 = ChessPlayer("Courage the CD", 25, 1000.39, 1000, False)
p2 = ChessPlayer("Princess Peach", 23, 945.65, 50, True)
p3 = ChessPlayer("Walter White", 50, 1650.73, 750, False)
p4 = ChessPlayer("Rory Gilmore", 16, 1700.87, 500, False)
p5 = ChessPlayer("Anthony Fantano", 37, 1400.45, 400, True)
p6 = ChessPlayer("Beth Harmon", 20, 2500.34, 150, False)

# create a list of players for the tournament
players = [p1, p2, p3, p4, p5, p6]

# print the table header
print("Name\t\t\tAge\tELO\t\tTenacity\tisBoring")

# loop through the players list
for player in players:
    # print the player's attributes separated by tabs and rounded to two decimal places
    print(f"{player.name}\t\t{player.age}\t{round(player.elo, 2)}\t\t{player.tenacity}\t\t{player.is_boring}")
