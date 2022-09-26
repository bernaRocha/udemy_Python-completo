#### Aula sobre quantidade de caracteres

user = input('Digit your username: ')

number_characters = len(user)

print(f'User: {user}, Number of characters: {number_characters}, type: {type(number_characters)}')

print(len(user))         ### same output
print(user.__len__())    ###