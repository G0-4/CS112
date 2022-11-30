password = input('Enter a password: ')
correct = 'mason_gmu'
x = 0

if password == correct:
    print('you\'re right!')
else:
    while x < 2 and password != correct:
        x += 1
        password = input('Enter a password: ')