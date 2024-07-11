# DONE 
cad_obst = str(input("Is CAD obstructive (yes/no)? "))

if cad_obst == "no" : 
    print ("Non-obstructive CAD.")
    print ("TAVI alone.")

elif cad_obst == "yes" :
    print ("Obstructive CAD.")
    large = str(input("Is area of myocardium at risk large (yes/no)? "))

    if large == "no" :
        print ("Small area of myocardium at risk.")
        print ("Consider TAVI first, then ischemia-driven revascularization.")

    elif large == 'yes':
            print("Large area of myocardium at risk.")
            caro_stenosis = float(input("How is coronary stenosis (%)? "))

            if caro_stenosis > 75 :
                print("Severe CAD.")
                print("Staged upfront or concomitant PCI and TAVI.")

            elif caro_stenosis <= 75 :
                print ("Moderate CAD.")
                print("Consider TAVI first, then CAD functional assessment.")
