def calc_energy(mass, speed, time):
    acceleration = speed / time
    
    force = mass * acceleration
    
    displacement = 0.5 * acceleration * (time ** 2)
    
    energy = force * displacement
    
    return energy, displacement

g = lambda f: f(float(input('object mass:')),
float(input('target speed:')),
float(input('time spent:')))
print("Energy = %.2f J. Distance = %.2f m."%g(calc_energy))