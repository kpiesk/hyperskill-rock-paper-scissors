weakness = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}

user_option = input()
pc_option = weakness[user_option]

print(f'Sorry, but computer chose {pc_option}')