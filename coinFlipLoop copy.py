# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 00:24:09 2023

@author: Acer
"""

from qiskit import QuantumCircuit, execute,Aer
from qiskit.visualization import plot_histogram
import random
qc = QuantumCircuit(1, 1)

#Three Sided Coin Randomizer

#first, a dumb one:
def numpyrandomizer():
     r2 = random.randint(0, 4)
     return r2

        
# Then a real one..still under development, please refer to the ThreeSidedCoin py file        
def TSCrandomizer():
    rqc = QuantumCircuit(3,3)
    rqc.h(0)
    rqc.h(2)
    rqc.ccx(0,2,1)
    rqc.barrier(0,1,2)
    
    #we don't use measure_all() because index 1 must be measured first (the order of the measurement matters)  
    rqc.measure(1,1)
    
    rqc.ccx(0,1,2)
    #measure the target
    rqc.measure(2,2)
    
    rqc.ccx(2,1,0)
    #measure the target
    rqc.measure(0,0)
    
    job = execute(rqc, Aer.get_backend('qasm_simulator'))

    counts = job.result().get_counts()
    r2 = list(counts) 
    return r2

def random_choice():
    qcc = QuantumCircuit(1,1)
    qcc.h(0)
    qcc.measure(0,0)
    job = execute(qcc, Aer.get_backend('qasm_simulator'))

    counts = job.result().get_counts()
    r1 = list(counts)[0]
    return r1


def Choice(true_choice):
     
     if true_choice == 1:
        qc.x(0)
        
     else :
        qc.i(0)
        
def QuantumChoice(true_choice):
     
     if true_choice == 1:
        qc.x(0)              
     elif true_choice == 0 :
        qc.i(0)
     elif true_choice == 2 :
        qc.h(0)        
        
def flip_coin(n):

    # #previously H
    # QuantumChoice(numpyrandomizer())

    # Choice(random_choice())
  
    # #previously H
    # QuantumChoice(numpyrandomizer())
    
    #for n number of turns
    for i in range(1,n+1):
        
        if i%2 == 0 :
            
            Choice(random_choice())
            
        else: QuantumChoice(numpyrandomizer())
    

    qc.measure(0, 0)

    
    job = execute(qc, Aer.get_backend('qasm_simulator'), shots=1024)

    counts = job.result().get_counts()
    #print(qc)
    if track:
        print(counts)

    try:
        out = 0
        counts['0']
    except:
        out = 1

    return out
track = False
count_Head = 0
count_Tail = 0

# problem:this for loop is consecutivly applying flip on the same circuit.

for i in range(0,100):
    

    bit = flip_coin(7)
    if bit == 0:
        count_Head += 1
    else:
        count_Tail += 1

print("Heads: " + str(count_Head))
print("Tails: " + str(count_Tail))

