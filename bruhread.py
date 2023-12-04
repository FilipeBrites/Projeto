import time
import os
import random

def __stock_():
    stk = open("stock.txt", "r")
    for line in stk:
        print(line)
    stk.close()

name_store = "Feira Virtual"
P = "Progress:|__________|"
num1 = 0.1

os.system('cls')
time.sleep(0.5)

for i  in range (1,8):
    os.system('cls')
    print(P)
    if i % 2:
        num2 = random.randint(3,5)
        P = P.replace('_','|',1)
        time.sleep(num1 * num2)
    else:
        num2 = random.randint(3,5)
        P = P.replace('_','|',2)
        time.sleep(num1 * num2)
time.sleep(2)
P = P.replace('_','|',1)
os.system('cls')
print(P)

time.sleep(1)
os.system('cls')
print("Welcome")
time.sleep(1.5)
os.system('cls')
print("This is the " + name_store)
time.sleep(1.5)
os.system('cls')
print("Here we show u how many games we have in stock for ur customers to buy.")
time.sleep(3)
os.system('cls')

__stock_()