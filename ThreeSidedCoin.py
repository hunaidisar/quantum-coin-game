# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 00:52:43 2023

@author: Acer
"""
## UNFINISHED , the best I got is a four sided die.

from qiskit import QuantumCircuit, Aer, execute
#from qiskit.visualization import plot_histogram , plot_state_qsphere , plot_bloch_multivector


rqc = QuantumCircuit(3,3)

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
    print (rqc)
    print(counts)
    #print(r2)


TSCrandomizer()
