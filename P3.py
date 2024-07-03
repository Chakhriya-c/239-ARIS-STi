investment = int(input("Investment (baht/rai): "))
rice_production = int(input("Rice production (kg/rai): "))
whole_sale = int(input("Wholesale price (baht/kwian): "))
income = rice_production * (1/1000) * whole_sale
print("Balance = income ({:,.2f}) - investment({:,.2f}) = {:,.2f} bath/rai".format(income, investment, income-investment))
