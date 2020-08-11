from random import choice


DEFAULT_OPTIONS = 'rock,paper,scissors'
FILE_NAME = 'rating.txt'
WIN_SCORE = 100
DRAW_SCORE = 50
RATING_COMMAND = '!rating'
EXIT_COMMAND = '!exit'


def main():
    user_name = input('Enter your name: ')
    print(f'Hello, {user_name}')
    options_weakness = determine_weakness(input())
    print("\nOkay, let's start")
    game(options_weakness, get_user_rating(user_name))


# allows the player to play rock-paper-scissors against a computer
def game(options_weakness, user_rating):
    while True:
        user_option = input()
        if user_option in list(options_weakness.keys()):
            pc_option = choice(list(options_weakness.keys()))
            user_rating = game_result(
                options_weakness, user_option, pc_option, user_rating)
        elif user_option == RATING_COMMAND:
            print(f'Your rating: {user_rating}')
        elif user_option == EXIT_COMMAND:
            print('Bye!')
            break
        else:
            print('Invalid input')


# determines the options weaknesses (which options lose)
# and returns the dictionary of it
def determine_weakness(options_input):
    options = determine_options(options_input)
    weakness = {}

    # iterates through all options, and
    # creates a list of weak options for each option
    for i in range(len(options)):
        # new list is combined from all options following the current option
        # with the options preceding it
        new_list = options[i + 1:] + options[:i]
        # weak options are the first half of the new list
        weak_options = new_list[:int(len(new_list) / 2)]
        weakness[options[i]] = weak_options

    return weakness


# determines which options to use, and returns a list of them
def determine_options(options_input):
    # if the user input is empty, default options are used
    if options_input.strip() is '':
        return DEFAULT_OPTIONS.split(',')
    while True:
        if len(options_input.split(',')) > 2 and \
                len(options_input.split(',')) % 2 != 0:
            return options_input.split(',')
        options_input = input('Invalid options '
                              '(the number of options needs to be odd, '
                              'and at least 3)\n')


# checks whether there is a record for the user with the same name
# in the ratings file
# if yes, returns the rating from the user's previous game session
def get_user_rating(user_name):
    with open(FILE_NAME, 'r') as ratings_file:
        for line in ratings_file:
            if line.split()[0] == user_name:
                return int(line.split()[1])
        else:
            return 0


# determines the outcome of the game and returns the current user rating
def game_result(options_weakness, user_option, pc_option, user_rating):
    if pc_option in options_weakness[user_option]:
        print(f'Sorry, but computer chose {pc_option}')
        return user_rating
    elif user_option == pc_option:
        print(f'There is a draw ({user_option})')
        return user_rating + DRAW_SCORE
    print(f'Well done. Computer chose {pc_option} and failed')
    return user_rating + WIN_SCORE


main()
