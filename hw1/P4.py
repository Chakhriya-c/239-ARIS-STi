import math

velocity = float(input("Plane speed (mph):"))
interval = float(input("Interval between crash and the last contact (h):"))

search_radius = velocity * interval
search_area = math.pi * (search_radius ** 2)

thailand_sq_mi = 198120

print("Search area = {:,.2f} sq.mi.".format(search_area))
print("That's {:.2f} time(s) the size of Thailand.".format(search_area / thailand_sq_mi))
