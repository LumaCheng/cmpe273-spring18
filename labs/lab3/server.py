import zmq
import time
import _thread


id = 0
user_msg = ""
sock2 =""

def start_socket():
    global sock2
    # ZeroMQ Context
    context = zmq.Context()

    # Define the socket using the "Context"
    sock2 = context.socket(zmq.PUB)
    sock2.bind("tcp://127.0.0.1:5680")

    context = zmq.Context()
    sock = context.socket(zmq.REP)
    sock.bind("tcp://127.0.0.1:5678")

    while True:
        message = sock.recv()
        message = message.decode()
        sock.send_string("")
        sock2.send_string(message)
        print(message)

if __name__ == '__main__':
    start_socket()
