#!/usr/bin/env python3

# Created By: Spencer Scarlett
# Date: Dec 18, 2022
# A program which calculations two numbers using a inputted sign (+, -, * etc)


# Function to perform the calculation
def calculate(sign, first_number, second_number):
    if sign == "+":
        return first_number + second_number
    elif sign == "-":
        return first_number - second_number
    elif sign == "*":
        return first_number * second_number
    elif sign == "/":
        return first_number / second_number
    elif sign == "%":
        return first_number % second_number


def main():
    # inputs for sign, first and second numbers
    user_sign = input("Enter a sign to use in calculation: ")
    user_first_number = input("Enter first number: ")
    user_second_number = input("Enter second number: ")

    # converts first and second number to floats
    try:
        first_number_flo = float(user_first_number)
        second_number_flo = float(user_second_number)
        # checks user_sign for invalid inputs
        if (
            user_sign == "+"
            or user_sign == "-"
            or user_sign == "*"
            or user_sign == "/"
            or user_sign == "%"
        ):
            # calls function
            results = calculate(user_sign, first_number_flo, second_number_flo)

            # displays function
            print(f"{first_number_flo} {user_sign} {second_number_flo} = {results}")
        else:
            # for invalid inputs for sign
            print(f"{user_sign} is a invalid sign, use +, -, *, /, % only!")

    except Exception:
        # for invalids number inputs (strings)
        print("Invalid inputs, use numbers only!")


if __name__ == "__main__":
    main()
