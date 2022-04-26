import json
import urllib.request
import webbrowser
import os
try:
    path=os.path.isfile('/data/data/com.termux/files/usr/bin/bash')
    def start():
        os.system('clear')



    def m3():
        try:
            print("""\n
╔════╗──────╔╗─╔╗────╔═╗╔═╗──╔╗
║╔╗╔╗║──────║║─║║────║║╚╝║║──║║
╚╝║║╠╩╦══╦╗╔╣╚═╣║╔══╗║╔╗╔╗╠══╣║╔╦══╦═╦══╗
──║║║╔╣╔╗║║║║╔╗║║║║═╣║║║║║║╔╗║╚╝╣║═╣╔╣══╣
──║║║║║╚╝║╚╝║╚╝║╚╣║═╣║║║║║║╔╗║╔╗╣║═╣║╠══║
──╚╝╚╝╚══╩══╩══╩═╩══╝╚╝╚╝╚╩╝╚╩╝╚╩══╩╝╚══╝
*****************************************************************
* Team Members:- Vijay Shanbhag                                 *
*                Abhishek Nalage                                *
*                Ganesh Yadav                                   *
*                Adarsh Devadiga                                *
*                Kunal Thakur                                   *
*****************************************************************
 
  Select option

1) Check your IP info
2) Check other IP info
3) Main program
4) Exit
""")
            ch=int(input("Enter Your choice: "))
            if ch==1:
                main2()
                m3()
            elif ch==2:
                main()
                m3()
            elif ch==3:
                import cstool
                cstool.first()
            elif ch==4:
                print("Exit................")
                quit()
            else:
                print("\nInvalid choice! Please try again\n")
                m3()
        except ValueError:
            print("\nInvalid choice! Please try again\n")
            m3()
        
    def finder(u):
        try:
            try:
                response = urllib.request.urlopen(u)
                data = json.load(response)

                print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print('\n>>> IP address details\n ')
                print("1) IP Address : "+data['query'],'\n')
                print("2) Org : "+data['org'],'\n')
                print("3) City : "+data['city'],'\n')
                print("4) Region : "+data['regionName'],'\n')
                print("5) Country : "+data['country'],'\n')
                print("6) Location\n")
                print("\tLattitude : "+str(data["lat"]),'\n')
                print("\tLongitude : "+str(data["lon"]),'\n')
                l='https://www.google.com/maps/place/'+str(data['lat'])+'+'+str(data['lon'])
                print("\n#"" Google Map link : ",l)
                path=os.path.isfile('/data/data/com.termux/files/usr/bin/bash')
                if path:
                    link='am start -a android.intent.action.VIEW -d '+str(l)
                    pr=input("\n>> Open link in browser? (y|n): ")
                    if pr=="y":
                        lnk=str(link)+" > /dev/null"
                        os.system(str(lnk))
                        start()
                        m3()
                    elif pr=="n":
                        print("\nCheck another IP or exit using Ctrl + C\n\n")
                        start()
                        m3()
                    else:
                        print("\nInvalid choice! Please try again\n")
                        m3()
                else:
                    pr=input("\n>> Open link in browser? (y|n): ")
                    if pr=="y":
                        webbrowser.open(l,new=0)
                        start()
                        m3()
                    elif pr=="n":
                        print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                        print("\nCheck another IP or exit using Ctrl + C\n\n")
                        start()
                        m3()
                    else:
                        print("\nInvalid choice! Please try again\n")
                        m3()
                return
            except KeyError:
                print("\nError! Invalid IP/Website Address!\n")
                m3()
        except urllib.error.URLError:
            print("\nError! Please check your internet connection!\n")
            exit()

        
    def main():
        u=input("\n>>> Enter IP Address/website address: ")
        if u=="":
            print("\nEnter valid IP Address/website address!")
            main()
        else:
            url ='http://ip-api.com/json/'+u
            finder(url)
    def main2():
        url ='http://ip-api.com/json/'
        finder(url)
        
    start()
    m3()
except KeyboardInterrupt:
    print("\nInterrupted ! Have a nice day :)")
finder()