r = int(input("R Channel[0-255]: "))
g = int(input("G Channel[0-255]: "))
b = int(input("B Channel[0-255]: "))

print ("Y = {}".format(int((0.2126 * r) + (0.7152 * g) + (0.0722 * b))))