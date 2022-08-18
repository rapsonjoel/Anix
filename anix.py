import os
with open(os.path.dirname(__file__) +'/'+'log.txt',"a") as f:
 with open(os.path.dirname(__file__) +'/'+'log.txt',"r") as r:
    if 'opened' in r.read():
     reqinp = input('this is the first time running this script would you like insall the required files [y/n]')
     if reqinp == 'y':
      import os 
      os.system('pip freeze' + os.path.dirname(__file__) +'/req.txt')
 r.close()   
f.write("open")  
f.close()


import os, math
from colorama import init
from pendulum import duration
from termcolor import colored
from termcolor import cprint
from pyfiglet import figlet_format
from colorama import Fore
import psutil
import platform
import time
from configparser import ConfigParser
import os

settings='config.ini'

from datetime import datetime
import subprocess


enabsettings='false'
if enabsettings=='true':
    set = '>(4) Settings\n'
else:
    set = ' '    

if "Linux" not in platform.platform():
    exit()  
config = ConfigParser()
config.read(os.path.dirname(__file__) +'/'+'config.ini') 
if config.get('settings','sudorequired') == 'true':   
 if os.geteuid() != 0:
    print("Please run as root [sudo] as this script is a administration program")
    config = ConfigParser()
    config.read(os.path.dirname(__file__) +'/'+'config.ini') 
    if config.get('settings','loginfo') == 'true':  
     with open(os.path.dirname(__file__) +'/'+'log.txt',"a") as f:
       now = datetime.now() 
       f.write(now.strftime("%d/%m/%Y %H:%M:%S") + "--" + os.getlogin()+' -- Failed (No Root Access)' +'\n' )
       f.close()
    time.sleep(0.7)   
    exit()     
def int():
    inp = input(">>")
    return inp  

def start():
 os.system("clear")
 print((colored (figlet_format("\u0332" + "ANIX", font='slant'), color="blue")))
 print("-----------------------------------------")
 print("-" + colored("Linux Administration / Utilities", color='yellow'))
 print('-' + colored("By Joel Rapson", color='red'))
 print("----------------------------------------- ")
 print("Currentley Logged in as" + ' ' + os.getlogin())
 print("----------------------------------------- ")
 print("[Type back to to go back and exit to exit]")
 print("-----------------------------------------")
 print("/Home")
 print("-----------------------------------------")
 print("Options | Choose a Number or Type the Name to Enter\n")
 print(">(0) Users <")
 print(" ")
 print(">(1) Stats\n")
 print('>(2) System Controls\n')
 print('>(3) NetWork\n')
 print(set)
 print("-----------------------------------------")
 def log():   
   config = ConfigParser()
   config.read(os.path.dirname(__file__) +'/'+'config.ini')   
   if config.get('settings','loginfo') == 'true':     
    with open(os.path.dirname(__file__) +'/'+'log.txt',"a") as f:
      now = datetime.now() 
      f.write(now.strftime("%d/%m/%Y %H:%M:%S") + "--" + os.getlogin()+' -- Success' +'\n' )
      f.close()
   
 log()    
 huh = int()          
 if "0" in huh:
        User()
 elif "user" in huh.lower():
        User()       
 
 elif "exit" in huh:
         print(colored(" --------------- Exiting ---------------", color="blue"))
         time.sleep(0.7)
         exit()  
 elif 'back' in huh:
     print('Already at Home')
     time.sleep(0.7)
     start() 
 elif '1' in huh:
     Stats()
 elif 'stats' in huh.lower():
     Stats()  
 elif '2' in huh:
       System()
 elif 'network' in huh.lower():
     network()
 elif '3' in huh.lower():
     network()  
 elif 'settings' in huh.lower():
     settings()
 elif '4' in huh.lower():
     settings()           
 else:
     print('Uknown Command')
     time.sleep(0.7)
     start()   
