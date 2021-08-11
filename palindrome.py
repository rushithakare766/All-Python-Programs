# program to check number is palindrome or not
num=int(input("Enter the number:")) # num variable is store the integer type value
originalnum=num #we have assign originalnum to num 
rev=0 #we have assign result variable to 0
rem=0 #we have assign remainder variable to 0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
if originalnum==rev: # this condition check that original no is equal to reverse or not
    print("The number is palindrome")
else:
    print("The number is not palindrome")
