ball_spd = float(input("Enter the ball speed (km/h):"))
court_length = float(input("Enter the court length (m):"))
ball_weight = float(input("Enter the ball weight (g):"))

ball_spd_ms = ball_spd / 3.6

time = 2* court_length / ball_spd_ms

ball_weight_kg = ball_weight / 1000

acc = (ball_spd_ms ** 2) / (2 * court_length)

force = ball_weight_kg * acc

energy = force * court_length

energy_cal = energy / 4.184

print("Time = {:.4f} s. Energy = {:.2f} J = {:.2f} cal".format(time, energy, energy_cal))
