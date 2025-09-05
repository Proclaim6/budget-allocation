Budget Allocation Calculator
This is a simple Python script that helps you manage your finances using the 50/30/20 budget rule. It's a command-line tool that calculates how to allocate your income into different categories: Essentials, Savings/Debt, and Spending. It also includes an optional tax deduction for Uber-related income.

Features
50/30/20 Rule: Allocates your post-tax income into:

50% for Essentials (needs)

30% for Savings/Debt (financial goals)

20% for Spending (wants)

Uber Tax Deduction: Applies a 25% tax deduction if the income is specified as being from an Uber source, before applying the 50/30/20 rule.

Interactive Command-Line Interface: Prompts you to enter your income and specify if it's from Uber, then displays a clear breakdown of the allocations.

Input Validation: Ensures that the income you enter is a valid number and that your responses are in the correct format.

Getting Started
Prerequisites
You need to have Python 3 installed on your machine to run this script. You can download it from the official Python website.

How to Run
Clone the repository (if you haven't already):

git clone [https://github.com/Proclaim6/budget-allocation.git](https://github.com/Proclaim6/budget-allocation.git)

Navigate to the project directory:

cd budget-allocation

Run the script:

python budget_allocation.py

(Note: If you have a different name for your file, replace budget_allocation.py with your filename).

Example Usage
When you run the script, you will be prompted to enter your income and answer a simple question.

Enter your income: 1000
Is this an Uber income? (yes/no): yes

--- Income Breakdown ---
Tax Allocation: £250.00
Essentials Allocation: £375.00
Savings/Debt Allocation: £225.00
Spending Allocation: £150.00
------------------------

Do you want to calculate again? (yes/no): no

How the Code Works
The core logic is within the allocation() function, which takes your income and a boolean (uber) to determine if the tax deduction should be applied. The main part of the script (if __name__ == "__main__":) handles the user input, validation, and output display in a loop, allowing you to perform multiple calculations.

Contributing
Feel free to open an issue or submit a pull request if you have suggestions for new features or improvements.
