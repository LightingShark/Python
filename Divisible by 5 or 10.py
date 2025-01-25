a = int(input())

check_1 = ( a % 10)      
remainder_10 = (check_1 == 0)    # if the remainder == 0 ......entered number is divisible by 10 

check_2 = ( a % 5)
remainder_5 = (check_2 == 0)     # if the remainder == 0 ......entered number is divisible by 5 

# if the given condition satisfies it will print the below statement
if remainder_10:   
    print("Divisible by 10")
elif remainder_5 :
    print("Divisible by 5")
else:
    print("Not Divisible by 10 or 5")
