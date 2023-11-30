# Start of code.
# At the top of the file include the line import math.
import math
# Print the explanations of the two calculation options for the user.
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")
# Create a variable which gives the user a choice of two explanations.
# Ensure that if they user enters a capital word, it will not affect the output bu using the .lower function.
user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed:").lower()
# Create an if statement, for the investment user input.
if user_choice == "investment":
    # Ask the user to input the amount of money that they are depositing.
    principle_amount = float(input("How much money are you depositing?"))
    # Ask the user for the interest rate. Only the number should be entered.
    interest_rate = int(input("Enter the interest rate. Please enter just the number, without the percentage sign."))
    # Ask the user for the number of years they plan on investing.
    num_of_years = int(input("Please enter the number of years you want the investment deal to last"))
    # Ask the user to input whether they want simple or compound interest.
    interest_type = input("Would you like simple or compound interest?")
    # Interest rate will have to be divided by 100 for the interest mathematical formula.
    interest_rate /= 100
    # Create a viariable for interest type.
    # Create an if statement for the simple interest type from the user input.
    if interest_type == 'simple':
    # Create a total money variable and apply the mathematical formula for calculating simple interest.
        total_money = principle_amount *(1 + interest_rate * num_of_years)
    # elif used incase the user inputs compound for interest type.
    elif interest_type == 'compound':
    # Apply the compound interest mathematicul formula to our total money back variable.
        total_money = principle_amount * math.pow((1 + interest_rate),num_of_years)
    #Tell the user how much money they will get back in total after their investment deal finishes.
    print(f"You will recieve {total_money} in total.")
# Create an elif statement if the user inputs bond.
elif user_choice == "bond":
    # Ask the user for the present value of the house.
    house_value = float(input("What is the present value of the house"))
    # Ask the user for the interest rate. Only the number should be entered.
    interest_rate = int(input("Enter the interest rate. Please enter just the number, without the percentage sign."))
    # Ask the user for the number of months they plan to take to repay the bond.
    num_of_months = int(input("Please enter the number of months you plan to take to repay the bond"))
    # Monthly interest rate is calucalted by dividing the annual interest rate by 12.
    monthly_interest = (interest_rate / 100) / 12
    # Create a repayment variable and apply the mathematical formula for calculating bond repayment.
    repayment = (monthly_interest * house_value) / (1 - (1 + monthly_interest)**(- num_of_months))
    # Print the total amount the user will have to repay each month
    print(f"You will have to repay {repayment} each month.")
# Create an else statement incase an invalid input is entered.
else:
    # Remind the user of the correct choices.
    print("This is not an option. Please choose either bond or investment.")

# End of code.