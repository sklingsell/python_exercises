import random

dice=[1,2,3,4,5,6]
n_dices = 5

rand_dices = random.choices(dice,k=n_dices)

if rand_dices[0] == rand_dices[1] == rand_dices[2] == rand_dices[3] == rand_dices[4] == rand_dices[5]:
    print('Congratulations, you scored a yahtzee!')
else: 
    print('Better luck next time!')

sorted_dices = sorted(rand_dices)
print("Minimum value: " + str(min(sorted_dices)))
print("Maximum value: " + str(max(sorted_dices)))
print("Sorted list: " + str(sorted_dices))