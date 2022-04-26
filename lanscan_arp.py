import scapy.all as scapy
import re


print("""
╔════╗──────╔╗─╔╗────╔═╗╔═╗──╔╗
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

def lanscan():
    ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")

    while True:
        ip_add_range_entered = input("\nPlease enter the ip address and range that you want to send the ARP request to (ex 192.168.1.0/24): ")
        if ip_add_range_pattern.search(ip_add_range_entered):
            print(f"{ip_add_range_entered} is a valid ip address range")
        break


    arp_result = scapy.arping(ip_add_range_entered)
    A=input("do you want to go to main program(y/n):")
    if (A == y):
        import cstool
        cstool.first()
    elif (A == n):
        lanscan()
    else:
        quit()

    


lanscan()
