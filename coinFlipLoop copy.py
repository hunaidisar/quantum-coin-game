from qiskit import QuantumCircuit, execute,Aer
from qiskit.visualization import plot_histogram
import random
qc = QuantumCircuit(1, 1)



def random_choice():
    qcc = QuantumCircuit(1,1)
    qcc.h(0)
    qcc.measure(0,0)
    job = execute(qcc, Aer.get_backend('qasm_simulator'), shots=1024)

    counts = job.result().get_counts()
    x = list(counts)[0]
    return x


def Choice(true_choice):
     
     if true_choice == 1:
        qc.x(0)
        
       
     else :
        qc.i(0)
        
def flip_coin():


    qc.h(0)

    Choice(random_choice())
  

    qc.h(0)
    
    

    qc.measure(0, 0)

    
    job = execute(qc, Aer.get_backend('qasm_simulator'), shots=1024)

    counts = job.result().get_counts()
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

for i in range(0,100):
    

    bit = flip_coin()
    if bit == 0:
        count_Head += 1
    else:
        count_Tail += 1

print("Heads: " + str(count_Head))
print("Tails: " + str(count_Tail))

