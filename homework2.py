from math import sqrt
import numpy as np

# This function calculate Fibonacci sequence
def fib(n):
	if n == 0 or n == 1:
		return 1
	else:
		return fib(n - 1) + fib(n - 2)

# This function calculate Lucas sequence
def lucas(n):
	if n == 0:
		return 2
	if n == 1:
		return 1
	else:
		return lucas(n - 1) + lucas(n - 2)

#This function transfer the result from Scientific counting method to float.
def format_float(num):
    return np.format_float_positional(num, trim='-')




def simulate_golden_rate():
	N = eval(input("Please enter N (>3): "))
	M = eval(input("Enter number of digits to be printed after decimal point (1>): "))
	F_n = fib(N)
	L_n = lucas(N)
	Golden_Ratio = (1 + sqrt(5)) / 2

	# Print Golden_Ratio and F_n and L_n
	print("Golden Ratio: " + str(Golden_Ratio))
	print("F_n: " + str(F_n) + "  L_n: " + str(L_n))
	
	F_err = round((abs(F_n / fib(N-1) - Golden_Ratio)),M)
	L_err = round((abs(L_n / lucas(N-1) - Golden_Ratio)),M)

	#Print the L_err and F_err
	print("L_err: " + str(L_err) + "    F_err: " + str(F_err) + '\n')
	
	#Print the digits after the decimal points
	print("The digits after decimal point for L_err (Least significant to Most significant):")
	print_digits_number(L_err,M)
	print("The digits after decimal point for F_err (Least significant to Most significant):")
	print_digits_number(F_err,M)

	
#This function helps calculate and print the digits after the decimal points
def print_digits_number(Num,M):
	Num_String = str(format_float(Num))[::-1]
	for i in range(0,M):
		print(Num_String[i])
	print('')
	
simulate_golden_rate()



	

