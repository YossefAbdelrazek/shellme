import os 
import time 
import sys
import threading
def revo():
    payload = "[+] <revsre_shells>\n"
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
8# Windows/Stageless/Reverse/TCP/x32
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
def helpbanner():
    print(f"""
 -------------------------------------
|  help ==> help banner               |                    
|  exit -y  ==> exit the exploit      |
|  list ==> to get reverseshells list |
|  use ==> to select exploit          |
 ------------------------------------  
""")
def reversehell_list():
    print("""
--------------------------------------------
                                       __       ____
  _______ _  _____ _______ ___    ___ / /  ___ / / /
 / __/ -_) |/ / -_) __(_-</ -_)  (_-</ _ \/ -_) / / 
/_/  \__/|___/\__/_/ /___/\__/__/___/_//_/\__/_/_/  
                            /___/                   
1# reversehell/Perl
2# reversehell/Perl/no_sh
3# reversehell/Perl/PentestMonkey
4# reversehell/PHP/Emoji
5# reversehell/PHP/PentestMonkey
6# reversehell/PHP/Ivan/Sincek
7# reversehell/PHP/cmd
8# reversehell/PHP/exec
9# reversehell/PHP/shell_exec
10# reversehell/PHP/system
11# reversehell/PHP/passthru
12# reversehell/PHP `
13# reversehell/PHP/popen
14# reversehell/PHP/proc/open
15# reversehell/Windows/ConPty
16# reversehell/PowerShell_1
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
60# reversehell/C/Windows
61# reverseshell/C#/TCP/Client
62# reverseshell/C#/Bash -i
63# reverseshell/Haskell_1
--------------------------------------------
    """)
