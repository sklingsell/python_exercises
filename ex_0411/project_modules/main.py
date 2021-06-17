from graphic.print_text import say_my_name
from graphic.print_text import say_many_names
from simple_math import my_calculator
from simple_math import speak_multiplier

def main():
    say_many_names(speak_multiplier)

    def do_calc():
        first_number = input('Please enter a number: ')
        operator = input('Please write an operator (+, -, *, /): ')
        second_number = input('Please enter another number: ')
        total_number = my_calculator(first_number,operator,second_number)
        print(f'{first_number}{operator}{second_number}={total_number}')

    while True:
        do_calc()
        continue_input = input('Do you want to continue (Y/N)?: ')
        if continue_input == 'Y':
            continue
        elif continue_input == 'N': 
            break


if __name__ == '__main__':
    main()