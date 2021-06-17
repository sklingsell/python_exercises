import os

target_nr = int(input('Write a number please: '))
nr_of_guesses = int(input('How many guesses are allowed?: '))

os.system('cls||clear')

counter = 0
while counter < nr_of_guesses:
    guess_nr = int(input('Guess what the number is: '))
    counter += 1
    if guess_nr < target_nr:
        print('Too low.')
        if counter == nr_of_guesses:
            print(f'This was your final guess. Game over. The correct number was {target_nr}')
    elif guess_nr > target_nr:
        print('Too high.')
        if counter == nr_of_guesses:
            print(f'This was your final guess. Game over. The correct number was {target_nr}')
    else:
        print('Congratulations, you guessed the correct number!')
        counter = nr_of_guesses
    