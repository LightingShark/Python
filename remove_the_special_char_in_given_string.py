enter_the_string = input()     # take the input string from the user
special_character = "!@#$%^&*()_+-=[]<>,.?/@"

updated_string = ""
for each_char in enter_the_string:    # itrating each char from the input string
    if each_char in special_character:   # checking each char in string Whether it is present in the special_character or not
        continue      # if present in the special_character continue
    else:
        updated_string += each_char  # update the each_char in the updated_string

print(updated_string)  
