# FIXME (1): Finish reading another word and an integer into variables. 
# Output all the values on a single line
favorite_color = input('Enter favorite color:\n')
user_data_2 = input('Please enter a word:\n')
user_data_3 = input('Please enter a number:\n')

print('You entered: {} {} {}'.format(favorite_color, user_data_2, user_data_3))


# FIXME (2): Output two password options
password1 = favorite_color + user_data_2
password2 = '6' + favorite_color + '6' 
print(f'\nFirst password: {password1}')
print(f'Second password: {password2}')


# FIXME (3): Output the length of the two password options
print(len(password1))
print(len(password2))