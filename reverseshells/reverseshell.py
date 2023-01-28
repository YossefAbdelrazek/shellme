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
        command = input("\033[1;32msmf \033[1;34m(\033[1;31mreverse/shells/console\033[1;34m)> \033[1;32m")
        if command == "help":
            helpbanner()
        elif command == "shellslist":
            shells()  
        elif command == "exit":
            print("[+] please type exit -y to go out the tool")
        elif command == "exit -y":
                            print("bye ! ")
                            os.system("""python3 -c 'import pty;pty.spawn("/bin/bash")'""")
        elif command == "back":
                        os.system("python3 shellme.py")   
        elif command == "clear":
                        os.system("clear")    
        elif command == "list":
                        reversehell_list()
        elif command == "use":
                        reversehell_list()
        elif command == "use 1" or command == "use reversehell/Perl":
                        os.system("python3 /etc/reverseshells/reverseshell-Perl.py")
        elif command == "":
            pass
        elif command == "use 2" or command == "use reversehell/Perl/no_sh":
            os.system("python3 /etc/reverseshells/revsreshell_Perl_no_sh.py")
            #
        elif command == "use 3" or command == "use reversehell/Perl/PentestMonkey":
            os.system("python3 /etc/reverseshells/revsreshell_Perl_PentestMonkey.py") 
            #
        elif command == "use 4" or command == "use reversehell/PHP/Emoji":
            os.system("python3 /etc/reverseshells/reversehell_PHP_Emoji.py") 
            #
        elif command == "use 5" or command == "use reversehell/PHP/PentestMonkey":
            os.system("python3 /etc/reverseshells/reversehell_PHP_PentestMonkey.py")
            #
        elif command == "use 6" or command == "use reversehell/PHP/Ivan/Sincek":
            os.system("python3 /etc/reverseshells/reversehell_PHP_Ivan_Sincek.py")
            #
        elif command == "use 7" or command == "use reversehell/PHP/cmd":
            os.system("python3 /etc/reverseshells/reverseshell_PHP_cmd.py")
            #
        elif command == "use 8" or command == "use reversehell/PHP/exec":
            os.system("python3 /etc/reverseshells/reversehell_PHP_exec.py")
            #
        elif command == "use 9" or command == "use reversehell/PHP/shell_exec":
            os.system("python3 /etc/reverseshells/reverseshell_PHP_shell_exec.py")
            #
        elif command == "use 10" or command == "use reversehell/PHP/system":
            os.system("python3 /etc/reverseshells/reversehell_PHP_system.py")
            #
        elif command == "use 11" or command == "use reversehell/PHP/passthru":
            os.system("python3 /etc/reverseshells/reverseshell_PHP_passthru.py")
            #
        elif command == "use 12" or command == "use reversehell/PHP `":
            os.system("python3 /etc/reverseshells/reversehell_PHP_bqout.py")
            #
        elif command == "use 13" or command == "use reversehell/PHP/popen":
            os.system("python3 /etc/reverseshells/reversehell_PHP_popen.py")
            #
        elif command == "use 14" or command == "use reverseshell/PHP/proc/open":
            os.system("python3 /etc/reverseshells/reverseshell_PHP_proc_open.py")
            #
        elif command == "use 15" or command == "use reversehell/Windows/ConPty":
            os.system("python3 /etc/reverseshells/reverseshell_Windows_ConPty.py")
            #
        elif command == "use 16" or command == "use reverseshell/PowerShell_1":
            os.system("python3 /etc/reverseshells/reverseshell_PowerShell_1.py")
            #
        elif command == "use 17" or command == "use reverseshell/PowerShell_2":
            os.system("python3 /etc/reverseshells/reverseshell_PowerShell_2.py")
            #
        elif command == "use 18" or command == "use reverseshell/PowerShell_3":
            os.system("python3 /etc/reverseshells/reverseshell_PowerShell_3.py")
            #
        elif command == "use 19" or command == "use reverseshell/PowerShell_TLS":
            os.system("python3 /etc/reverseshells/reverseshell_PowerShell_TLS.py")
            #
        elif command == "use 20" or command == "use reverseshell/PowerShell/Base64":
            os.system("python3 /etc/reverseshells/reverseshell_PowerShell_Base64.py")
            #
        elif command == "use 21" or command == "use reverseshell/Python_1":
            os.system("python3 /etc/reverseshells/reverseshell_Python_1.py")
            #
        elif command == "use 22" or command == "use reverseshell/Python_2":
            os.system("python3 /etc/reverseshells/reverseshell_Python_2.py")
            #
        elif command == "use 23" or command == "use reverseshell/Python3_1":
            os.system("python3 /etc/reverseshells/reverseshell_Python3_1.py")
            #
        elif command == "use 24" or command == "use reverseshell/Python3_2":
            os.system("python3 /etc/reverseshells/reverseshell_Python3_2.py")
            #
        elif command == "use 25" or command == "use reverseshell/Python3_Windows":
            os.system("python3 /etc/reverseshells/reverseshell_Python3_Windows.py")
            #
        elif command == "use 26" or command == "use revseshell/Python3_shortest":
            os.system("python3 /etc/reverseshells/reverseshell_Python3_shortest.py")
            #
        elif command == "use 27" or command == "use reverseshell/Ruby_1":
            os.system("python3 /etc/reverseshells/reverseshell_Ruby_1.py")
            #
        elif command == "use 28" or command == "use reverseshell/Ruby/no_sh":
            os.system("python3 /etc/reverseshells/reverseshell_Ruby_no_sh.py")
            #
        elif command == "use 29" or command == "use reverseshell/socat_1":
            os.system("python3 /etc/reverseshells/revseshell_socat_1.py")
            #
        elif command == "use 30" or command == "use reverseshell/socat_2":
            os.system("python3 /etc/reverseshells/revseshell_socat_2.py")
            #
        elif command == "use 31" or command == "use reverseshell/node.js":
            os.system("python3 /etc/reverseshells/reverseshell_node.js.py")
            #
        elif command == "use 32" or command == "use reverseshell/node.js_2":
            os.system("python3 /etc/reverseshells/reverseshell_node.js_2.py")
            #
        elif command == "use 33" or command == "use reverseshell/Java_1":
            os.system("python3 /etc/reverseshells/revseshell_Java_1.py")
            #
        elif command == "use 34" or command == "use reverseshell/Java_2":
            os.system("python3 /etc/reverseshells/revseshell_Java_2.py")
            #
        elif command == "use 35" or command == "use reverseshell/Java_3":
            os.system("python3 /etc/reverseshells/revseshell_Java_3.py")
            #
        elif command == "use 36" or command == "use reverseshell/Javascript":
            os.system("python3 /etc/reverseshells/reverseshell_Javascript.py")
            #
        elif command == "use 37" or command == "use reverseshell/Groovy":
            os.system("python3 /etc/reverseshells/reverseshell_Groovy.py")
            #
        elif command == "use 38" or command == "use reverseshell_telnet.py":
            os.system("python3 /etc/reverseshells/reverseshell_telnet.py")
            #
        elif command == "use 40" or command == "use reverseshell/Lua_1":
            os.system("python3 /etc/reverseshells/reverseshell_Lua_1.py")
            #
        elif command == "use 41" or command == "use reverseshell/Lua_2":
            os.system("python3 /etc/reverseshells/reverseshell_Lua_2.py")
            #
        elif command == "use 42" or command == "use reverseshell/Golang":
            os.system("python3 /etc/reverseshells/reverseshell_Golang.py")
            #
        elif command == "use 43" or command == "use reverseshell/Vlang":
            os.system("python3 /etc/reverseshells/reverseshell_Vlang.py")
            #
        elif command == "use 44" or command == "use reverseshell/Awk":
            os.system("python3 /etc/reverseshells/reverseshell_Awk.py")
            #
        elif command == "use 45" or command == "use reverseshell/Dart":
            os.system("python3 /etc/reverseshells/reverseshell_Dart.py")
            #
        elif command == "use 46" or command == "use reverseshell/Bash -i":
            os.system("python3 /etc/reverseshells/reverseshell_Bash_-i.py")
            #
        elif command == "use 47" or command == "use reverseshell/Bash/196":
            os.system("python3 /etc/reverseshells/reverseshell_Bash_196.py")
            #
        elif command == "use 48" or command == "use reverseshell/Bash/read_line":
            os.system("python3 /etc/reverseshells/reverseshell_Bash_read_line.py")
            #
        elif command == "use 49" or command == "use reverseshell/Bash_5":
            os.system("python3 /etc/reverseshells/reverseshell_Bash_5.py")
            #
        elif command == "use 50" or command == "use reverseshell/Bash_udp":
            os.system("python3 /etc/reverseshells/reverseshell_Bash_udp.py")
            #
        elif command == "use 51" or command == "use reverseshell/nc_mkfifo":
            os.system("python3 /etc/reverseshells/reverseshell_nc_mkfifo.py")
            #
        elif command == "use 52" or command == "use reverseshell/nc -e":
            os.system("python3 /etc/reverseshells/reverseshell_nc_-e.py")
            #
        elif command == "use 53" or command == "use reverseshell/nc_exe -e":
            os.system("python3 /etc/reverseshells/reverseshell_nc_exe_-e.py")
            #
        elif command == "use 54" or command == "use reverseshell/nc -c":
            os.system("python3 /etc/reverseshells/reverseshell_nc_-c.py")
            #
        elif command == "use 55" or command == "use reverseshell/ncat -e":
            os.system("python3 /etc/reverseshells/reverseshell_ncat_-e.py")
            #
        elif command == "use 56" or command == "use reverseshell/ncat_exe -e":
            os.system("python3 /etc/reverseshells/reverseshell_ncat_exe_-e.py")
            #
        elif command == "use 57" or command == "use reverseshell/ncat_udp":
            os.system("python3 /etc/reverseshells/reverseshell_ncat_udp.py")
            #
        elif command == "use 58" or command == "use reverseshell/rustcat":
            os.system("python3 /etc/reverseshells/reverseshell_rustcat.py")
            #
        elif command == "use 59" or command == "use reverseshell/C":
            os.system("python3 /etc/reverseshells/reverseshell_C.py")
            #
        elif command == "use 60" or command == "use reversehell/C/Windows":
            os.system("python3 /etc/reverseshells/reversehell_C_Windows.py")
            #
        elif command == "use 61" or command == "use reverseshell/C#/TCP/Client":
            os.system("python3 /etc/reverseshells/reverseshell_C#_TCP_Client.py")
            #
        elif command == "use 62" or command == "use reverseshell/C#/Bash -i":
            os.system("python3 /etc/reverseshells/reverseshell_C#_Bash_-i.py")
            #
        elif command == "use 63" or command == "use reverseshell/Haskell_1":
            os.system("python3 /etc/reverseshells/reverseshell_Haskell_1.py")
        else:
            print(f"command is not found: \033[1;34m'\033[1;31m{command}\033[1;34m'")  
    except:
        pass