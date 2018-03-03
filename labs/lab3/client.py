import zmq
import sys
import threading
import time
import re



sock2 = ""
flag = 0
uname = ""
self_flag = 0



def start_socket():
    global sock2
    global uname

    context = zmq.Context()

    # SUB
    sock2 = context.socket(zmq.SUB)
    sock2.setsockopt_string(zmq.SUBSCRIBE, "")
    sock2.connect("tcp://127.0.0.1:5680")

    threading.Thread(target=wait_server_msg).start()

    try:
        while True:
            register_to_server()

    except KeyboardInterrupt:
        print('end')

def register_to_server():
    global flag
    global self_flag
    global uname
    context = zmq.Context()
    sock = context.socket(zmq.REQ)
    sock.connect("tcp://127.0.0.1:5678")
    self_flag = 1
    if flag == 0:
        uname = " ".join(sys.argv[1:])
        sock.send_string(uname)
        print('User[{}] Connected to the chat server.'.format(uname))
        flag = 1
    else:
        new_msg = input('[{}] > '.format(uname))
        sock.send_string('[{}]: '.format(uname) + new_msg)


def wait_server_msg():
    global sock2
    global self_flag
    global uname
    while True:
        msg = sock2.recv()
        msg = msg.decode()

        if re.match('(\[{}\]:.+)'.format(uname),msg):
            continue;
        else:
            if re.search('(^\[[a-zA-Z]+\]:.+)',msg):
                #print(msg)
                sys.stdout.write('\x1b[2K\r'+ msg + '\n' + '[{}] > '.format(uname) )
                #print('\n' + msg)

if __name__ == '__main__':
    start_socket()
