while True:
    user_text = input('Please enter a word and a number: ')
    if user_text.startswith('quit '):
        break
    user_data = user_text.split()
    print(f'Eating {user_data[1]} {user_data[0]} a day keeps the doctor away.')