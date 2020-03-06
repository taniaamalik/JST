import numpy as np 
import random


def membuatArray(huruf):
    huruf=huruf.replace("#","1,").replace(".","-1,").replace("\n",'')
    arr = np.fromstring(huruf[:],dtype=int,sep=',')
    return arr

def inisialisasi(alfa, treshold, input):  
    # berat = [random.random() for _ in range(0, len(input))]
    berat = [0.1,0.2]
    # bias = random.random()
    bias = 0.5
    return (alfa, treshold, berat, bias)

def hitungOutput(x,w,bias):
    y = np.matmul(x,w)+bias
    return y

def updateBobot(w,bias,target, alfa,treshold,y):
    y = hitungOutput(x,w,bias)
    print("wlama = "+ str(w))
    w = w + alfa * (target-y) * x
    bias = bias + alfa * (target-y)
    return (w,bias)

# def HitungAdeline(array):




input = "##"
x = membuatArray(input)
t = 1.0
alfa, treshold, w, bias = inisialisasi(0.1,0.1,input)
print("data = " + str(x))
print("target = " + str(t))
print("alfa = " + str(alfa))
print("treshold = " + str(treshold))
print("berat = " + str(w))
print("bias = " + str(bias))
y=hitungOutput(x,w,bias)
print("y = " + str(y))
w,bias = updateBobot(w,bias,t,alfa,treshold,y)
print("w = " + str(w))
print("bias = " + str(bias))
print ("-------------------------------")
input = "#."
x = membuatArray(input)
t = -1
print("data = " + str(x))
print("target = " + str(t))
print("alfa = " + str(alfa))
print("treshold = " + str(treshold))
print("berat = " + str(w))
print("bias = " + str(bias))
y=hitungOutput(x,w,bias)
print("y = " + str(y))
w,bias = updateBobot(w,bias,t,alfa,treshold,y)
print("w = " + str(w))
print("bias = " + str(bias))
# print(membuatArray("#.#.#"))