from random import Random

class Sender(object):

    def genRandomtring(self,num):
        r = []
        random_instance = Random()      # Random是一个类，需要实例化
        for i in range(0, num):
            r.append(random_instance.randint(0,1))
        return r

    def strExtend(self, str, num):
        R = []
        for i in range(0, len(str)):
            R.append([])
            for j in range(0, num):
                R[i].append(str[i])
        return R
    
    
test = Sender()
str = [1,1,0,0,1,0,1]    

for i in range(0, len(str)):
    print(test.strExtend(str, 4)[i])

        
    