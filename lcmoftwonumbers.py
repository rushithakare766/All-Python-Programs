# lcm of two numbers
num1=int(input("Enter the number 1:"))
num2=int(input("Enter the number 2:"))
if (num1>num2): # use if condition to find greatest among two numbers
    maximum=num1
else:
    maximum=num2
while(True): # this loop runs until the condition is true
    if (maximum % num1==0 and maximum% num2==0): 
        print(maximum)
        break
    maximum=maximum+1



