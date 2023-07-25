from qiskit import QuantumCircuit, execute,Aer
from qiskit.visualization import plot_histogram
import random
qc = QuantumCircuit(1, 1)


        
def flip_coin():


    qc.h(0)

    qc.h(0)
  
    qc.h(0)

    qc.measure(0, 0)

    
    job = execute(qc, Aer.get_backend('qasm_simulator'), shots=1)

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
