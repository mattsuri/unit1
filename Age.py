#Matthew Suriawinata
#1/17/18
#Age.py - age



name = input('What is your name? ')
print('Hello', name)
first_name, last_name = name.split()

age = int(input('What is your age?'))
print ('you are' , age, 'years old')

print("Your first name has", len(first_name), "letters")
print("Your last name has", len(last_name), "letter")
print("Next year you will be ", age + 1, "years old")

