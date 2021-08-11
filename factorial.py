# program to find factorial of number
n=int(input("Enter the number")) # n is variable is store the integer type value
fact=1 
for i in range(1,n+1): # for loop iterates multiplication 5 times
    fact=fact*i
print("Factorial of a  {0} is {1}".format(n,fact))