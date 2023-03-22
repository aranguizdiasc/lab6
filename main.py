
def menu():
    print()
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()

def pass_encode(password): # “00009962” will become “33332295” after encoding
    new_pass = ""
    for num in password[0:]:
        new_digit = str(int(num) + 3)
        new_pass += new_digit[-1]
    return new_pass

if __name__ == "__main__":
    while True:
        # print all the menu options
        menu()
        # prompt the user for menu option
        option = int(input("Please enter an option: "))
        if option == 1: # encode
            password = input("Please enter your password to encode: ")
            encoded_pass = pass_encode(password)
            print("Your password has been encoded and stored!")
            print(encoded_pass)

        if option == 2: # decode
            pass

        elif option == 3: # quit
            break

