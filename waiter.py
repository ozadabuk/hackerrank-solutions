import time
import sys

start_time = time.time()

def getPrimes(upper):
    primes = []
    for num in range(2, sys.maxsize):
        isPrime = True
        if num > 1:
            for i in range(2, num + 1):
                if i != num and num % i == 0:
                    isPrime = False
        if isPrime:
            primes.append(num)
            if len(primes) == upper:
                break
    return primes

f = open("input.txt", "r")
lines = f.readlines()
params = lines[0].rstrip("\n")
params1 = params.split(" ")
n = int(params1[0])
q = int(params1[1])
prime = getPrimes(q)
print(str(time.time() - start_time) + " to get prime numbers")
#print(str(len(prime)) + " primes")
print("n:" + str(n) + " q:" + str(q))
num = lines[1].rstrip("\n")
num = num.split(" ")
#print(num)
number = []
for i in range(len(num)):
    number.append(int(num[i]))
print(number)
print(len(number))
#number = [3, 4, 7, 6, 5]
#number = [3, 3, 4, 4, 9]

A = []
B = [[]]

A.append(number)

for i in range(0, q):
    #print("i:" + str(i) + " len(A):" + str(len(A)) + " len(B):" + str(len(B)))
    A.append([])
    B.append([])
    #print("A[" + str(i) + "]:" + str(A[i]))
    while A[i]:
        #print(len(A[i]))
        plate = A[i].pop()
        #print(str(plate) + " % " + str(prime[i]) + " = " + str(plate % prime[i]))
        if plate % prime[i] == 0:
            #print("Add to Bi")
            B[i+1].append(plate)
        else:
            #print("Add to Ai")
            A[i+1].append(plate)

results = []
for pile in B:
    while pile:
        results.append(pile.pop())
for pile in A:
    while pile:
        results.append(pile.pop())
print(time.time() - start_time)
print(results)

#print("DONE!")
