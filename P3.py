investment_per_rai = float(input("Investment (baht/rai): "))
rice_production_per_rai = float(input("Rice production (kg/rai): "))
wholesale_price_per_kwian = float(input("Wholesale price (baht/kwian): "))

income = rice_production_per_rai * (wholesale_price_per_kwian / 1000)

balance = income - investment_per_rai

print("Balance = income ({:,.2f}) - investment ({:,.2f}) = {:,.2f} baht/rai".format(
    income, investment_per_rai, balance
))
