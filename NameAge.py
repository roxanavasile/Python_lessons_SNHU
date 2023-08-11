import datetime

#get user data
name = input('What is your name? ')
age = int(input('How old are you? '))

#calculate birth year 
today = datetime.date.today()
current_year = today.year
birth_year = current_year - age

print(f'Hello {name}! You were born in {birth_year}.')
