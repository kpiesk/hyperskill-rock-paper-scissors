from random import choice


weakness = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
user_option = input()
pc_option = choice(list(weakness.keys()))

if user_option in list(weakness.keys()):
    if weakness[user_option] == pc_option:
        print(f'Sorry, but computer chose {pc_option}')
    elif user_option == pc_option:
        print(f'There is a draw ({user_option})')
    else:
        print(f'Well done. Computer chose {pc_option} and failed')
