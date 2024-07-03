angle = float(input("Angle (degree): "))
distance = float(input("Distance (km): "))

circumference = 360 * distance / angle

print('Eratosthenes: "The Earth circumference is about {:,.2f} km."'.format(circumference))
