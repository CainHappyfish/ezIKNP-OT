from sender import *
from receiver import *


class OT(object):
    ot_sender = Sender()
    ot_receicer = Receiver()
    
    def __init__(self, sender, receiver):
        self.sender = sender
        self.receiver = receiver
        
    def CorrelationOT(self):
        Q = []

        for i in range(0, len(self.receiver.s)):
            for j in range(0, self.sender.matrix_len):
                Q.append([])

                if self.receiver.s[i] == 0:
                    Q[i].append(self.sender.T[i][j])
                elif self.receiver.s[i] == 1:
                    Q[i].append(self.sender.T_[i][j])
                else:
                    print("Error")    
        
        self.Q = Q
        
        return Q
    
    def Transfer(self):
        for i in range(0, len(self.ot_sender.r)):
            if self.ot_sender.[i] == 1:
                
            
        
        