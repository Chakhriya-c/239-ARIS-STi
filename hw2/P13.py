# DONE 
def est_prob(counting):
    prob = []
    for i in range(len(counting)):
        prob.append(counting[i]/sum(counting))
    return prob