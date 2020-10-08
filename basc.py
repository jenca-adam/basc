#!/usr/bin/python
import os,getpass,hashlib,time
firststart=False
username=''
homedir=os.getcwd()
class User:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.hashuser=sha224(username)
        self.hashpwd=sha224(password)
    def auth(self):
        pwddir=homedir+'/basc/pwd'
        os.chdir(pwddir)
        try:
            with open(self.hashuser) as file:
                if file.read()!=self.hashpwd:
                    print('Login failed')
                    return
        except IOError:
            print ('Login failed')
            return
        import httplib2
        h=httplib2.Http('.cache')
        try:
            response,content=h.request('http://bascos.org/all.txt')
        except httplib2.ServerNotFoundError:
            print('connection--error:could not connect to server. Error code 404')
            return
        self.prompt()
                
def sha224(string):
    return hashlib.sha224(string.encode('utf-8')).hexdigest()
def run():
    global firststart
    try:
        import httplib2
        print('Httplib2 installed.OK')
    except ImportError:
        print('Installing safe-connection library...')
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
    login()
def login():
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
        os.chdir('users')
        os.mkdir(username)
        os.chdir(homedir+'/basc/pwd')
        with open(sha224(username),'w')as f:
            f.write(sha224(pwd))
    else:
        username=input('Username:')
        pwd=getpass.getpass()
        user=User(username,pwd)
        user.auth()
        login()
run()       
