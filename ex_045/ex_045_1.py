# a
students = ['Susan Klingsell','Fredrik Harberg','Rasmus Andreasson','Alexis Kan','Tonje Andersen']

#b
print(students[2])

#c
print(students[2][0])

#d
students[2]='Ole'

#e
students[2]+=' Nordmann'

#f
students.append('Rasmus Andreasson')

#g
students.insert(4, 'Monty Python')
print(students)

#h
print(len(students))
students.remove('Ole Nordmann')
print(len(students))

#i
print(students.index('Monty Python'))

#j
print(students[0:3])

#k
students_reverse = students[::-1]
print(students_reverse)

#l
students_even = students[0::2]
print(students_even)

#m
students_odd = students[1::2]
print(students_odd)