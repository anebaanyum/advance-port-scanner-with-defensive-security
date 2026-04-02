import socket as s
import threading as th

target_web = str(input("ENTER A TARGET WEBSITE : "))
open_port = set()

def scan_port(port):

    sock = s.socket(s.AF_INET,s.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((target_web,port))

    if result == 0 :

        open_port.add(port)
    
    sock.close()

threads = []

for port in range(1,65535) :

    thr = th.Thread(target=scan_port, args=(port,))
    
    threads.append(th)
    thr.start()


print("\n=====OPEN PORTS======\n")

for port in open_port :

    print(f"port {port} are opened")

    print("\n============= LENGTH===========\n")

print(f"Total Opened Port Is : {len(open_port)}")
                                                  

#defensive system

from utils import save_log
import socket

target = "127.0.0.1"

for port in range(1, 100):  # test کیلئے 100 رکھو
    s = socket.socket()
    s.settimeout(0.5)

    try:
        s.connect((target, port))
        print(f"Port {port} OPEN")
        save_log(target, port, "OPEN")
    except:
        save_log(target, port, "CLOSED")
    finally:
        s.close()
