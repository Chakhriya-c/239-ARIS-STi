import numpy as np

class Sphere:
    def __init__(self, C, r, col=(128,128,128)):
        self.C = C
        self.r = r
        self.color = col

    def ray(self, O, V):
        a = np.dot(V - O, V - O)
        b = 2 * np.dot(O - self.C, V - O)
        c = np.dot(O - self.C, O - self.C) - self.r ** 2

        discriminant = b ** 2 - 4 * a * c

        if discriminant < 0:
            return np.inf
        elif discriminant == 0:
            t = -b / (2 * a)
            return t
        else:
            t1 = (-b - np.sqrt(discriminant)) / (2 * a)
            t2 = (-b + np.sqrt(discriminant)) / (2 * a)
            if t1 >= 0:
                return t1
            elif t2 >= 0:
                return t2
            else:
                return np.inf