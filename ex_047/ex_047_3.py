first_number = input('Please enter a number: ')
operator = input('Please write an operator (+, -, *, /): ')
second_number = input('Please enter another number: ')

def my_calculator(first_number, operator, second_number):
    if (not first_number.isnumeric()) or (not second_number.isnumeric()):
        print('You did not enter numbers. Try again!')
    elif not (operator == '+' or operator == '-' or operator == '*' or operator == '/'):
        print('You did not enter one of the operators. Try again!')
    else:
        if operator == '+':
            total_number = int(first_number)+int(second_number)
        elif operator == '-':
            total_number = int(first_number)-int(second_number)
        elif operator == '*':
            total_number = int(first_number)*int(second_number)
        elif operator == '/':
            if second_number == '0':
                print('You cannot divide by zero. Try again!') 
            else:
                total_number = int(first_number)/int(second_number)
        return total_number
    
    
number = my_calculator(first_number,operator,second_number)
print(f'{first_number}{operator}{second_number}={number}')
