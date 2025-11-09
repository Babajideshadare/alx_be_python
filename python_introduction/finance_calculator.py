# calculating the user’s monthly savings based on inputted monthly income and expenses.
monthly_income = float(input("Enter your montly income: "))
monthly_expenses = float(input("Enter your monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
projected_savings = (monthly_savings * 12 +(monthly_savings * 12 * 0.05)) # adding 5% annual interest
print("Your monthly savings are:", monthly_savings) 
print("Projected savings after one year, with interest is:", projected_savings)