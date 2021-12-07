import os
import subprocess
from random2 import randrange

def root_permission():
    user = str(subprocess.check_output('whoami',shell=True),'utf-8')
    user=user.replace('\n','')
    if ( user != 'root'):
        print("\033[1;32mPlease run as root")
        exit()

root_permission()

def header(i, name):
    print("\033[1;37m {} \t\t\t \033[1;31m {}".format(i, name))

def header1(i, name):
    if len(i)>10:
        print("\033[1;37m {} \t\t\t \033[1;31m {}".format(i, name))
    elif len(i)>6:
        print("\033[1;37m {} \t\t\t\t \033[1;31m {}".format(i, name))
    else:
        print("\033[1;37m {} \t\t\t\t\t \033[1;31m {}".format(i, name))


def banner(k):
    print('\033[1;3{}m m    m                                    mmmmm           m   \n #    #  mmm   m mm    mmm   m   m         #   "#  mmm   mm#mm \n #mmmm# #" "#  #"  #  #"  #  "m m"         #mmm#" #" "#    #   \n #    # #   #  #   #  #""""   #m#    """   #      #   #    #   \n #    # "#m#"  #   #  "#mm"   "#           #      "#m#"    "mm \n                              m"                               \n                             ""  \n'.format(k))

def port_list():
    i=21
    name='FTP'
    header(i, name)
    i=22
    name='SSH'
    header(i, name)
    i=23
    name='TELNET'
    header(i, name)
    i=25
    name='SMTP'
    header(i, name)
    i=53
    name='DNS'
    header(i, name)
    i=80
    name='HTTP'
    header(i, name)
    i=110
    name='POP3'
    header(i, name)
    i=115
    name='SFTP'
    header(i, name)
    i=135
    name='RPC'
    header(i, name)
    i=139
    name='NETBIOS'
    header(i, name)
    i=143
    name='IMAP'
    header(i, name)
    i=194
    name='IRC'
    header(i, name)
    i=443
    name='SSL'
    header(i, name)
    i=445
    name='SMB'
    header(i, name)
    i=1433
    name='MSSQL'
    header(i, name)
    i=3306
    name='MYSQL'
    header(i, name)
    i=25565
    name='MINECRAFT'
    header(i, name)

def about():
    print('\n\033[1;31mCreate By     \t\t\t        \033[1;36m>\033[1;37m \tIHA\n\033[1;31mWritten Language\t        \t\033[1;36m>\033[1;37m \tPython3 & shell\n\033[1;31mSupported Operation System\t\t\033[1;36m>\033[1;37m \tKali Linux\n\033[1;31mPurpose\t\t\t\t\t\033[1;36m>\033[1;37m\tCatch Attacker in Local Network\n\033[1;31mGitHub \t\t\t\t\t\033[1;36m>\033[1;37m\thttps://github.com/IHA-arch\n')
    
def port_name(port):
    port=int(port)
    if port == 21:
        name='FTP'
    elif port == 22:
        name='SSH'
    elif port == 23:
        name='TELNET'
    elif port == 25:
        name='SMTP'
    elif port == 53:
        name='DNS'
    elif port == 80:
        name='HTTP'
    elif port == 110:
        name='POP3'
    elif port == 115:
        name='SFTP'
    elif port == 135:
        name='RPC'
    elif port == 139:
        name='NETBIOS'
    elif port == 143:
        name='IMAP'
    elif port == 194:
        name='IRC'
    elif port == 443:
        name='SSL'
    elif port == 445:
        name='SMB'
    elif port == 1433:
        name='MSSQL'
    elif port == 3306:
        name='MYSQL'
    elif port == 25565:
        name='MINECRAFT'
    else:
        name='**'
    return name

def Menu():
    i="about"
    name="Tool Creater information"
    header1(i, name)
    i="help"
    name="Show Help"
    header1(i, name)
    i='port list'
    name='show default port list'
    header1(i, name)
    i='set ip <ip>'
    name='\t  set listening ip for honeypot'
    header1(i, name)
    i='set port <port no.>'
    name='set port for honeypot'
    header1(i, name)
    i='set port all'
    name='\t  set all default port for honeypot'
    header1(i, name)
    i='start'
    name='start honeypot server'
    header1(i, name)
    i='show'
    name='show listening ip and ports set by user'
    header1(i, name)
    i='reset'
    name='remove set ip and ports from honeypot'
    header1(i, name)
    i='exit'
    name = 'Exit Honeypot'
    header1(i, name)
    i='clear'
    name = 'Clear Screen'
    header1(i, name)
    i='stop'
    name = 'Close Another xterm windows and stop honeypot server'
    header1(i, name)

global file_path
file_path='/usr/share/honeypot_IHA/honeypot.py'
global path
path='/usr/share/honeypot_IHA/ipport'
global create_path
create_path='/usr/share/honeypot_IHA/fakeservice'
cmd='echo 0 > {}'.format(create_path)
os.system(cmd)