if enabsettings == 'true':       
 def settings():
    s = open(os.getcwd() + '/config.ini')  
    os.system("clear")
    print((colored (figlet_format("\u0332" + "ANIX", font='slant'), color="blue")))
    print("-----------------------------------------")
    print("-" + colored("Linux Administration / Utilities", color='yellow'))
    print('-' + colored("By Joel Rapson", color='red'))
    print("----------------------------------------- ")
    print("Currentley Logged in as" + ' ' + os.getlogin())
    print("----------------------------------------- ")
    print("[Type back to to go back and exit to exit]")
    print("-----------------------------------------")
    print("/Home/Settings")
    print("-----------------------------------------")
    config = ConfigParser()
    
    config.read(os.path.dirname(__file__) +'/'+'config.ini')     
    if config.get('settings','loginfo') == 'true':
        loganw=colored('True','green')
        print('nig')
    else:
        loganw=colored('False','red')       
    print('\n Log Loggins [loginfo][true/false] = ' + loganw)
    if config.get('settings','sudorequired') == 'true':
        suanw = colored('True','green')
    else:
        suanw = colored('False','red')    
    print('\n Sudo Required [true/false] (will cause errors if false) = '+suanw)
    def setimp():
        setint=input("\n>>")
        return setint 
    setint = setimp()
    if 'back' in setint.lower():
        start()
    elif "exit" in setint.lower():
         print(colored(" --------------- Exiting ---------------", color="blue"))
         time.sleep(0.7)
         exit()      
    elif 'set loginfo true' in setint.lower():
        config.set('settings','loginfo','true')
        with open(os.path.dirname(__file__) +'/'+'config.ini', "w") as config_file:
         config.write(config_file)
        settings()
    elif 'set loginfo false' in setint.lower():
        config.set('settings','loginfo','false') 
        time.sleep(1)    
        settings() 
    elif 'set sudoreq true' in setint.lower():
        config.set('settings','sudoreq','true')
        time.sleep(1)    
        settings() 
    elif 'set sudoreq false' in setint.lower():
        config.set('settings','sudoreq','false') 
        time.sleep(1)    
        settings()             
     
def network():
    os.system("clear")
    print((colored (figlet_format("\u0332" + "ANIX", font='slant'), color="blue")))
    print("-----------------------------------------")
    print("-" + colored("Linux Administration / Utilities", color='yellow'))
    print('-' + colored("By Joel Rapson", color='red'))
    print("----------------------------------------- ")
    print("Currentley Logged in as" + ' ' + os.getlogin())
    print("----------------------------------------- ")
    print("[Type back to to go back and exit to exit]")
    print("----------------------------------------- ")
    print("/Home/NetWork")
    print('-----------------------------------------  ')
    print('             Open Ports')
    print('-----------------------------------------  ')
    portss= os.system('sudo netstat -tulpn | grep LISTEN')
    if len(str(portss)) > 1:
        print(os.system('sudo netstat -tulpn | grep LISTEN'))
    else:
        print('\nNo Ports Currentley Open\n')    
    print('-----------------------------------------  ')
    print('> Close Port [clport]')
    print('> Open Port [opport]')
    print('> Scan Ports(Rustscan Required)[pscan]')
    def netimp():
        netint = input('>>')
        return netint
    netint = netimp()
    if 'back' in netint.lower():
        start()
    elif 'pscan' in netint.lower():
        def scanimp():
            scanint=input("IP >> ")
            return scanint
        scanint = scanimp() 
        if scanint == "self":
            IP = '127.0.0.1' 
        if scanint != 'self':
            IP = scanint          
        os.system('rustscan -a' + IP) 
        input("Press Enter When Done")
        network()   
    elif 'clport' in netint.lower():
            def clportportimp():
                clportportint=input('Type(TCP,UDP, e.g)>> ')
                return clportportint
             
            def clportnumimp():
                clportnumint=input('What Port>> ')                
                return clportnumint
            clportportint=str(clportportimp())
            clportnumint = str(clportnumimp())
            os.system('sudo ' + "ufw "  + 'deny ' +clportportint + '/' + clportnumint)  
            print('------Closing Port------')
            print('---Port: ' + clportnumint)
            print('---Type: ' + clportportint)  
            time.sleep(2)
            print('------Done------')
            time.sleep(1)
            network()    
    elif 'opport' in netint.lower():
            def opportportimp():
                opportportint=input('Type(TCP,UDP, e.g)>> ')
                return opportportint
             
            def opportnumimp():
                opportnumint=input('What Port>> ')                
                return opportnumint
            opportportint=str(opportportimp())
            opportnumint = str(opportnumimp())
            os.system('sudo ' + "ufw "  + 'allow ' +opportnumint + '/' + opportportint) 
            print('------Opening Port------')
            print('---Port: ' + opportnumint)
            print('---Type: ' + opportportint)  
            time.sleep(2)
            print('------Done------')
            time.sleep(1)
            network()  
    elif "exit" in netint.lower():
         print(colored(" --------------- Exiting ---------------", color="blue"))
         time.sleep(0.7)
         exit() 
    else:
        network()                  
        
        
