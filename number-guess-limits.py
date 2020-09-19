# correct_answers = range(100)
the_answer = 3
# quit_options = ['Exit', 'exit', 'No', 'no', 'n']
# play_options = ['Yes', 'yes', 'y', 'si']
quit = 'no'
play = 'yes'
tries = 3

play_answer = input('would you like to guess a number? ')

if play_answer != quit: #if yes
  number_guess = int(input('guess a number from 1-100 '))

  if number_guess == 3:
    print('correct! thanks for playing!')

  if number_guess != 3:
    while tries > 0:
      # less than or equal to 0 || less than or equal to 101
      if number_guess <= 0 or number_guess >= 101:
        number_guess = int(input('out of range, guess a number from 1-100 '))
        tries-=1 # -1 try

      elif number_guess != 3 and number_guess >1 or number_guess <= 100:
        print('not 3 but in range, try again')
        tries-=1 # -1 try

      elif number_guess == 3:
        print('finally correct! thanks for playing!')
        break
      
else: #no
  print('okay.. sorryforaskingyoudonthavetoplaymygameBYE')