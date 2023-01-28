# HELLO FROM SHELL ME FRAMWORK
# MADE BY YOSSEF ABDELRAZEK 
import platform
import os
import time
import random
from datetime import datetime
from sys import stdout
def msfvenom():
  print("""
--------------------------------------------
                +msfvenom+

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
|   help ==> help banner              |                    
|   exit ==> exit the exploit         |                                  |
|   list ==> to show  reverseshells   |
|   list2 ==> to show  Listenershells |
|   shellslist ==> to show shells     |
|   bindslist ==> to show binds       |
|   msfvenomlist ==> to show msfvenom |
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
11# revsreshell/PHP/passthru
12# revsreshell/PHP `
13# revsreshell/PHP/popen
14# revsreshell/PHP/proc/open
15# revsreshell/Windows/ConPty
16# revsreshell/PowerShell_1
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
def banner1(): # THIS IS BANNER FOR THE TOOL
    print("""    
       \033[1;31m(`-').-> (`-').-> (`-')  _                     <-. (`-')   (`-')  _ 
       \033[1;31m( OO)_   (OO )__  ( OO).-/  <-.      <-.          \(OO )_  ( OO).-/ 
      \033[1;31m(_)--\_) ,--. ,'-'(,------.,--. )   ,--. )      ,--./  ,-.)(,------. 
      \033[1;31m/    _ / |  | |  | |  .---'|  (`-') |  (`-')    |   `.'   | |  .---' 
      \033[1;31m\_..`--. |  `-'  |(|  '--. |  |OO ) |  |OO )    |  |'.'|  |(|  '--.  
      \033[1;31m.-._)   \|  .-.  | |  .--'(|  '__ |(|  '__ |    |  |   |  | |  .--'  
      \033[1;31m\       /|  | |  | |  `---.|     |' |     |'    |  |   |  | |  `---. 
       \033[1;31m`-----' `--' `--' `------'`-----'  `-----'     `--'   `--' `------'            
                                                                                                    
               \033[1;34m (               \033[1;32mSHELL ME v1.1.0 dev           \033[1;34m    ) 
        \033[1;34m+ -- --=\033[1;32m[      63:reverseshells  -  24:msfvenom           \033[1;32m]
        \033[1;34m+ -- --=\033[1;32m[                                                 \033[1;32m]
        \033[1;34m+ -- --=\033[1;32m[                   8:Listeners                   \033[1;32m]       
        \033[1;34m+ -- --=\033[1;32m[                                                 \033[1;32m]
        \033[1;34m+ -- --=\033[1;32m[           \033[1;31mMADE BY YOSSEF ABDELRAZEK             \033[1;32m]
        """)
user_in_linux = platform.node()
timer = time.strftime("%Y-%m-%d")
timer3 = time.strftime("%H:%M:%S")
os.system("clear")                                     
print(banner1())
timer2 = time.strftime("%Y-%m-%d %H:%M:%S")
commands = ["help","clear","","exit","reverseshellconsole","rsc","rsconsole","list","list2","shellslist","bindslist","msfvenomlist","smf -php --bind","smf -python --bind"] # THIS IS THE COMMADS FOR THE TOOL 
while True: # AND THIS LOOP FOR THE INPUT OF THE TOOL 
    try:   
      i = input(f""" 
┌──(\033[1;31mroot\033[1;31m-@\033[1;34m{user_in_linux}\033[1;32m)-[{timer}]\033[0m
\033[1;31m└─$ """)
      if i == "clear":
            os.system("clear")
            pass
      elif i == None:
        pass
      elif i == "exit":
        os.system("""python3 -c 'import pty;pty.spawn("/bin/bash")'""") 
      elif i == "help":
          os.system("cat banner.txt")
          print("")
          pass
      elif i == "rsc" or i == "reverseshellconsole" or i == "rsconsole":
        os.system("cd /etc/reverseshells/")
        os.system("python3 /etc/reverseshells/reverseshell.py")
      elif i == "list":
          reverseshell_list()
          pass
      elif i == "list2":
          Listenershell()
          pass
      elif i == "msfvenomlist":
              msfvenom()
              pass
      elif i == "":
        pass
      else:
        print(f"commad is not found: '{i}'")
    except:
      pass
    
    
          
    