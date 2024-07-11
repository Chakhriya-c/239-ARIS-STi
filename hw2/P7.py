# DONE 

import math

x = float(input("x:"))
m = int(input("M:"))

sin_x = 0

for i in range(m):
    sin_x += ((-1)**i * x**(2*i + 1)) / math.factorial(2*i + 1)

print(f"sin({x:.2f}) = {sin_x:.5f}")
