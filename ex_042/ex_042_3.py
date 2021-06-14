punishment_text = "I WILL NOT TEACH OTHERS TO FLY THAT GOOD\n"
numb_of_repetition = 10

#print(punishment_text*numb_of_repetition)

new_text = punishment_text.replace('NOT','').replace('GOOD','BAD').replace('  ',' ')
print(new_text*numb_of_repetition)

count = punishment_text.count('THAT')
print("The occurence of the word THAT in the original sentence is: " + str(count))