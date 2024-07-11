# DONE 
def collect_data():
    observ_list = []
    nums = []
    while True:
        observed = str(input("Observation:"))

        if observed != "":
            counting = int(input("Found:"))
            observ_list.append(observed)
            nums.append(counting)
        else :
            break
    
    return observ_list, nums
