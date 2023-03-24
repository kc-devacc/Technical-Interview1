import random

'''
Calculate the score for a word. The score is the sum of the points for the letters that make up a word. For example: GUARDIAN = 2 + 1 + 1 + 1 + 2 + 1 + 1 + 1 = 10.
Assign seven tiles chosen randomly from the English alphabet to a player's rack.

In the real game, tiles are taken at random from a 'bag' containing a fixed number of each tile. Assign seven tiles to a rack using a bag containing the above distribution.
Find a valid word formed from the seven tiles. A list of valid words can be found in dictionary.txt.
Find the longest valid word that can be formed from the seven tiles.
Find the highest scoring word that can be formed.
Find the highest scoring word if any one of the letters can score triple.
For discussion: how would we adapt our solution for a multiplayer environment?
'''

'''
Object: bag w/ tiles 
dict: tile -> value
Object: player 

Function: creates a word form player tiles & checks them against dictionary
Function: gets the score of word

'''

def score_for_word(word: str) -> int:
    score = 0
    for letter in word:
        score += letter_points[letter.upper()]
    return score


def create_random_hand(number_of_tiles:int = 7) -> list[str]:
    player_hand = []
    for i in range(number_of_tiles):
        player_hand.append(random.choice(alphabet))
    return player_hand


def generate_bag(bag_distro: dict) -> dict:
    bag = {}
    for key in bag_distro.keys():
        for letter in key:
            # maps individual letter in distro to value
            bag[letter] = bag_distro[key]
    return bag

def get_random_tile_from_bag(tile_bag: dict) -> str:
    invalid_tile = True
    
    while invalid_tile:
        tile = random.choice(alphabet)
        if tile_bag[tile] > 0:
            tile_bag[tile] -= 1
            return tile


def assign_player_hand(tile_bag: dict) -> list[str]:
    player_tiles = []
    



letter_points = {
    "A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 8, "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10
}

alphabet = list(letter_points.keys())
bag_distribution = {'E': 12, 'AI': 9, 'O': 8, 'NRT': 6, 'LSUD': 4, 'G': 3, 'BCMPFHVWY': 2, 'KJXQZ': 1}
bag = generate_bag()





