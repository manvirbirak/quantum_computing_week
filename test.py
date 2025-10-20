from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt
import os

from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from qiskit.transpiler import generate_preset_pass_manager
from qiskit_ibm_runtime import EstimatorV2 as Estimator

# Create and save directory
os.makedirs("data", exist_ok=True)

# Create a simple 1-qubit circuit 
qc = QuantumCircuit(1)
qc.h(0)

# Get the statevector of the circuit
init_state = Statevector.from_instruction(qc)
print("Statevector:\n", init_state)

# Plot and save Bloch sphere representation
bloch_plot = plot_bloch_multivector(init_state)
plt.savefig("data/bloch_vector.png")

print("Bloch vector saved to data/bloch_vector.png")

 
# Create a new circuit with two qubits
qc = QuantumCircuit(2)
 
# Add a Hadamard gate to qubit 0
qc.h(0)
 
# Perform a controlled-X gate on qubit 1, controlled by qubit 0
qc.cx(0, 1)
 
qc.draw("mpl")
plt.savefig("data/mpl.png")

# build a 2 qubit, 2 classical circuit
circuit = QuantumCircuit(2,2)

# apply a NOT gate to qubit 0, currently 0,0
circuit.x(0)
# now 10

# apply a CNOT gate, which flips 2nd qubit value if first qubit is a 1
circuit.cx(0, 1)
# now 11

circuit.measure([0, 1], [0, 1])

print(circuit.draw())







