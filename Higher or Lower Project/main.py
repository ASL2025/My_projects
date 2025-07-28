import game_data
import random
import art

# extract data from game data for comparison
def game_char():
    character = random.choice(game_data.data)
    data = f"{character['name']}, a {character['description']}, from {character['country']}"
    return data, character['follower_count']

def screen(compare_a, against_b):
    print(compare_a)
    print(art.vs)
    print(against_b)

def comparison(compare_a, against_b, follower_count_a, follower_count_b):
    new_char = ""
    score = 0
    screen(compare_a, against_b)
    guess = input("Who has more followers? Type 'A' or 'B'.").lower()
    if follower_count_a > follower_count_b and guess == 'a':
        new_char = compare_a
        score += 1
        print(f"You are right! current score: {score}")

    elif follower_count_a < follower_count_b and guess == 'b':
        new_char = against_b
        score += 1
        print(f"You are right! current score: {score}")
    else:
        true_guess = False
        print(f"Sorry that's wrong. Final score: {score}")


def checking_guess():
    compare_a, follower_count_a = game_char()
    against_b, follower_count_b = game_char()
    score = 0
    true_guess = True
    while true_guess:
        comparison(compare_a,against_b,follower_count_a,follower_count_b)

checking_guess()

