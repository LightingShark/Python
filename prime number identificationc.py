#Write a Python program that identifies all prime numbers from an input number and its individual digits.

entered_number = int(input())

actual_number_list = [entered_number]
entered_number = str(entered_number)

new_list_of_number = []
for each_char in entered_number:
    new_list_of_number.append(each_char)
for char in range(len(new_list_of_number)):
    new_list_of_number[char] = int(new_list_of_number[char])
new_list_of_number.extend(actual_number_list)   


def find_prime_number(new_list_of_number):
    result = []
    for i in range(len(new_list_of_number)):
        number = new_list_of_number[i]
        counter = 0
        for j in range ( 1, number + 1 ):
            if number % j == 0:
                counter += 1
        if counter == 2:
            result.append(number)
    return result        

result = find_prime_number(new_list_of_number)

if result == []:
    print("No prime number found")
else:    
    for k in range(len(result)):
        print((result[k]), end = " ")
    print()
