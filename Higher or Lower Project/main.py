import art
import random
import game_data

# comparison of two dictionaries with followers and save the dictionary which is correct for the next comparison
# count score function
# while loop
data = random.choice(game_data.data)
def person_info(person_data, label_type):

    info = f"{label_type}: {person_data['name']}, a {person_data['description']}, from {person_data['country']}"
    return info



def compare():
    first_person = person_info(data, 'Compare A' )
    print(first_person)


#     compare_with = []
#     follow_count = []
#     comparison = True
#     while comparison:
#         guess = int(input("Who has more followers? Type 'A' or 'B': "))
#         person_info(data)
#         b = against['follower_count']
#         if guess == a or guess == b:
#
#
# print(art.logo)
# print(art.vs)

compare()

