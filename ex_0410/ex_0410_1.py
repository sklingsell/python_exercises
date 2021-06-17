keep_going = True
my_dict={}

while keep_going:
    user_input = input('Please enter a key and value pair with a ; in between. \nType revert to exit, save to save your dictionary, load to load a dictionary: ').lower().strip()
    
    if user_input == 'revert':
        keep_going = False
        print(f'Original dictionary: {my_dict}')
        revert_dict = {}
        for key,value in my_dict.items():
            revert_dict[value]=key
        print(f'Reverted dictionary: {revert_dict}')
        break
    
    elif user_input == 'save':
        my_file = open('saved_dict.txt','w')
        data=str(my_dict)
        my_file.write(data)
        my_file.close()

    elif user_input == 'load':
        my_file = open('saved_dict.txt','r')
        data = my_file.read()
        my_dict = eval(data)
        print(my_dict)

    elif not (';' in user_input):
        print('Please enter it in the correct format!')

    else: 
        separated_input = user_input.split(';')
        key = separated_input[0]
        value = separated_input[1]
        my_dict[key]=value
