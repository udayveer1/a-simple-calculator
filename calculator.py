user_input_1 = int(input("enter a number"))

user_input_2 = int(input("enter another a number"))

operator = input("enter a operator(+, -, /, *)")

added_value = user_input_1 + user_input_2
subtracted_value = user_input_1 - user_input_2
multiplied_value = user_input_1 * user_input_2
divided_value = user_input_1 / user_input_2
if operator == "+":
    print(f"the output is going to be: {added_value} ")

elif operator == "-":
    print(f"the output is going to be: {subtracted_value}")

elif operator == "/":
    print(f"the output is going to be: {divided_value}")

elif operator == "*":
    print(f"the output is going to be: {multiplied_value}")

else:
    print("invalid syntax")
    print("please input an correct  operator")
