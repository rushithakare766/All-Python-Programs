# program to check given year is leap or not
year=int(input("Enter the year:"))
if year%4==0: # when this condition is true then control goes to another if statement
    if year%100==0: # when this condition is true then control goes to another if statement
        if year%400==0: # when this is true then print statement will excecute 
            print(year,"is a leap year")
        else:
            print(year,"is not a leap year")
    else:
        print(year,"is a leap year") # this else blocks for if year%100==0
else:
    print(year,"is not a leap year")  # this else blocks for if year%400==0          
