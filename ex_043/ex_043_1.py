first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
course_name = input('What is the name of the course? ')
num_candidates = input('How many people are taking the course? ')

first_name.capitalize()
last_name.capitalize()
course_name.lower()

#print("My name is " + first_name, end=' ')
#print("with last name " + last_name + ".", end=' ')
#print("I am participating in the course " + course_name + ".", end=' ')
#print("There are " + str(num_candidates) + " candidates taking the " + course_name + " course.")

print(f"My name is {first_name} with last name {last_name}. I am participating in the course {course_name}. There are {num_candidates} candidates taking the {course_name} course.")