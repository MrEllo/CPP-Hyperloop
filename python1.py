# Hello World!
# print("Hello World!")

# Get input from user, print it out onto terminal (Concatenation)
'''
userinput = input()
print("You said: " + userinput)
print(f"You said: {userinput}")
'''

# I am buying 32 oranges, 5 apples, an 4 bananas at the store
'''
numoranges = 32
numapples = 5
numbananas = 4

print(f"I am buying {numoranges} oranges, {numapples} apples, and {numbananas} bananas at the store.")
'''


# Integers are whole numebrs! They can be negative
sampleint = -1


# Doubles  are decimal numbers! They can also be negative
sampledouble = 6.32125231643

# Strings
samplestring = "This is a string!"

# Booleans (Different states - False or True)
samplebool = False

# List (1st number is 0, 2nd is 1, etc) Putting a negative when printings means going backwards on list
samplelist = [34, 165, 452, 2333, 54, 45]
try:
    print(samplelist[10])
except Exception as e:
    print(f"What's wrong?: {e}")
print(f"length of samplelist: {len(samplelist)}")