def System(): 
    os.system("clear")
    print((colored (figlet_format("\u0332" + "ANIX", font='slant'), color="blue")))
    print("-----------------------------------------")
    print("-" + colored("Linux Administration / Utilities", color='yellow'))
    print('-' + colored("By Joel Rapson", color='red'))
    print("----------------------------------------- ")
    print("Currentley Logged in as" + ' ' + os.getlogin())
    print("----------------------------------------- ")
    print("[Type back to to go back and exit to exit]")
    print("----------------------------------------- ")
    print("/Home/System Controls")
    print('-----------------------------------------  ')
    print("\n> Restart System [restart]")
    print('\n> Update System [update]')
    print('\n> Create New User [new user]')
    print('\n> Remove User [remove user]')
    print('\n> Scan System For File type [scan]')
    print('\n> Scan System For Folder [discan]')
    print('\n-----------------------------------------  ')
    def sysinp():
        sysint=input('>>')
        return sysint
    imp = sysinp()
    
    #Commands
    if 'restart' in imp.lower():
        def resint():
         ques=input('Confirm [y/n]>>')
         return ques
        
        def ask():
         ques = resint()
         if ques == 'y':
             print(colored('------RESTARTING------', 'blue'))
             time.sleep('')
             os.system('sudo reboot')
         elif ques == 'n':
             print('------Canceled------')
             time.sleep(0.3)
             System()    
         else:
             print('Please Choose y or n')
             ask()
        ask()    
    if 'update' in imp.lower():
        print(colored('------Updating System------', 'blue'))
        time.sleep(1)
        os.system('sudo apt update')
        def ask2():
         def resint2():
          ques2=input('Would you like to upgrade [y/n]>>')
          return ques2
         ques2= resint2()
         if  ques2 == "y":
             print('------Upgrading-------')
             time.sleep(1)
             os.system('sudo apt upgrade')
             System()
         elif ques2 == 'n':
             print('------Canceled------')
             time.sleep(0.3)
             System()    
         else:
             print('Please Choose y or n')
             ask2()
        ask2()   
    elif 'new user' in imp.lower():
                 def addint():
                     addinpt=input('UserName >> ')
                     return addinpt
                 addinpt=addint()
                 print('------Adding User ' + addinpt +'------')          
                 os.system('adduser ' + addinpt)
                 print('User successfuly created')
                 time.sleep(1)
                 System()   
    elif 'remove user' in imp.lower():
                ka = input('Users Name That You Wish To Delete >>')
                print('------Deleting User------')
                time.sleep(2)   
                os.system('userdel' + " " +ka)
                print('User Successfuly Deleted')
                time.sleep(2)
                System() 
    elif 'back' in imp.lower():   
        start()             
    elif imp.lower() == 'scan':
        def scanimp():
            scanint = input('File Type(.txt)>> ')
            return scanint
        scanint = scanimp()  
        os.system('find . -type f -name "*' + scanint + '"')
        input("Press Enter When Done")
        System()   
    elif imp.lower() == 'discan':
        def scanfiimp():
            scanint = input('Folder Type>> ')
            return scanint
        scanint = scanfiimp()  
        os.system("sudo find / -type d -name '" + scanint + "'")
        input("Press Enter When Done")
        System() 
    elif "exit" in imp.lower():
         print(colored(" --------------- Exiting ---------------", color="blue"))
         time.sleep(0.7)
         exit()  
    else:
        System()          
              
                 
                            
                 
             
            
                
        
        
        
        
   
