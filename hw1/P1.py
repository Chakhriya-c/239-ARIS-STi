distance = float(input("Enter distance (m): "))
spring_constant = float(input("Enter spring constant (N/m): "))

force = distance * spring_constant

print("The force is {:,.3f} N".format(force))