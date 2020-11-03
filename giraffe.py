i = 1
while i <= 10:
    print(i)
    i = i + 1

print('end of the while loop')

# building a secret word

word = 'jackpot'
guess = ''
while guess != word:
    guess = input('Guess the correct word: ').lower()
print('Congratulations. You guessed right.')

"""
 DEFINING VARIABLES -
    case sensitive,
    must start with a letter or underscore,
    can contain numbers but they can not be at the start.
"""

"""
Multiple Assignment

"""
name, age, gender = ('Mike Doe', 44, 'Male')
add = age + age
print(name, age, gender, add)
print(type(add))

print(f'{add} is of type {type(float(add))}')
print(212 - 20)
print('Something magical is happening')


def hello_world(name='Mike Mundu'):
    return f'Hello {name}'


h = hello_world('James Doe')
print(h)
