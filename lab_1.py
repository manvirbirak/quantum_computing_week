from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt
import os

from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from qiskit.transpiler import generate_preset_pass_manager
from qiskit_ibm_runtime import EstimatorV2 as Estimator


qc = QuantumCircuit(1)
qc.x(0)
print(qc.draw())

qc.p(qc.pi/4, 0)

qc.draw(output='mpl')
print(qc.draw(output='mpl'))
