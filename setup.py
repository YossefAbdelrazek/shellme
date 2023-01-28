import os
import time
print("""
┌──\033[1;32m(+)
└─welcome to shellme tool!
""")
time.sleep(2)
os.system("sudo apt-get install rlwrap")
time.sleep(1)
os.system("sudo apt-get install pwncat")
time.sleep(1)
os.system("sudo apt-get install powercat")
time.sleep(1)
os.system("sudo mv reverseshells /etc")
time.sleep(1)
os.system("sudo mv msfvenom /etc")
time.sleep(1)
os.system("mv .shellme.py shellme.py")
time.sleep(1)
print("nice ! ")
time.sleep(1)
os.system("python3 shellme.py")