def check_file():
    if os.path.isfile(file_path) is True:
        os.remove(file_path)
    filettr=open(file_path, 'a')
    head='import socket\nimport honeypotweb\nimport subprocess\nfrom threading import Thread\nip="127.0.0.1"\nprint("listening at::",ip)\nprint("\\033[1;31m   Target IP\t\tTarget HostName\t  System PORT\t      Target PORT      Fake Service")\n'
    filettr.write(head)
    filettr.close()
    http_port_for_all()
    iipp='ipport'
    if os.path.isfile(iipp) is True:
        os.remove(iipp)


def validIP(address):
    parts = address.split(".")
    if len(parts) != 4:
        return False
    for item in parts:
        try:
            if not 0 <= int(item) <= 255:
                return False
        except ValueError:
            return False
    return True

def set_ip(user):
    ip=user.split(' ')
    ip=ip[2]
    if validIP(ip) is True:
        filettr=open(file_path, 'r')
        kr=filettr.read()
        cmd="cat {} | grep 'ip='".format(file_path)
        grep_ip = subprocess.check_output(cmd, shell=True)
        grep_ip=str(grep_ip, 'utf-8')
        grep_ip=grep_ip.replace('\n', '')
        grep_ip=grep_ip.split('=')
        grep_ip=grep_ip[1].replace('"', '')
        filettr.close()
        kr=kr.replace(grep_ip, ip)
        filettr=open(file_path, 'w')
        filettr.write(kr)
        filettr.close()

    else:
        print("\033[1;31mInvalid IP \033[1;37m{}".format(ip))
    
def create():
    cmd='cat {}'.format(create_path)
    j=str(subprocess.check_output(cmd, shell=True), 'utf-8')
    j=j.replace('\n','')
    k=int(j)
    k=k+1
    cmd='echo "{}" > {}'.format(k, create_path)
    os.system(cmd)
    return j



def set_port(user):
    try:
        port=user.split(' ')
        port=port[2]
        
    except:
        port=''
    portlist=[21, 22, 23, 25, 53, 80, 110, 115, 135, 139, 143, 194, 443, 445, 1433, 3306, 25565]
    if not port:
        print("Usage: set port <port number>")
    else:
        try:
            port=int(port)
        except:
            print("Entered port is not intger, please enter intger")
            port='bypass'

        if port == 'bypass':
            pass
        elif port == 80:
            print("port 80 setup as default automatically")
        elif port in portlist:
            setff=open(path, 'a')
            pport="port="+str(port)
            setff.write(pport)
            setff.write("\n")
            setff.close()
            name=port_name(port)
            server_write(name, port)
        else:
            name='not_define' + create()
            setff=open(path, 'a')
            pport="port="+str(port)
            setff.write(pport)
            setff.write("\n")
            setff.close()
            server_write(name, port)
            print("\033[1;31mWarning::\033[1;35mPort '{}' is not in default portlist".format(port))
            
def check_set_port(user):
    try:
        port=user.split(' ')
        port=int(port[2])
    except:
        port=''
    if not port:
        pass
    else:
        if os.path.isfile(path) is True:
            try:
                data=open(path, 'r')
                ddr=data.read()
                if str(port) in ddr:
                    print("\033[1;32mPORT \033[1;35m{} \033[1;32mAlready define".format(str(port)))
                else:
                    set_port(user)            
            except:
                pass
        else:
            set_port(user)

def check_set_ports(user):
    try:
        port=user.split(' ')
        port = port[2]
        if port == 'all':
            user='set port 21'
            check_set_port(user)
            user='set port 22'
            check_set_port(user)
            user='set port 23'
            check_set_port(user)
            user='set port 25'
            check_set_port(user)
            user='set port 53'
            check_set_port(user)
            user='set port 110'
            check_set_port(user)
            user='set port 115'
            check_set_port(user)
            user='set port 135'
            check_set_port(user)
            user='set port 139'
            check_set_port(user)
            user='set port 143'
            check_set_port(user)
            user='set port 194'
            check_set_port(user)
            user='set port 443'
            check_set_port(user)
            user='set port 445'
            check_set_port(user)
            user='set port 1433'
            check_set_port(user)
            user='set port 3306'
            check_set_port(user)
            user='set port 25565'
            check_set_port(user)
        else:
            check_set_port(user)
    except:
        print("Usage: set port <port number>")

