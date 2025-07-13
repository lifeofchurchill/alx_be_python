monthly_income = input('Enter your monthly income: ')
monthly_expenses = input('Enter yot total monthly expenses: ')

monthly_savings = int(monthly_income) - int(monthly_expenses)
print(f"your monthly savings are ${monthly_savings}")
interest = 0.05

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * interest)
print(f"Projected savings after one year, with interest is: ${projected_savings}")