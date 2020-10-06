#!/usr/bin/python
import os,getpass,hashlib,time
firststart=False
username=''
homedir=os.getcwd()
def run():
    global firststart
    try:
        import httplib2
        print('Httplib2 installed.OK')
    except ImportError:
        import subprocess
        subprocess.call(['pip','install','httplib2'])
        import httplib2
    
    if 'basc' not in os.listdir(os.getcwd()):
        print('You are starting new basc session.')
        firststart=True
        print('Creating basc root...')
        
        time.sleep(0.1)

        os.mkdir('basc')
        print('1/3')
    os.chdir('basc')
    if firststart:
        time.sleep(0.1)
        os.mkdir('users')
        print('2/3')
        time.sleep(0.1)
        os.mkdir('pwd')
        print('3/3')
    main()
def main():
    global firststart
    global username
    if firststart:
        print('You are creating a first user.')
        username=input('Username:')
        pwd=getpass.getpass('New password:')
        repwd=getpass.getpass('Retype new password:')
        if pwd != repwd:
            print("Passwords didn't match.")
            main()
        hashpwd=hashlib.sha224(pwd)
        hashuser=hashlib.sha224(pwd)
        os.chdir('users')
        os.mkdir(username)
        os.chdir(homedir+'/basc/pwd')
        with open(hashuser.hexdigest,'w')as f:
            f.write(hashpwd.hexdigest)





run()       
