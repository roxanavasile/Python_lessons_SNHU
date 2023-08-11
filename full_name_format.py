full_name = input('Enter name: ')
full_name = full_name.split()
print(full_name)

if len(full_name) == 3:
    first_name, middle_name, last_name = full_name
    print(f'{last_name}, {first_name[0]}.{middle_name[0]}.')
elif len(full_name) == 2:
    first_name, last_name = full_name
    print(f'{last_name}, {first_name[0]}.')