def http_port_for_all():
    server='def http():\n    get_path=\'/usr/share/honeypot_IHA/getdata\'\n    server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)\n    server.bind((ip, int(80)))\n    kk=open(get_path,\'w\')\n    kk.write(\'0000\')\n    kk.close()\n    while True:\n        server.listen()\n        client, addr = server.accept()\n        hostname=socket.gethostbyaddr(addr[0])\n        if len(hostname[0]) < 6:\n            print("\\033[1;37m",addr[0],"\\t\\t",hostname[0],"\\t\\t\\t80\\t\\t",addr[1],"\\t\\tHTTP")\n        else:\n            print("\\033[1;37m",addr[0],"\\t\\t",hostname[0],"\\t\\t80\\t\\t",addr[1],"\\t\\tHTTP")  \n        try:           \n            client.send(honeypotweb.fake_ftp_page_html())\n            data = str(client.recv(1024), \'utf-8\')\n        except:\n            pass\n        try:\n            gg=\'cat \' + get_path + \'|grep "User-Agent:"\'\n            ggr=str(subprocess.check_output(gg, shell=True),\'utf-8\')\n        except:\n            ggr=\'\'\n\n        try:\n            kk=open(get_path, \'w\')\n            kk.write(data)\n            kk.close()\n\n            grep_cmd=\'cat \' + get_path + \'|grep "User-Agent:"\'\n            user_agent=str(subprocess.check_output(grep_cmd, shell=True),\'utf-8\')\n            if ggr == user_agent:\n                pass\n            else:\n                print("\\033[1;31m",user_agent, end=\'\')\n        except:\n            pass\n\n                \n\nhttp_server=Thread(target=http)\nhttp_server.start()\n'

    honey=open(file_path, 'a')
    honey.write(server)
    honey.close()
    
    
def server_write(name, port):
    server='def {}():\n    server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)\n    server.bind((ip, int({})))\n    while True:\n        server.listen()\n        client, addr = server.accept()\n        hostname=socket.gethostbyaddr(addr[0])\n        if len(hostname[0]) < 6:\n            print("\\033[1;37m",addr[0],"\\t\\t",hostname[0],"\\t\\t\\t{}\\t\\t",addr[1],"\\t\\t{}")\n        else:\n            print("\\033[1;37m",addr[0],"\\t\\t",hostname[0],"\\t\\t{}\\t\\t",addr[1],"\\t\\t{}")\n\n{}_server=Thread(target={})\n{}_server.start()\n'.format(name,port,port,name,port,name,name,name,name)

    honey=open(file_path,'a')
    honey.write(server)
    honey.close()


def show_set_info():
    if os.path.isfile(path) is True:
        try:
            ip_cmd='cat {} | grep "ip="'.format(file_path)
            g_ip=str(subprocess.check_output(ip_cmd, shell=True), 'utf-8')
            g_ip=g_ip.split('=')
            g_ip=g_ip[1].replace("\n",'')
            g_ip=g_ip.replace('"','')
            print("IP==>",g_ip)
        except:
            print("IP==>127.0.0.1")
        
        try:
            port_cmd='cat {} | grep "port="'.format(path)
            g_port=str(subprocess.check_output(port_cmd, shell=True), 'utf-8')
            g_port=g_port.replace('\n', ' | ')
            g_port=g_port.replace('port=','')
            print("PORT==>| 80 |",g_port)
        except:
            print("PORT==>| 80 |")
    else:
        print("IP==>127.0.0.1")
        print("PORT==>| 80 |")

def server_start():
    show_set_info()
    kill_cmd='killall xterm >/dev/null 2>&1'
    os.system(kill_cmd)
    start="xterm -title 'Honey-Pot::server' -fa 'Monospace' -fs 9 -geometry 100x20 -bg black -fg green -ls -xrm 'XTerm*selectToClipboard: true' -hold -e 'python3 /usr/share/honeypot_IHA/honeypot.py'&"
    os.system(start)
    
def server_stop():
    kill_cmd='killall xterm >/dev/null 2>&1'
    os.system(kill_cmd)

def root():
    k=7
    banner(k)
    check_file()
    condition=True
    f='first'
    while condition:
        try:
            user = input("\033[1;31mHoneypot\033[1;34m>>\033[1;37m")
            if not user:
                pass
            elif user == 'help':
                Menu()
            elif user == 'about':
                about()
            elif user == 'port list':
                port_list()
            elif 'set port' in user:
                check_set_ports(user)
            elif 'set ip' in user:
                set_ip(user)
            elif user == 'show':
                show_set_info()
            elif user == 'start':
                server_start()
            elif user == 'exit' or user == 'quit':
                print("\033[1;32m Exiting....")
                condition=False
                server_stop()
                exit()
            elif user == 'reset':
                check_file()
            elif user == 'clear':
                os.system("clear")
                k=randrange(9)
                banner(k)
            elif user == 'stop':
                server_stop()
            else:
                print("\033[1;39minvalid command \033[1;36m: {}".format(user))
                if f == 'first':
                    print("\033[1;39mtype '\033[1;36mhelp\033[1;39m' for more information")
                    f = 'chang'

        except KeyboardInterrupt:
            print("\n", end='')


root()
    
