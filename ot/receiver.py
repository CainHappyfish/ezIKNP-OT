from random import Random
from sender import *

class Receiver(object):
    
    s = []
    Q = []
    
    q_xor = []
    q = []
    toSender = []
    
    num_ot = 0
    
    def __init__(self) -> None:
        pass

    def genRandomString(self, num):     # 这里的num为Sender的MatrixWide
        r = []
        
        random_instance = Random()      
        
        for i in range(0, num): 
            r.append(random_instance.randint(0,1))
            
        self.s = r
        
        return r
    
    def OTInitialize(self):
        qi =  ""
        q = []

        self.num_ot = int(len(self.Q) / len(self.s))
        
        for i in range(0, self.num_ot):
            q_str = [str(num) for num in self.Q[i]]
            qi = "".join(q_str)
            q.append(qi)
           
            
        self.q = q
        
        return q
    
    def OTtoSender(self):
        toSender = []
        q_xor = []

        for i in range(0, self.num_ot):
            qi_xor_str = []
            for j in range(0, len(self.Q[i])):
                qi_xor_str.append(str(self.s[j] ^ self.Q[i][j]))

            qi_xor = "".join(qi_xor_str)
            q_xor.append(qi_xor)
            
        self.q_xor = q_xor
        
        for i in range(0, self.num_ot):
            toSender.append([])
            toSender[i].append(self.q[i])
            toSender[i].append(self.q_xor[i])
            
        self.toSender = toSender
            
        return toSender
            
            
        