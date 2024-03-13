
from sender import Sender
from receiver import Receiver
from OT import *


print("IKNP OT emulation")
print("You're Bob, a sender")

num1 = int(input("Please input matrix's length"))

Bob = Sender()
r = Bob.genRandomString(num1)
print("Your random string is ", r)

num2 = int(input("Please input the number of extended matrix R"))
R = Bob.strExtend(num2)
print("R = ")
for i in range(0, Bob.matrix_len):
    print(Bob.R[i])

T = Bob.genRandomMatrix()
T_ = Bob.MatrixSecretShare()

print("Bob's random matrix is")
for i in range(0, Bob.matrix_len):
    print(T[i])
    
print("Bob's shareing matrix is")
for i in range(0, Bob.matrix_len):
    print(T_[i])

print("You're Alice, a receiver")
Alice = Receiver()

print("Your random string is ", Alice.genRandomString(Bob.matrix_wide))

print("According to your random string, your matrix Q is")
ot = OT(Bob, Alice)
Alice.Q = ot.CorrelationOT()
for i in range(0, Bob.matrix_len):
    print(ot.CorrelationOT()[i])
    
print(Alice.OTInitialize())
print(Alice.OTtoSender())