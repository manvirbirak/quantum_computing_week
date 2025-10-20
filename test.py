from qiskit import QuantumCircuit
from qiskit.visualization import circuit_drawer
import os

# Create folder if it doesn't exist
os.makedirs("data", exist_ok=True)

# Create circuit
qc = QuantumCircuit(1, 1)
qc.measure(0, 0)

# Save the circuit as an image
circuit_drawer(qc, output='mpl', filename="data/quantum_circuit.png")

print("Circuit saved to data/quantum_circuit.png")

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt
import os

# Create and save directory
os.makedirs("data", exist_ok=True)

# Create a simple 1-qubit circuit (example: put in superposition)
qc = QuantumCircuit(1)
qc.h(0)

# Get the statevector of the circuit
init_state = Statevector.from_instruction(qc)
print("Statevector:\n", init_state)

# Plot and save Bloch sphere representation
bloch_plot = plot_bloch_multivector(init_state)
plt.savefig("data/bloch_vector.png")

print("Bloch vector saved to data/bloch_vector.png")

