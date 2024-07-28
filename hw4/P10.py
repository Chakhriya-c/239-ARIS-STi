import numpy as np

class Face:
    def __init__(self, A, B, C, col=(128, 128, 128)):
        self.A = A
        self.B = B
        self.C = C
        self.color = col
        AB = B - A
        AC = C - A
        self.normal = np.cross(AB, AC).astype(float)
        self.normal /= np.linalg.norm(self.normal)  

    def ray(self, O, V):
        k = np.dot(self.normal, self.A)
        denom = np.dot(self.normal, V - O)
        if abs(denom) < 1e-6: 
            return np.inf
        t = (k - np.dot(self.normal, O)) / denom

        if t < 0:
            return np.inf  

        Q = O + t * (V - O)
        
        def sign_test(p1, p2, p3):
            return np.dot(np.cross(p2 - p1, Q - p1), self.normal) >= 0
        
        if (sign_test(self.A, self.B, Q) and
            sign_test(self.B, self.C, Q) and
            sign_test(self.C, self.A, Q)):
            return t
        else:
            return np.inf 

