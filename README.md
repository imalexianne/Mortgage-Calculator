# Mortgage-Calculator
A mortgage calculator is a tool used to estimate mortgage payments for a home loan. It helps individuals or prospective homeowners calculate and understand the financial aspects of a mortgage, such as monthly payments, total interest paid, and loan amortization.
## Description
Kelly is an upcoming entrepreneur who is working on setting up 3 factories in the next month.
She discovers that she needs GHS 1,000,000 but unfortunately does not have that amount to begin the factories.
This happens to be a big blow in the business plans made by Kelly. Kelly being an industrious individual decides to still move on with the project.
She contacts her banker, and an agreement is made to offer her a loan to proceed with her project.
Kelly asks her banker the amount she has to pay each month to be able to settle the loan.
Now the banker has to develop a program to make the calculations.

## Example:

input

- mortgage loan principal

  principal = 100000

- percent annual interest

  interest = 7.5

- years to pay off mortgage

  years = 30


## Output

 
 result ...

For a 30-year mortgage loan of $100,000 at an annual interest rate of 7.50%  you pay


$699.21 monthly

 
----------------------------------------

 
Total amount paid will be $251,717.22



----------------------------------------

## Formula



M = P [ i(1 + i)^n ] / [ (1 + i)^n – 1]

M = Total monthly payment
P = The total amount of your loan
i = Your interest rate, as a monthly percentage
N = The total amount of months in your timeline for paying off your mortgage.


## Setup
Install the required packages to be able to run the evaluation locally.

You need to have [`Python 3`](https://www.python.org/) on your system (**a Python version lower than 3.10**). Then you can clone this repo and being at the repo's `root :: repository_name> ...`  follow the steps below:


- Windows *(Python should be added to the Path variable of environment)*:
        
        python3 -m venv venv; venv\Scripts\activate; python -m pip install --upgrade pip; python -m pip install -r requirements.txt  

- Linux & MacOs:
        
        python3 -m venv venv; source venv/bin/activate; python -m pip install --upgrade pip; python -m pip install -r requirements.txt

The both long command-lines have a same structure, they pipe multiple commands using the symbol **;** but you may manually execute them one after another.

1. **Create the Python's virtual environment** that isolates the required libraries of the project to avoid conflicts;
2. **Activate the Python's virtual environment** so that the Python kernel & libraries will be those of the isolated environment;
3. **Upgrade Pip, the installed libraries/packages manager** to have the up-to-date version that will work correctly;
4. **Install the required libraries/packages** listed in the `requirements.txt` file so that it will be allow to import them into the python's scripts and notebooks without any issue.
