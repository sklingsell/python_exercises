captured = tuple(['Pikachu','Pidgey','Abra','Pidgey','Eevee','Pidgey'])

count = captured.count('Pidgey')
print(count)

pokemon = input('Type a pokemon name: ')

if pokemon in set(captured):
    print('Pokemon has already been captured')
else:
    print('Pokemon has not been captured yet')

print("Total number of captured pokemon: " + str(len(captured)))
print("Number of unique captured pokemon: " + str(len(set(captured))))