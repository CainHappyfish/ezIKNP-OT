from random import Random

class Sender(object):

    r = ""
    matrix_len = 0
    matrix_wide = 0
    T = []
    T_ = []

    def __init__(self) -> None:
        pass

    def genRandomString(self, num):
        
        r = []
        random_instance = Random()      # Random是一个类，需要实例化
        for i in range(0, num):
            r.append(random_instance.randint(0,1))
            
        self.r = r
        
        return r

    def strExtend(self, num):
        self.matrix_len = len(self.r)
        self.matrix_wide = num
        R = []
        for i in range(0, len(self.r)):
            R.append([])
            for j in range(0, num):
                R[i].append(self.r[i])
        
        self.R = R
        
        return R
    
    def genRandomMatrix(self):
        T = []
        genRandomBit = Random()

        for i in range(0, self.matrix_len):
            T.append([])
            for j in range(0, self.matrix_wide):
                T[i].append(genRandomBit.randint(0,1))

        self.T = T

        return T
    
    def MatrixSecretShare(self):
        T_ = []


        for i in range(0, self.matrix_len):
            T_.append([])
            for j in range(0, self.matrix_wide):
                T_[i].append(self.T[i][j] ^ self.R[i][j]) 

        self.T_ = T_

        return T_


    
    
# test = Sender()
# str = [1,1,0,0,1,0,1]    

# for i in range(0, len(str)):
#     print(test.strExtend(str, 4)[i], "R", test.matrix_wide)

# for i in range(0, len(str)):
#     print(test.genRandomMatrix()[i], "T")

# for i in range(0, len(str)):
#     print(test.MatrixSecretShare()[i], "T_")        
  