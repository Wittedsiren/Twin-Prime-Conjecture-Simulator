# Twin Prime Conjecture Simulator
import threading
primeNumbers = []

print('----------------------------------------')

def primeNumTest(num):
    prime = True
    if num == 1:
        prime = False
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                prime = False
                break
    return prime

factor = 10
numberofsets = 3
RANGE = 1_0
twinPrimeNum = 0

def checkforTwin(x):
    if primeNumTest(x) :

        if primeNumTest(x - 2) and x-2 > 1 :
            # print(x-2,x,'Twin Prime\n')
            return 1
            
    return 0

for r in range(numberofsets):
    RANGE = 10
    RANGE = RANGE * (10**r)
    print(RANGE,r)
    for x in range(RANGE + 1):
        twinPrimeNum += checkforTwin(x)
    # print('\nThere is a total of ',twinPrimeNum,' twin primes')
    # print(twinPrimeNum/RANGE*100,'% are twin prime', 'out of',RANGE,'numbers\n=========')
    print(twinPrimeNum, 'twin primes', 'out of',RANGE,'numbers\n=========')
    twinPrimeNum = 0


