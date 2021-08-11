# program to print pyramid pattern  
'''
* 
* * 
* * * 
* * * * 
* * * * * 
''' 
# take input as rows from user 
rows = int(input("Enter  the number of rows: "))
# outer loop 
for i in range(rows):
    # nested loop
    for j in range(i+1):
        # print star 
        print("* ", end="")
    print("\n")