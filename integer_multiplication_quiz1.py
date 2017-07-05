# Recursive method for integer multiplication
# Basic Idea: We will divide the numbers into left and right halves (by number of digits), and recursively apply the multiply integers
# function. If one of the numbers is too small, zeroes will be appended to left to make the numbers have equal number of digits. 
def multiply_ints(num1, num2):
	#print num1, num2
	import sys
	# Base case
	if len(str(num1)) == 1 or len(str(num2)) == 1:
		return num1*num2
	else:
		ndigits1 = len(str(num1))
		ndigits2 = len(str(num2))
		n = max(ndigits2,ndigits1)
		
		# Take last n/2 digits of the num1 as 'b'
		b = int(str(num1)[-1*int(n/2):])
		# Take any remaining digits to the left of 'b' as 'a'. If no digits are remaining, we will assign 'a' to be zero. 
		if(ndigits1 > n/2):
			a = int(str(num1)[:-1*int(n/2)])
		else:
			a = 0

		# Take last n/2 digits of the num2 as 'd'
		d = int(str(num2)[-1*int(n/2):])

		# Take any remaining digits to the left of 'd' as 'c'. If no digits are remaining, we will assign 'c' to be zero. 
		if(ndigits2 > n/2):
			c = int(str(num2)[:-1*int(n/2)])
		else:
			c = 0
		
	return multiply_ints(b,d) + pow(10,int(n/2))*(multiply_ints(a,d)+multiply_ints(b,c)) + pow(10,2*int(n/2))*multiply_ints(a,c)

num1 = 3141592653589793238462643383279502884197169399375105820974944592
num2 = 2718281828459045235360287471352662497757247093699959574966967627

# Checking the algorithm against the built-in multiplication function in python
if(num1*num2 == multiply_ints(num1,num2)):
	print str(num1)+ ' * ' + str(num2) + ' = ' + str(multiply_ints(num1,num2))
else:
	print 'your program does not work: ' str(num1)+ ' * ' + str(num2) + ' != ' + str(multiply_ints(num1,num2))
else:
