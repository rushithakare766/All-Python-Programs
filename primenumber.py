# program to check the enter number is prime or not
num=int(input("Enter the number:"))
if num>1:#  this condition is true then control goes into for loop
    for i in range(2,num):# this for loop run from 2 to num-1
        if num%i==0: # this condition is true when num is divisble by i and remainder is 0
            print(num,"is not a prime number")
            break 
    else:
        print(num,"is a prime number")
else:
    print(num,"is not a prime number")       