exin_commands = ["help","exit","","use","use 1","use reversehell/Perl","back","exit -y","list","clear","use 2","use reversehell/Perl/no_sh","use 3","use reversehell/Perl/PentestMonkey","use 4","use reversehell/PHP/Emoji","use 5","use reversehell/PHP/PentestMonkey","shellslist"]
while True:
    try:  
        command = input("\033[1;32msmf \033[1;34m(\033[1;31mmsfvenom/console\033[1;34m)> \033[1;32m")
        if command == "help":
            helpbanner()
        elif command == "shellslist":
            shells()  
        elif command == "exit":
            print("[+] please type exit -y to go out the tool")
        elif command == "exit -y":
            print("bye ! ")
            os.system("""python3 -c 'import pty;pty.spawn("/bin/bash")'""")   
        elif command == "clear":
            os.system("clear")    
        elif command == "list":
            reversehell_list()
        elif command == "use":
            reversehell_list()
        elif command == "use 1" or command == "use Windows/Meterpreter/Staged/Reverse/TCP/x64":
            os.system("python3 /etc/msfvenom/Windows_Meterpreter_Staged_Reverse_TCP_x64.py")
        elif command == "":
            pass
        elif command == "use 2" or command == "use Windows/Meterpreter/Staged/Reverse/TCP/x32":
            os.system("python3 /etc/msfvenom/Windows_Meterpreter_Staged_Reverse_TCP_x32.py")
            #
        elif command == "use 3" or command == "use Windows/Meterpreter/Stageless/Reverse/TCP/x64":
            os.system("python3 /etc/msfvenom/Windows_Meterpreter_Stageless_Reverse_TCP_x64.py") 
            #
        elif command == "use 4" or command == "use Windows/Meterpreter/Stageless/Reverse/TCP/x32":
            os.system("python3 /etc/msfvenom/Windows_Meterpreter_Stageless_Reverse_TCP_x32.py") 
            #
        elif command == "use 5" or command == "use Windows/Staged/Reverse/TCP/x64":
            os.system("python3 /etc/msfvenom/Windows_Staged_Reverse_TCP_x64.py")
            #
        elif command == "use 6" or command == "use Windows/Staged/Reverse/TCP/x32":
            os.system("python3 /etc/msfvenom/Windows_Staged_Reverse_TCP_x32.py")
            #
        elif command == "use 7" or command == "use Windows/Stageless/Reverse/TCP/x64":
            os.system("python3 /etc/msfvenom/Windows_Stageless_Reverse_TCP_x64.py")
            #
        elif command == "use 8" or command == "use Windows/Stageless/Reverse/TCP/x32":
            os.system("python3 /etc/msfvenom/Windows_Stageless_Reverse_TCP_x32.py")
            #
        elif command == "use 9" or command == "use Linux/Meterpreter/Staged/Reverse/TCP/x64":
            os.system("python3 /etc/msfvenom/Linux_Meterpreter_Staged_Reverse_TCP_x64.py")
            #
        elif command == "use 10" or command == "use Linux/Meterpreter/Staged/Reverse/TCP/x86":
            os.system("python3 /etc/msfvenom/Linux_Meterpreter_Staged_Reverse_TCP_x86.py")
            #
        elif command == "use 11" or command == "use Linux/Stageless/Reverse/TCP/x64":
            os.system("python3 /etc/msfvenom/Linux_Stageless_Reverse_TCP_x64.py")
            #
        elif command == "use 12" or command == "use Linux/Stageless/Reverse/TCP/x86":
            os.system("python3 /etc/msfvenom/Linux_Stageless_Reverse_TCP_x86.py")
            #
        elif command == "use 13" or command == "use Windows/Bind/TCP/ShellCode/BOF":
            os.system("python3 /etc/msfvenom/Windows_Bind_TCP_ShellCode_BOF.py")
            #
        elif command == "use 14" or command == "use macOS/Meterpreter/Staged/Reverse/TCP/x64":
            os.system("python3 /etc/msfvenom/macOS_Meterpreter_Staged_Reverse_TCP_x64.py")
            #
        elif command == "use 15" or command == "use macOS/Meterpreter/Stageless/Reverse/TCP/x64":
            os.system("python3 /etc/msfvenom/macOS_Meterpreter_Stageless_Reverse_TCP_x64.py")
            #
        elif command == "use 16" or command == "use macOS/Stageless/Reverse/TCP/x64":
            os.system("python3 /etc/msfvenom/macOS_Stageless_Reverse_TCP_x64.py")
            #
        elif command == "use 17" or command == "use PHP/Meterpreter/Stageless/Reverse/TCP":
            os.system("python3 /etc/msfvenom/PHP_Meterpreter_Stageless_Reverse_TCP.py")
            #
        elif command == "use 18" or command == "use PHP/Reverse/PHP":
            os.system("python3 /etc/msfvenom/PHP_Reverse_PHP.py")
            #
        elif command == "use 19" or command == "use JSP/Stageless/Reverse/TCP":
            os.system("python3 /etc/msfvenom/JSP_Stageless_Reverse_TCP.py")
            #
        elif command == "use 20" or command == "use WAR/Stageless/Reverse/TCP":
            os.system("python3 /etc/msfvenom/WAR_Stageless_Reverse_TCP.py")
            #
        elif command == "use 21" or command == "use Android/Meterpreter/Reverse/TCP":
            os.system("python3 /etc/msfvenom/Android_Meterpreter_Reverse_TCP.py")
            #
        elif command == "use 22" or command == "use Android/Meterpreter/Embed/Reverse/TCP":
            os.system("python3 /etc/msfvenom/Android_Meterpreter_Embed_Reverse_TCP.py")
            #
        elif command == "use 23" or command == "use Python/Stageless/Reverse/TCP":
            os.system("python3 /etc/msfvenom/Python_Stageless_Reverse_TCP.py")
            #
        elif command == "use 24" or command == "use Bash/Stageless/Reverse/TCP":
            os.system("python3 /etc/msfvenom/Bash_Stageless_Reverse_TCP.py")  
        else:
            print(f"commad is not found: '{command}'")
    except:
        pass