def User():
     os.system("clear")
     print((colored (figlet_format("\u0332" + "ANIX", font='slant'), color="blue")))
     print("-----------------------------------------")
     print("-" + colored("Linux Administration / Utilities", color='yellow'))
     print('-' + colored("By Joel Rapson", color='red'))
     print("----------------------------------------- ")
     print("Currentley Logged in as" + ' ' + os.getlogin())
     print("----------------------------------------- ")
     print("[Type back to to go back and exit to exit]")
     print("----------------------------------------- ")
     print("/Home > Users")
     print('-----------------------------------------  ')
     user_list = psutil.users()
     print("Current Users:")
     
     def search():
      os.system("clear")
      print((colored (figlet_format("\u0332" + "ANIX", font='slant'), color="blue")))
      print("-----------------------------------------")
      print("-" + colored("Linux Administration / Utilities", color='yellow'))
      print('-' + colored("By Joel Rapson", color='red'))
      print("----------------------------------------- ")
      print("Currentley Logged in as" + ' ' + os.getlogin())
      print("----------------------------------------- ")
      print("[Type back to to go back and exit to exit]")
      print("----------------------------------------- ")
      print("/Home/Users")
      print('-----------------------------------------  ')
      
      print(colored('Users Like "postgres" or "0" or "root" Should not be touched\n', 'blue'))
      print("Users Loggin:")   
      '''users = psutil.users()
      for user in users:
        print(user.name)'''
      print(os.system("getent passwd | egrep  '(/bin/bash)|(/bin/zsh)|(/bin/sh)' | cut -f1 -d:"))  
        
      print(" ")  
      print("-----------------------------------------")
     def userint():  
       userinp=input('>>')
       return userinp 
     
     search() 
     inpt = userint()
     
     if "back" in inpt: 
        start() 
     elif "refresh" in inpt:
         search()   
     
     elif len(inpt) == 0:
         User()    
        
     elif "exit" in inpt:
         print(colored(" --------------- Exiting ---------------", color="blue"))
         time.sleep(0.7)
         exit()
      
     else:
         print('Uknown Command')
         search()      
     def usopts():
             selected=inpt
             adcheck = subprocess.getoutput("id" +" "+ selected) 
             os.system("clear")
             print((colored (figlet_format("\u0332" + "ANIX", font='slant'), color="blue")))
             print("-----------------------------------------")
             print("-" + colored("Linux Administration / Utilities", color='yellow'))
             print('-' + colored("By Joel Rapson", color='red'))
             print("----------------------------------------- ")
             print("Currentley Logged in as" + ' ' + os.getlogin())
             print("----------------------------------------- ")
             print("[Type back to to go back and exit to exit]")
             print("----------------------------------------- ")
             print("/Home/Users/" + inpt.lower())
             print('-----------------------------------------  ')
             if "sudo" in subprocess.getoutput("groups" + " " + inpt):
                 print("Privledges --" + colored(" Root\n", 'red'))
             else:
                 print("Privledges --" + colored(" User\n", 'yellow'))
             
               
                   
             logcheck = subprocess.getoutput("last" + " " + inpt + " " + "-1") 
             logcheck2 = logcheck.replace(inpt,"")
             logcheck3=logcheck2.replace(':1',"")
             logcheck4=logcheck3.replace("still logged in", "")
             logcheck5=logcheck4.replace("wtmp begins Sun Feb  6 20:24:30 2022","")   
             logcheck6=logcheck5.replace("                              ","") 
             logcheck7=logcheck6.replace("    tty3         tty3             ",'')
             if len(logcheck7) == 0:
                 logcheck8 = "New User Or Deleted User, Please Restart Your System"
             else:
                 logcheck8 = logcheck7    
             print(colored("Last Loggin:  ", 'red') + colored(str(logcheck8), "yellow")) 
             print('-----------------------------------------  ') 
             print('> Change Password [set password]\n')
             print("> Exit the script [exit] \n")
             print("> Return to Previos Page [back] \n")
             print("> Print Histroy [history] -- \n")
             print("> Add Sudo Permission To User [add root] -- \n")
             print("> Remove Sudo Permissions From User [remove root] \n")
             print("> Restore Page [clear]  \n")
             print("> Reboots System [restart] (helpful to apply changes)\n")  
             print('> Remove User [remove user]\n')   
               
             if os.getlogin() == inpt:
                 print(colored("[Current User]", 'red')) 
             print("When Finished Relog to apply changes [Type [restart] to restart the system]")   
             
                 
                 
             def inpu():
              useropin = input(">>")
              return useropin
             useropint=inpu()       
          
             if "back" in useropint:
                 User()
             elif len(useropint) == 0:
                 usopts()       
             elif "exit" in useropint:
                  print(colored(" --------------- Exiting ---------------", color="blue"))
                  time.sleep(0.7)
                  exit()       
             elif "add root" in useropint:
                 os.system("sudo usermod -a -G sudo" + " " + inpt.lower())
                 os.system("sudo usermod -a -G sudoers" + " " + inpt.lower())
                 usopts()

             elif "remove root" in useropint:
                 os.system("gpasswd -d" + " " + inpt.lower()+ " " + "sudo")
                 os.system("gpasswd -d" + " " + inpt.lower()+ " " + "sudoers")
                 usopts()      
             elif "history" in useropint:
                 history = os.system('last' + " " +inpt)   
                 print(history)   
                 inpu()
             elif "clear" in useropint:
                 usopts()    
             elif "restart" in useropint:
                 os.system("sudo reboot") 
             elif "set password" in useropint.lower():
                     print('------Reset Password------')                
                     os.system('sudo passwd' + ' ' + inpt)
             elif 'remove user' in useropint:
                ka = input('Confirm [y/n]')
                if 'y' in ka: 
                 print('------Deleting User------')
                 time.sleep(2)   
                 os.system('userdel' + "" + inpt) 
                 usopts() 
                elif 'n' in ka:
                    print('k')
                    time.sleep(0.3)
                    usopts() 
                else:
                    print('Please Choose y or n') 
             
                        
             
                
     users=subprocess.getoutput("getent passwd | egrep  '(/bin/bash)|(/bin/zsh)|(/bin/sh)' | cut -f1 -d:")
     if inpt.lower() in users:
            if len(inpt) != 0:
                usopts()
              
                 
        
     
