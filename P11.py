import math
states = int(input("Enter # possible states:"))
bits_needed = math.ceil(math.log(states, 2))

print(bits_needed)
