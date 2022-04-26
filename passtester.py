cyan="\033[1;36;40m"
green="\033[1;32;40m"
print(cyan+""" ╔════╗──────╔╗─╔╗────╔═╗╔═╗──╔╗
 ║╔╗╔╗║──────║║─║║────║║╚╝║║──║║
 ╚╝║║╠╩╦══╦╗╔╣╚═╣║╔══╗║╔╗╔╗╠══╣║╔╦══╦═╦══╗
 ──║║║╔╣╔╗║║║║╔╗║║║║═╣║║║║║║╔╗║╚╝╣║═╣╔╣══╣
 ──║║║║║╚╝║╚╝║╚╝║╚╣║═╣║║║║║║╔╗║╔╗╣║═╣║╠══║
 ──╚╝╚╝╚══╩══╩══╩═╩══╝╚╝╚╝╚╩╝╚╩╝╚╩══╩╝╚══╝""")
print("\n*****************************************************************")
print("\n* Team Members:- Vijay Shanbhag                                 *")
print("\n*                Abhishek Nalage                                *")
print("\n*                Ganesh Yadav                                   *")
print("\n*                Adarsh Devadiga                                *")
print("\n*                Kunal Thakur                                   *")
print("\n*****************************************************************")
print(green+"")
import re
def passtester():
    password=(input("Enter Password for testing:-"))
    flag = 0
    while True:
        if (len(password)<8):
            flag = 1
            print("Password length should be more than 8.")
            break
        elif not re.search("[a-z]", password):
            flag = 1
            print("Password should consist atleast one lowercase letter.")
            break
        elif not re.search("[A-Z]", password):
            flag = 1
            print("Password should consist one uppercase letter.")
            break
        elif not re.search("[0-9]", password):
            flag = 1
            print("Password should consist atleast one number.")
            break
        elif not re.search("[@$#%^&!]", password):
            flag = 1
            print("Password should consist atleast one special character.")
            break
        elif re.search("\s", password):
            flag = 1
            print("Password should not have spaces.")
            break
        else:
            flag = 0
            print(password,":This password is suitable for use")
        response = input("If you want to go to main program press 'y', for restarting the program press 'n'  ? (y/n): ")
        if response.lower() == "y":
            import cstool
            cstool.first()
        elif response.lower() == "n":
            passtester()
            break

    if flag == 1:
        print(password,":Password not suitable for use")
        response = input("Do you want to go to the main program ? (y/n): ")
        if response.lower() == "y":
            import cstool
            cstool.first()
       

        else:
            passtester()

passtester()