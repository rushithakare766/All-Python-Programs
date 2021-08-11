# program to print inverted half pyramid in python 
'''
* * * * *
* * * *
* * *
* *
*
'''
# take input as rows from user 
rows = int(input("Enter the number of rows: "))  
# the outer loop is executing in reversed order  
for i in range(rows + 1, 0, -1):   
    # nested loop  
    for j in range(0, i - 1):  
        #print star 
        print("*", end=' ')  
    print(" ")  