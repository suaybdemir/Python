message = ' Hello There!'

message = message.upper()

print(message)

# Only first letter Upper!

message = message.capitalize()

print(message)

# Delet spaces which spanning in front of sentence

message = message.strip()

print(message)

# It is what it is
message = 'Hello There!'

message = message.split()

print(message)

message = '-'.join(message)

print(message)

index = message.find('There')
print(index)

# It will return bool
isFound = message.startswith('H')
print(isFound)


# It is what it is
message = 'Hello There!'


message = (message.replace('H','h')
           .replace('T','t')).replace(' ','')

print(message)

message = message.center(100,'*')

print(message)

