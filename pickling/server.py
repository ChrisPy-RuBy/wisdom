import socket
import pickle
from pickle_play import Gerkin

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # setup a TCP socket
s.bind((socket.gethostname(), 5234))  # This gives us our ip and the port
s.listen(5)  # The number of unaccepted connections before we start to refuse


gerkin = Gerkin(4, 2)
print(f"pre pickle gherkin: {gerkin.volume}")
pickled_gerkin = pickle.dumps(gerkin)

while True:
    clientsocket, address = s.accept()  # accept a connection
    print(f"Connection from {address} has been established")
    clientsocket.send(pickled_gerkin)
    clientsocket.close()
