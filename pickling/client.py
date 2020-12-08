import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP socket
s.connect((socket.gethostname(), 5234))

full_msg = b""
while True:
    msg = s.recv(8)
    if len(msg) <= 0:
        break
    full_msg += msg

de_pickled_gerkin = pickle.loads(full_msg)
print(f"post-pickled gerkin: {de_pickled_gerkin.volume}")
print(de_pickled_gerkin)
