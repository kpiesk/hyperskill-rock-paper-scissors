from random import choice


WEAKNESS = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
DRAW_SCORE = 50
WIN_SCORE = 100
FILE_NAME = 'rating.txt'


# allows the player to play rock-paper-scissors against a computer
def main():
    user_name = input('Enter your name: ')
    print(f'Hello, {user_name}')
    user_rating = get_user_rating(user_name)

    while True:
        user_option = input()
        if user_option in list(WEAKNESS.keys()):
            pc_option = choice(list(WEAKNESS.keys()))
            user_rating = game_result(user_option, pc_option, user_rating)
        elif user_option == '!rating':
            print(f'Your rating: {user_rating}')
        elif user_option == '!exit':
            print('Bye!')
            break
        else:
            print('Invalid input')


# checks whether there is a record for the user with the same name in rating.txt
# if yes, returns the rating from the user's previous game session
def get_user_rating(user_name):
    ratings_file = open(FILE_NAME, 'r')
    user_rating = 0

    for line in ratings_file:
        if line.split()[0] == user_name:
            user_rating = int(line.split()[1])

    ratings_file.close()
    return user_rating


# determines the outcome of the game and returns the current user rating
def game_result(user_option, pc_option, user_rating):
    if WEAKNESS[user_option] == pc_option:
        print(f'Sorry, but computer chose {pc_option}')
        return user_rating
    elif user_option == pc_option:
        print(f'There is a draw ({user_option})')
        return user_rating + DRAW_SCORE
    print(f'Well done. Computer chose {pc_option} and failed')
    return user_rating + WIN_SCORE


main()
