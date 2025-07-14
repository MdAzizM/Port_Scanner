from Utils.scanner import thread_scan, default_scan
def banner ():
    print(r"""
 ____            _     ____                                  
|  _ \ ___  _ __| | __/ ___|  ___ __ _ _ __  _ __   ___ _ __ 
| |_) / _ \| '__| |/ /\___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
|  __/ (_) | |  |   <  ___) | (_| (_| | | | | | | |  __/ |   
|_|   \___/|_|  |_|\_\|____/ \___\__,_|_| |_|_| |_|\___|_|   

                        Port Scanner
""")    
    print("Auth: Guard, Version: 1.0")
    print("This tool is designed to scan ports on a target host.")
    print("\n")  



def menu():
    print("===============menu================")
    print("| Please select an option:        |")
    print("|  1> Scan with threads           |")
    print("|  2> Default scan without threads|")
    print("|  3> Display menu                |")
    print("|  4> Quit                        |")
    print("===================================")
    print("\n")



def quest():
    choice = int(input("Enter a number: "))
    if choice < 1 or choice > 4:
        print("Invalid choice. Please try again.")
        return quest()
    else:
        return choice
    


def pick(choice):
    while(choice != 4):
        if choice == 1:
            thread_scan()
        elif choice == 2:
            default_scan()
        elif choice == 3:
            menu()
        elif choice == 4:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        
        choice = quest()
    

    
def display ():
    banner()
    menu()
    choice = quest()
    pick(choice)
