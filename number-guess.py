
# quit_options = ['Exit', 'exit', 'No', 'no', 'n']
# play_options = ['Yes', 'yes', 'y', 'si']
quit = 'no'
play = 'yes'
tries = 3

play_answer = input('would you like to guess a number? ')

if play_answer != quit:
  number_guess = int(input('guess a number from 1-100'))

  # less than or equal to 0 less than or equal to 101
  if number_guess <= 0 or number_guess >= 101:
    print('guess from 1-100')

  elif number_guess != 3:
    print('incorrect. thanks for playing')

  elif number_guess == 3:
    print('correct! thanks for playing')

  else:
    print('number_guess else')

else:
  print('okay sorry for asking.. youdonthavetoplaymygameBYE')
