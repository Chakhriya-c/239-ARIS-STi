import math
velocity = float(input("Plane speed (mph): "))
interval = float(input("Interval between crash and the last contact (h): "))

search_area = math.pi * ((velocity * interval)**2)

print("Search area {:,.2f} sq.mi.".format(search_area))
print("That's {:.2f} time(s) the size of Thailand.".format(search_area/198120))