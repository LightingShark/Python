a = int(input())   # 1_st number
b = int(input())   # 2_st number
c = int(input())   # 3_st number

greatest_is_a = ( a > b) and ( a > c)   # if a is greater than b and c print(a)
if greatest_is_a:
    print(a)
elif ( b > c):                          # if b is greater than c print(b)
    print(b)
else:
    print(c)                            #else print(c)
