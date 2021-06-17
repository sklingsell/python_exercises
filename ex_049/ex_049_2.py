keep_going = True
my_dict={}

while keep_going:
    user_input = input('Please enter a key and value pair with a ; in between. Type revert to exit: ').lower().strip()
    
    if user_input == 'revert':
        keep_going = False
        print(f'Original dictionary: {my_dict}')
        revert_dict = {}
        for key,value in my_dict.items():
            revert_dict[value]=key
        print(f'Reverted dictionary: {revert_dict}')
        break
    
    elif not (';' in user_input):
        print('Please enter it in the correct format!')

    else: 
        separated_input = user_input.split(';')
        key = separated_input[0]
        value = separated_input[1]
        my_dict[key]=value
