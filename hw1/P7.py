angle = float(input("Angle (degree): "))
distance = float(input("Distance (km): "))

circumference = 360 * distance / angle

print('Eratosthenes: "the earth circumference is about {:,.1f} km."'.format(circumference))
