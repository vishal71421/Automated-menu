import os
import getpass
import subprocess as sp
import signal
global ch
def lw(x, y):
    print("\ngoodbye!!")
    exit()

signal.signal(2, lw)
# x = sp.getoutput("tput setaf 1")
# print(x)

print("\t\t\tWELCOME TO AUTO-MATE")

# x = sp.getoutput("tput setaf 0")
# print(x)
"""
# password=input()
ausername="saleena"
print("Username:")
username=input()
if username != ausername:

        print("Unauthorized user")
        exit()

password=getpass.getpass("Enter password: ")
#password=input()
apassword="saleena"
if password != apassword:

        print("Unauthorized user")
        exit()
"""
while True:
    print("""
    Press 1: for basic linux utilities
    Press 2: for entertainment options
    Press 3: for technologies
    Press 4: for networking options
    Press 5: To Exit""")

    # speaker = pyttsx3.init()
    # speaker.say("Enter your choice")
    # speaker.runAndWait()
    print("Enter your choice:", end='')
    ch = input()

    def fn():
        print("""
        Press 1: for basic linux utilities
        Press 2: for entertainment options
        Press 3: for technologies
        Press 4: for networking options
        Press 5: To Exit""")

        # speaker = pyttsx3.init()
        # speaker.say("Enter your choice")
        # speaker.runAndWait()
        print("Enter your choice:", end='')
        ch = input()
    
    
    while int(ch)==1:
        print("""
            Press 1 : for python compiler
            Press 2 : to create LVM
            Press 3 : to create swap partition
            Press 4 : to create raid devices
            Press 5 : to add new user
            Press 6 : to add new group
            Press 7 : to delete user
            Press 8 : to modify permissions
            press 9 : Go back to previous menu
            press 10 :to Exit """)
        print("Enter your choice:", end='')
        op = int(input())
        if op == 1:
            x = sp.getoutput("jupyter notebook")
            print(x)

        elif op == 2:
            print("Enter size of lvm")
            lvm = input()
            x = sp.getoutput("pvcreate /dev/sdc2")
            print(x)
            y = sp.getoutput("pvcreate /dev/sdd2")
            print(y)
            z = sp.getoutput("vgcreate vg1 /dev/sdc2 /dev/sdd2")
            print(z)
            a = sp.getoutput("lvcreate --size {} --name lvm1 vg1".format(lvm))
            b = sp.getoutput("lvdisplay lvm1")
            print(b)
                
        elif op==9:
            fn()

        elif op==10:
            exit()

    
            
    while int(ch)==2:
        print("ok")
        break
    while int(ch)==3:
        print("hii")
        break
    while int(ch)==4:
        print('hello')
        break
            
    if int(ch)==5:
        exit(0)
