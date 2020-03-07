import numpy as np

def membuatArray(huruf):
    huruf=huruf.replace("#","1,").replace(".","-1,").replace("\n",'')
    arr = np.fromstring(huruf[:],dtype=int,sep=',')
    return arr

def hitungOutput(x,w,bias):
    v = np.matmul(x,w)+bias
    return v

def fungsiAktivasi(v):
    if(v>=0):
        return 1
    else:
        return -1

def menyamakan(t,y):
        if t==y:
            return "sesuai"
        else:
            return "tidak"

input = "#."
x = membuatArray(input)
t = 1
w =[0.4153,0.386799] 
bias=-0.357223
print("data = " + str(x))
print("target = " + str(t))
print("berat = " + str(w))
print("bias = " + str(bias))
v=hitungOutput(x,w,bias)
print("v = " + str(v))
y=fungsiAktivasi(v)
print("y = " + str(y))
print("apakah sesuai dengan target? " + menyamakan(t,y))