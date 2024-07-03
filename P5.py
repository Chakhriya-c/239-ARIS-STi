import math

impact_duration = float(input("Impact duration (s): "))
effective_weight = float(input("Effective weight (kg): "))
effective_lenght = float(input("Impact lenght (m): "))
blow_exec = float(input("Blow execution time (s): "))

ang_velocity = (2 * math.pi) / blow_exec 
impact_velo = ang_velocity * effective_lenght
impact_force = (effective_weight * impact_velo) / impact_duration

print ("v = {:,.2f} km/h = {:,.2f} mph".format(impact_velo * 3.6, impact_velo * 2.23694))
print ("f = {:,.2f} N = {:,.2f} lbf".format(impact_force, impact_force / 4.45))