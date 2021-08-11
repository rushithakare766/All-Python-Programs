#Print equilateral triangle Pyramid using asterisk symbol 
'''
            *   
           *  *   
          *  *  *   
         *  *  *  *   
        *  *  *  *  *   
       *  *  *  *  *  *   
      *  *  *  *  *  *  * 
      '''
# take rows as input from user
rows = int(input("Enter the number of rows:"))
m = (2 * rows) - 2
# iterates for loop on rows and coloumns 
for i in range(0, rows):
    for j in range(0, m):
        print(end=" ")
    # decrementing m after each loop
    m = m - 1
    for j in range(0, i + 1):
        print("* ", end=' ')
    print(" ")