def Stats():
    os.system("clear")
    print((colored (figlet_format("\u0332" + "ANIX", font='slant'), color="blue")))
    print("-----------------------------------------")
    print("-" + colored("Linux Administration / Utilities", color='yellow'))
    print('-' + colored("By Joel Rapson", color='red'))
    print("----------------------------------------- ")
    print("Currentley Logged in as" + ' ' + os.getlogin())
    print("----------------------------------------- ")
    print("[Type back to to go back and exit to exit]")
    print("----------------------------------------- ")
    print("/Home/Stats")
    print('-----------------------------------------  ') 
    print("             CPU STATS")
    print('-----------------------------------------  ')
    print("             Current = " + str(round(psutil.cpu_freq().current, 2)) + "GHz")  
    print("             Max = " + str(round(psutil.cpu_freq().max, 2)) + "GHz")
    print("             Min = " + str(round(psutil.cpu_freq().min, 2)) + "GHz")
    print("             Usage = " + str(psutil.cpu_percent()) + '%')    
    print("             Cores = " + str(psutil.cpu_count()) + ' Cores')  
    print('-----------------------------------------  ')
    print('             RAM STATS')
    print('-----------------------------------------  ')
    print('             Usage = ' + str(round(psutil.virtual_memory().percent, 2)) + '%')
    print('             Total = ' + str(round(psutil.virtual_memory().total / 1073741824, 2)) + 'GB')
    print('             Free = ' + str(round(psutil.virtual_memory().free / 1073741824, 2)) + 'GB')
    print('             Used = ' + str(round(psutil.virtual_memory().used / 1073741824, 2)) + 'GB')
    print('-----------------------------------------  ')
    print('Type [refresh] or [r] to refresh')
    
   
    
    
    def statint():
        yeah = input(">> ") 
        return yeah
    statinp = statint() 
       
    
    if 'back' in statinp.lower():       
        start()  
    if 'refresh' in statinp.lower():
        Stats()
    if 'r' in statinp.lower():
        Stats()  
    if len(statinp) == 0:
        Stats()   
    if "exit" in statinp.lower():
        print(colored(" --------------- Exiting ---------------", color="blue"))
        time.sleep(0.7)
        exit()          
        
    
                 
                     
                 
     
        
         
start()     

    
    
       
     
    
    
     
