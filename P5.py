import math

impact_duration = float(input("Impact duration (s): "))
effective_weight = float(input("Effective weight (kg): "))
effective_length = float(input("Effective length (m): "))
blow_execution_time = float(input("Blow execution time (s): "))

angular_velocity = (2 * math.pi) / blow_execution_time
impact_velocity = angular_velocity * effective_length
impact_force = (effective_weight * impact_velocity) / impact_duration

impact_velocity_kmh = impact_velocity * 3.6
impact_velocity_mph = impact_velocity_kmh * 0.62111801242

print("v = {:,.2f} km/h = {:,.2f} mph".format(impact_velocity_kmh, impact_velocity_mph))
print("f = {:,.2f} N = {:,.2f} lbf".format(impact_force, impact_force / 4.45))
