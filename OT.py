from sender import *
from receiver import *
from Crypto.Hash import SHA256

class OT(object):
    ot_sender = Sender()
    ot_receicer = Receiver()
    
    def __init__(self, sender, receiver):
        self.ot_sender = sender
        self.ot_receiver = receiver
        
    def CorrelationOT(self):
        Q = []

        for i in range(0, len(self.ot_receiver.s)):
            for j in range(0, self.ot_sender.matrix_len):
                Q.append([])

                if self.ot_receiver.s[i] == 0:
                    Q[i].append(self.ot_sender.T[i][j])
                elif self.ot_receiver.s[i] == 1:
                    Q[i].append(self.ot_sender.T_[i][j])
                else:
                    print("Error")    
        
        self.Q = Q
        
        return Q
    
    def Transfer(self):
        message = []
        sha256 = SHA256.new()
        sha256.update(self.ot_receiver.toSender[0][1].encode("utf-8"))
        for i in range(0, len(self.ot_sender.r)):
            if self.ot_sender.r[i] == 1:
               
                sha256.update(self.ot_receiver.toSender[i][1].encode("utf-8"))
                message.append(sha256.hexdigest())
                print(sha256.hexdigest())
                print(message[i])
                # message[i] = self.Q[i][1]
            elif self.ot_sender.r[i] == 0:
               sha256.update(self.ot_receiver.toSender[i][0].encode("utf-8"))
               message.append(sha256.hexdigest())

                
                # message[i] = self.Q[i][0]
                
        return message
                
                
            
        
        