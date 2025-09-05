# This function calculates the allocation of income based on the 50/30/20 rule
# and applies a tax deduction if the income is from an Uber source.
def allocation(income, uber):
    """
    Calculates the allocation of income into different categories.
    
    Args:
        income (float): The total income amount.
        uber (bool): True if the income is from Uber, False otherwise.
        
    Returns:
        tuple: A tuple containing the allocations for tax, essentials, savings, and spending.
    """
    essentials_percentage = 0.5
    savings_percentage = 0.3
    spending_percentage = 0.2
    
    # Determine the tax percentage based on whether it's Uber income
    uber_tax = 0.25 if uber else 0.0
    
    tax_allocation = uber_tax * income
    remaining_income = income - tax_allocation
    
    essentials_allocation = essentials_percentage * remaining_income
    savings_allocation = savings_percentage * remaining_income
    spending_allocation = spending_percentage * remaining_income

    return (tax_allocation, essentials_allocation, savings_allocation, spending_allocation)

if __name__ == "__main__":
    calculate_again = True
    while calculate_again:
        
        # Input validation for income
        while True:
            try:
                income = float(input("Enter your income: "))
                if income < 0:
                    print("Please enter a positive income value.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number for your income.")
        
        # Input validation for Uber income
        while True:
            uber_input = input("Is this an Uber income? (yes/no): ").strip().lower()
            if uber_input in ['yes', 'no']:
                uber = (uber_input == 'yes')
                break
            else:
                print("Invalid input. Please answer 'yes' or 'no'.")

        tax, essentials, savings, spending = allocation(income, uber)

        print(f"\n--- Income Breakdown ---")
        print(f"Tax Allocation: £{tax:.2f}")
        print(f"Essentials Allocation: £{essentials:.2f}")
        print(f"Savings/Debt Allocation: £{savings:.2f}")
        print(f"Spending Allocation: £{spending:.2f}")
        print(f"------------------------\n")

        # Input validation for calculating again
        while True:
            again_input = input("Do you want to calculate again? (yes/no): ").strip().lower()
            if again_input in ['yes', 'no']:
                calculate_again = (again_input == 'yes')
                break
            else:
                print("Invalid input. Please answer 'yes' or 'no'.")