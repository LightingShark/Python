# write a program to print the sum of N number of values entered by the user

N = int(input())
counter = 0        # Initializing a counter to control the while loop
sum_of_number = 0  # creating a temp variable to store the sum of of the N number of values

while counter < N:  # loop header
  # conditional statement 
    number = int(input())     # take the input has number from the user
    sum_of_number = sum_of_number + number   # add the number which is entered by the user
    counter = counter + 1    # incerase the counter value by 1 after each iteration
    
print(sum_of_number)   # print the sum of N numbers
