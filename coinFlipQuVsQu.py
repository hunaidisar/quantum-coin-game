from qiskit import QuantumCircuit, Aer, IBMQ, QuantumRegister, ClassicalRegister, execute
from qiskit.visualization import *
import matplotlib.pyplot as plt
import random
import inquirer

qc = QuantumCircuit(1, 1)
    




qc.h(0)
       
qc.h(0)

qc.h(0)
qc.measure(0, 0)


backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend, shots=1024)
output = job.result().get_counts()


if list(output.keys())[0] == '0':
    print("Heads, the first Qu-C wins")
    qc.draw('mpl')
if list(output.keys())[0] == '1':
    print("Tails,the second you win")
    qc.draw('mpl')

plot_histogram(output)

plt.show()








# What if, instead of quantum computer taking first turn, the classical human take the first turn ?
# What if, instead of representing head as , the tail is represented as  ?
# What if, instead of using fair coin, we used unfair coin ?
# What if, instead of playing against a classical human, the quantum computer plays with another quantum computer ?
# What if, instead of having 3 turns, there are  number of turns ?
# What if, instead of using all gates, restrict the use of some gates ?