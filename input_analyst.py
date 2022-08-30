"""
get an input from the user
analyst the input:
1) if it number or string
2)if it a number how much digit (len), if the number even or odd and if number%7 == 0?
if its a string to dont do anythng 
"""

def input_analyst_from_the_user ():
    """we check if its a num, if its a num - we do all the next requirements, 
            if its not a num- we print its a string"""
    user_input = input("please enter here, string or num:")
    if user_input.isdigit() == True: 
            print ("the user input is a int")
            print (f"the len numbers is {len(user_input)}")
            if (int(user_input) % 2 ) == 0: 
                print ("the user choose an even num")
            else:
                print ("the user choose an odd num ")
            if (int(user_input) % 7) == 0:
                print ("the user input's number is divisible 7 - without remainder")
            else:
                print ("the user input's number divisible 7 - with remainder")
    else: 
        print ("the user input is a string")

def main():
    input_analyst_from_the_user()


if __name__ == "__main__":
    main()