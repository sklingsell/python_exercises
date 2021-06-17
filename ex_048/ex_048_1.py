punishment_text = "I WILL NOT TEACH OTHERS TO FLY THAT GOOD\n"
numb_of_repetition = 10

def bart_cheat_code_while(punishment_text,numb_of_repetition=10):
    counter=0
    while(counter<numb_of_repetition):
        print(punishment_text)
        counter+=1

bart_cheat_code_while(punishment_text)

def bart_cheat_code_for(punishment_text,numb_of_repetition=10):
    for i in range(numb_of_repetition):
        print(punishment_text)

bart_cheat_code_for(punishment_text)