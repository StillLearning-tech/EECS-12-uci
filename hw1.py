def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")

    principal = eval(input("Enter the initial investment: "))
    qcr = eval(input("Enter the quarterly compounded interest rate (less than 1): "))
    qir = eval(input("Enter the quarterly investment rate (less than 1): "))
    invest_per_quarter = principal * qir
    quarterly_rate = qcr / 4

    for i in range(10):
        principal = year_balance_calc(principal, quarterly_rate, invest_per_quarter)

        print("The balance after", i, "year is", principal)

    print("The value in 10 years is:", principal)

# calculate a new principal for one year
def year_balance_calc(principal, quarterly_rate, invest_per_quarter):
    for i in range(4):
        principal = principal * (1 + quarterly_rate) + invest_per_quarter
    return principal

main( )