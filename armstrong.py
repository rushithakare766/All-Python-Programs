# program to check given number is amstrong or not
num=int(input("Enter the number:")) # num variable is used to store integer type value
originalnum=num #we have assign originalnum to num 
res=0 #we have assign result variable to 0
rem=0 #we have assign remainder variable to 0
while num>0:
    rem=num%10 
    res=res+rem*rem*rem
    num=num//10
if originalnum==res: # this condition check that original no is equal to result or not
    print("This is a armstrong number")
else:
    print("THis is not a armstrong number")   

