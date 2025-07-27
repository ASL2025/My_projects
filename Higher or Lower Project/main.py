import game_data
import random
import art


# extract data from game data for comparison
def game_char():
    character = random.choice(game_data.data)
    data = f"{character['name']}, a {character['description']}, from {character['country']}"
    return data, character['follower_count']

compare_A, follower_count_a = game_char()
against_B, follower_count_b = game_char()
#
def comparison(compare,against, guess):
    if follower_count_a > follower_count_b and guess == 'a':
        new_char.append(compare_A)
        return score += 1
    elif follower_count_a < follower_count_b and guess == 'b':
        new_char.append(against_B)
        return score += 1
    else:
        true_guess = False


def checking_guess():
    score = 0
    true_guess = True
    while true_guess:
        new_char = []
        guess = input("Who has more followers? Type 'A' or 'B'."),lower()
        comparison(compare_A, against_B, guess)

