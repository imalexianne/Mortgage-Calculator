#Declaration of variables,

total_loan = int(input('Enter total loan')) # Total amount of requested loan
interest_rate = float(input('Enter interest_rate')) #7.5% of interest per year
loan_term = int(input('Enter loan_term')) # 30 years of paying a loan


#calculation of loan interest for each month
interest_per_month = interest_rate /12
loan_term_months = loan_term * 12

#calculation of monthly payment
total_monthly_payment = total_loan * (interest_per_month*(1 + interest_per_month)**loan_term_months) / ((1 + interest_per_month)**loan_term_months - 1)
#calculation of total payment
Total_amount_paid = total_monthly_payment * loan_term_months
#formulating the the total payment
Formatted_Total_amount_paid = "$ {:,.2f}".format(Total_amount_paid)

print( "Monthly Payment will be: $",format(total_monthly_payment,".2f") + " Monthly")
print("Total amount paid Will be: ",Formatted_Total_amount_paid)