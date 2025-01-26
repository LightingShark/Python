# Print first Prime number

a =  int(input())     # a variable  indicates no of input from the user 

for i in range ( a ):  # creating a loop to take no of input from the user
    Enter_the_number = int(input())  # enter the number 
    for j in range ( 1, Enter_the_number + 1 ):  # condition to check whether the entered number is prime number or not
        if Enter_the_number % j == 0:    # condition to find the factor for the entered number
            count += 1     # if the above condition satisfies count will increase  by one 
    if count == 2:    # if the count == 2 then it will come out of the loop
        break
print(Enter_the_number)   # print the first prime number  
