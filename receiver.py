from random import Random

class Receiver(object):
    def __init__(self) -> None:
        pass

    def genRandomString(self, num):     # 这里的num为Sender的MatrixWide
        r = []
        random_instance = Random()      
        for i in range(0, num):
            r.append(random_instance.randint(0,1))
        return r