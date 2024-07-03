import math

drag_coef = float(input("CD: "))
lift_coef = float(input("CL: "))
air_den = float(input("air density: "))
cross_sec = float(input("cross-section area: "))
wing_area = float(input("wing area: "))
plane_weight = float(input("plane weight: "))

cruising_spd = math.sqrt((2 * plane_weight * 9.8) / (lift_coef * air_den * wing_area))
drag = drag_coef * (0.5 * air_den * (cruising_spd ** 2) * cross_sec)
power = drag * cruising_spd

print ("power = {:,.2f} W. = {:,.2f} hp.".format(power, power * 0.00136))