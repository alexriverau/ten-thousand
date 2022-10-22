import game_logic

print('Welcome to Ten Thousand')
print(f'(y)es to play or (n)o to decline')
response = input('> ')
if response.lower() == 'n' or response.lower() == 'no':
    print('OK. Maybe another time')


