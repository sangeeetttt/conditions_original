'''
if the name is less than 3 char,
its a short name!
if the name is more than 50 chars,
its a long name!
otherwise
Damnnnn, you've got a nice name.

'''

name = str(input('Enter your Name: '))
if len(name)<3:
    print(f'its a short name!')
elif len(name)>50:
    print(f'its a long name!')
else:
    print(f'Damnnnn! its a fine name')