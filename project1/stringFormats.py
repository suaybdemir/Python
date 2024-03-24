name = 'Suayb'
lastName = 'Demir'

print('My name is {s} {n}'.format(n=name,s=lastName))

result = 1/3

print('result {r:1.4}'.format(r=result))

print('result {r:8.4}'.format(r=result))

print('result {r:1.4}'.format(r=result))

print(f'My name is {name} {lastName}')

s = 'Hello world'

print(s)

s = s[0:6] + 'W' + s[-4:]

print(s)

# Swap w with W
s.replace('w','W')

print(s)

m = s[:-3]

print(m)

# Reverse Printing

m = s[::-1]

print(m)
