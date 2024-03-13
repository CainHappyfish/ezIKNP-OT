from random import Random

class Sender(object):

    matrix_len = 0
    matrix_wide = 0

    def __init__(self) -> None:
        pass

    def genRandomString(self,num):
        r = []
        random_instance = Random()      # Random是一个类，需要实例化
        for i in range(0, num):
            r.append(random_instance.randint(0,1))
        return r

    def strExtend(self, str, num):
        self.matrix_len = len(str)
        self.matrix_wide = num
        R = []
        for i in range(0, len(str)):
            R.append([])
            for j in range(0, num):
                R[i].append(str[i])
        
        self.R = R
        
        return R
    
    def genRandomMatrix(self):
        T = []
        genRandomBit = Random()

        for i in range(0, self.matrix_len):
            for j in range(0, self.matrix_wide):
                T[i][j] = genRandomBit.randint(0,1)

        self.T = T

        return T
    
    def MatrixSecretShare(self):
        T_ = []

        for i in range(0, self.matrix_len):
            for j in range(0, self.matrix_wide):
                T_[i][j] = self.T[i][j] ^ self.R[i][j]

        self.T_ = T_

        return T_


    
    
test = Sender()
str = [1,1,0,0,1,0,1]    

for i in range(0, len(str)):
    print(test.strExtend(str, 4)[i])

        
    