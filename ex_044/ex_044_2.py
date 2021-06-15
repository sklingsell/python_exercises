import random

dice_one = random.randint(1,6)
dice_two = random.randint(1,6)
dice_three = random.randint(1,6)
dice_four = random.randint(1,6)
dice_five = random.randint(1,6)

if dice_one == dice_two == dice_three == dice_four == dice_five:
    print(f'{dice_one},{dice_two},{dice_three},{dice_four},{dice_five}')
    print('Congratulations. You generated a Yahtzee!!!')
else:
    print(f'{dice_one},{dice_two},{dice_three},{dice_four},{dice_five}')
    print('Better luck next time!')