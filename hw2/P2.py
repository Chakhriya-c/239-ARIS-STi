# DONE 
def ch4combus(ch4_weight, oxygen_weight):
    molecular_weight_ch4 = 12.011 + 4 * 1.008
    molecular_weight_oxygen = 2 * 15.999

    moles_ch4 = ch4_weight / molecular_weight_ch4
    moles_oxygen = oxygen_weight / molecular_weight_oxygen

    if moles_ch4 <= moles_oxygen / 2:
        moles_coxygen = moles_ch4
        moles_h2o = 2 * moles_ch4
        remaining_ch4 = 0
        remaining_oxygen = oxygen_weight - moles_ch4 * 2 * molecular_weight_oxygen
    else:
        moles_co2 = moles_oxygen / 2
        moles_h2o = moles_oxygen
        remaining_ch4 = ch4_weight - moles_oxygen / 2 * molecular_weight_ch4
        remaining_oxygen = 0

    molecular_weight_co2 = 12.011 + 2 * 15.999
    molecular_weight_h2o = 2 * 1.008 + 15.999

    weight_co2 = moles_co2 * molecular_weight_co2
    weight_h2o = moles_h2o * molecular_weight_h2o

    print(f"CH4: {remaining_ch4:.2f} g. O2: {remaining_oxygen:.2f} g. CO2: {weight_co2:.2f} g. H2O: {weight_h2o:.2f} g")

ch4_weight = float(input("Methane (CH4, in g): "))
oxygen_weight = float(input("Oxygen (O2, in g): "))
ch4combus(ch4_weight, oxygen_weight)
