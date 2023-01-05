import socket
import threading
import time
import random
import string
global zzz,is_start
is_start=0
zzz=[]

host = "103.178.234.247"
port = 80
headers = """\
POST /dangky.php HTTP/1.1\r
Content-Type: application/x-www-form-urlencoded\r
Content-Length: {content_length}\r
Host: {host}\r
Connection: close\r
\r\n"""
def id_generator(size=5, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
def start(host,port,headers):
    global zzz,is_start
    for __ in range(0,1,1):
        name=id_generator()
        while name in zzz:
            name=id_generator()
        zzz.append(name)
        while is_start==0:
            time.sleep(2)
        for _ in range(0,1,1):
            try:
                print('{0}{1}'.format(str(name),str(_)))
                passw=id_generator(6)
                print(passw)
                body_bytes = 'uname={0}{1}&passw={2}&repassw={2}'.format(str(name),str(_),str(passw)).encode('ascii')
                header_bytes = headers.format(
                    content_length=len(body_bytes),
                    host=str(host) + ":" + str(port)
                ).encode('iso-8859-1')
                payload = header_bytes + body_bytes
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((host, port))
                s.sendall(payload)
                print('{0}{1}'.format(str(name),str(_)))
            except KeyboardInterrupt:
                exit()
            except TimeoutError:
                print('timeout: {0}{1}'.format(str(name),str(_)))
                pass
            except ConnectionRefusedError:
                print('refused: {0}{1}'.format(str(name),str(_)))
                pass
            except:
                pass
            try:
                s.close()
            except:
                continue

for _ in range(0,1,1):
    print('thread '+str(_))
    threading.Thread(target=start, args=(host,port,headers,)).start()
while 1:
    is_start=1
    time.sleep(100)