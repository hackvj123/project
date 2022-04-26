cyan="\033[1;36;40m"
green="\033[1;32;40m"
red="\033[1;31;40m"
Y = '\033[1;33;40m'

def Main(a):
    if(a==1):
        from passtester import passtester
    elif(a==2):
        from HashIdentifier import identify_hashes
    elif(a==3):
        from lanscan_arp import lanscan
    elif(a==4):
        from nmap_port_scanner import nmaps
    elif(a==5):
        from ipicker import finder
    elif(a==6):
        from wifi_dos3 import wifi_dos
    elif(a==7):
        quit()
    else:
        return

def first():
    print(cyan+"""
    
  ______ ____    ____ .______    _______ .______           _______. _______   ______  __    __  .______       __  .___________.____    ____    .___________.  ______     ______    __      
 /      |\   \  /   / |   _  \  |   ____||   _  \         /       ||   ____| /      ||  |  |  | |   _  \     |  | |           |\   \  /   /    |           | /  __  \   /  __  \  |  |     
|  ,----' \   \/   /  |  |_)  | |  |__   |  |_)  |       |   (----`|  |__   |  ,----'|  |  |  | |  |_)  |    |  | `---|  |----` \   \/   /     `---|  |----`|  |  |  | |  |  |  | |  |     
|  |       \_    _/   |   _  <  |   __|  |      /         \   \    |   __|  |  |     |  |  |  | |      /     |  |     |  |       \_    _/          |  |     |  |  |  | |  |  |  | |  |     
|  `----.    |  |     |  |_)  | |  |____ |  |\  \----..----)   |   |  |____ |  `----.|  `--'  | |  |\  \----.|  |     |  |         |  |            |  |     |  `--'  | |  `--'  | |  `----.
 \______|    |__|     |______/  |_______|| _| `._____||_______/    |_______| \______| \______/  | _| `._____||__|     |__|         |__|            |__|      \______/   \______/  |_______|
                                                                                                                                                                                           
    """)
    print(cyan+""" Made by:- Vijay Shanbhag                                 
                             Abhishek Nalage                                
                             Ganesh Yadav                                   
                             Adarsh Devadiga                                
                             Kunal Thakur                                   
                     """)
                               
    print(green+"""
            Available Modules 
           
           1.Password Strength Tester.
           2.Hash Identifier.
           3.Lanscan.
           4.Port Scan.
           5.Iptracer.
           6.Wifi DOS.
           7.Quit
    """) 
    print(red+"Note : Lanscan requires an active lan/wlan connecetion.")
    print(red+"Note : Port Scan requires an active internet connection.")
    print(red+"Note : Iptracer requires an active internet connection. ")
    print(red+"Note : Wifi DOS requires a wlan card which supports monitor mode  ")
    
    inpt = 0
    while(inpt not in [1,2,3,4,5,6,7]):
        inpt=int(input(Y+"Module >> "))
    
    Main(inpt)
        

if __name__=="__main__":
    first()