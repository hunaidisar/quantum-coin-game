from qiskit import QuantumCircuit, Aer, QuantumRegister ,ClassicalRegister, execute
from qiskit.visualization import *
import matplotlib.pyplot as plt
import numpy as np
from math import pi
import random
import inquirer

qc =QuantumCircuit(1, 1)




def Choice():
        questions = [  inquirer.List('gate',  message="Choose a gate to apply:", choices=['Identity', 'Flip'],
            ),
]

        answers = inquirer.prompt(questions)
        if answers['gate'] == 'Identity':
                
                 
                 qc.i(0)
   

        if answers['gate'] == 'Flip':
                 qc.x(0)





qc.h(0)


Choice()
qc.h(0)

        






qc.measure(0, 0)


backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend, shots=1)
output = job.result().get_counts()


if list(output.keys())[0] == '0':
    print("Heads,Qu-C wins")
   
if list(output.keys())[0] == '1':
    print("Tails, you win")

print(list(output.keys())[0] )

qc.draw('mpl')
plot_histogram(output)
plt.show()








# What if, instead of quantum computer taking first turn, the classical human take the first turn ?
# What if, instead of representing head as , the tail is represented as  ?
# What if, instead of using fair coin, we used unfair coin ?
# What if, instead of playing against a classical human, the quantum computer plays with another quantum computer ?
# What if, instead of having 3 turns, there are n number of turns ?
# What if, instead of using all gates, restrict the use of some gates ?







