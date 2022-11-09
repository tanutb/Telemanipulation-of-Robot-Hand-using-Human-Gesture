import socket
import pickle


class Socket:
    def __init__(self,IP="localhost",PORT=1119) -> None:
        self.HOST_IP = IP
        self.PORT = PORT
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send_array_data(self,s,array):   
        data=pickle.dumps(array)
        s.send(data)

    ##### FOR SERVER ########
    def echo_server(self,function=print):         #pass function
        self.s.bind((self.HOST_IP,self.PORT))
        self.s.listen()
        print(f"Watting for connect")
        conn, addr = self.s.accept()
        if conn:
            print(f"Connected by {addr}")
            ## starttime = time.time() for timer
            while True:
                rev = conn.recv(1024)
                if rev:
                    data=pickle.loads(rev)
                    ## Funtion Something
                    function(data)
                    # conn.sendall(b"PBestkodlnw")
                else : 
                    #for didnt get any data from client
                    connect = self.is_still_connected(self.s)
                    if not connect :
                        break;

    def is_still_connected(self,sock):
        try:
            sock.sendall(b"ping")
            return True
        except:
            return False
                    

    ##### FOR CLIENT ########
    def client_connect(self):
        self.s.connect((self.HOST_IP, self.PORT))

    def client_send_data(self,array):
        print("sendded")
        self.send_array_data(self.s,array)
        # self.s.recv(1024)






        
