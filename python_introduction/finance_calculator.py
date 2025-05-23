monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: ")) 
monthly_savings = monthly_income - monthly_expenses

Projected_savings = int(monthly_savings * 12 + monthly_savings * 12 * 0.05)
print('Projected savings after one year, with interest, is: ' + str(Projected_savings))