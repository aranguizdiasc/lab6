
def menu():
    print()
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()

def pass_encode(password):
    pass

if __name__ == "__main__":
    while True:
        # print all the menu options
        menu()
        # prompt the user for menu option
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")

            pass
        elif option == 3:
            break

