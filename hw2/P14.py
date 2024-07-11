# DONE 
def laplace_smooth(count, param):
    prob = []
    for i in range(len(count)):
        laplace_eq = (count[i] + param) / (sum(count) + param * len(count))
        prob.append(laplace_eq)
    return prob