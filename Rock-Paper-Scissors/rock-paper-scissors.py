from random import choice


weakness = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}


# allows the player to play rock-paper-scissors against a computer
def main():
    while True:
        user_option = input()
        if user_option in list(weakness.keys()):
            pc_option = choice(list(weakness.keys()))
            print(game_result(user_option, pc_option))
        elif user_option == '!exit':
            print('Bye!')
            break
        else:
            print('Invalid input')


# determines the outcome of the game and returns the string of it
def game_result(user_option, pc_option):
    if weakness[user_option] == pc_option:
        return f'Sorry, but computer chose {pc_option}'
    elif user_option == pc_option:
        return f'There is a draw ({user_option})'
    return print(f'Well done. Computer chose {pc_option} and failed')


main()