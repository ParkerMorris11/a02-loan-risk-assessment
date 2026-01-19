
# Name: Parker Morris
# Loan Risk Assessment
# input variables
name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
income = float(input("Enter your annual income in dollars: "))
debt = float(input("Enter your total monthly debt payments in dollars: "))

DTI = debt / (income / 12)

if DTI < 0.20: # find category of risk with if statement
    category = "Low risk"
elif DTI < 0.36:
    category = "Moderate risk"
elif DTI < 0.50:
    category = "Elevated risk"
else:
    category = "High risk"
# output results
print(f"{name} {last_name} has a DTI of {DTI:.2f}. The associated category is: {category}.")