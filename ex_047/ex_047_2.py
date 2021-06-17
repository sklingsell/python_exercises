
def bart_cheat_code(punishment_text, numb_of_repetition=10):


    text = (punishment_text*numb_of_repetition)
    return text

text= bart_cheat_code("I WILL NOT TEACH OTHERS TO FLY THAT GOOD\n",10)
print(text)

text2= bart_cheat_code("I WILL NOT TEACH OTHERS TO FLY\n",5)
print(text2)

text3= bart_cheat_code("THIS IS A WORKING TEXT\n",8)
print(text3)

text4= bart_cheat_code("I WILL NOT SPECIFY THE NUMBER OF REPETITIONS HERE\n")
print(text4)