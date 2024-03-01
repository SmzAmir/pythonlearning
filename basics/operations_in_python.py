# Operation Types in Python
# addition -> +
# subtraction -> -
# multiplication -> *
# division -> / (gives you a float)
# integer division -> // (gives you an integer)
# power -> x ** y or pow(x, y)
# remainder -> %

x1 = 5
x2 = 2
print(x1 // x2)
print(x1 % x2)

# You have a three digits number 589,
# use // and % to reverse the number -> 985
my_number = 589
digit_1 = 589 % 10
print(digit_1)
remainder_1 = 589 // 10
# print(remainder_1)
digit_2 = remainder_1 % 10
digit_3 = remainder_1 // 10
print(digit_2)
print(digit_3)

reverse_number = (digit_1 * 100) + (digit_2 * 10) + digit_3
# reverse_number =  (900) + (80) + 5
print(reverse_number)