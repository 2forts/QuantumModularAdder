# Code for [Optimized design of a quantum modular adder over GF(2^n − 1)](https://www.computer.org/csdl/magazine/mi)

**Francisco Orts, Elisabeth Ortega-Carrasco, and Ernestas Filatovas**

This repository contains all the written code for the paper "Optimized design of a quantum modular adder over GF(2^n − 1)", written by Francisco Orts, Elisabeth Ortega-Carrasco, and Ernestas Filatovas. This code allows the construction of a quantum modular adder circuit for binary numbers of any size. You only have to specify the numbers to add ($a$ and $b$), and the modulus $2^n$ (you only need to specify $n$). The number of bits in $a$ and $b$ must be $n$, so fill in leading zeros if necessary.

The code is written in Python. These libraries are necessary:
* cirq
* texlive-latex-base (only for pdf writing functionality)
* latexmk (only for pdf writing functionality)

**Files included:**
* [toffoli.py](https://github.com/2forts/QuantumMeter/blob/main/OptimizeConcatenatedCNOT.py): Replaces, as specified in the paper, controlled operations that can be simplified.
* [test_toffoli.py](https://github.com/2forts/QuantumMeter/blob/main/QuantumCostAnalyzer.py): Quantum circuit metric calculator.
* [temporary.py](https://github.com/2forts/QuantumMeter/blob/main/RemoveCNOT.py): Replaces CNOT operations with unit operations.
* [test_temporary.py](https://github.com/2forts/QuantumMeter/blob/main/RemoveUnusedQubits.py): Eliminates all unused qubits from a circuit, obtaining an equivalent and ordered one.
* [undo_temporary.py](https://github.com/2forts/QuantumMeter/blob/main/Example.py): Example of how to use the framework operations.
* [test_undotemporary.py](https://github.com/2forts/QuantumMeter/blob/main/comparator.qasm): Comparator obtained using the framework, as described in the paper.
* [builder.py](https://github.com/2forts/QuantumMeter/blob/main/comparator.qasm): Comparator obtained using the framework, as described in the paper.
* [how_to_use.py](https://github.com/2forts/QuantumMeter/blob/main/comparator.qasm): Comparator obtained using the framework, as described in the paper.
* [LiCENSE](https://github.com/2forts/QuantumMeter/blob/main/LICENSE): Apache License 2.0.

**How to cite:**

IMPORTANT: This work is currently under review.

If you are going to use all or part of this code in your own work, please quote it as follows

F. Orts, E. Ortega-Carrasco & E. Filatovas. (2024). Optimized design of a quantum modular adder over GF(2^n − 1). IEEE Micro.

BibTex:
```{bibtex}
@article{ortsadder2024,
  title={Optimized design of a quantum modular adder over GF(2^n − 1)},
  author={Orts, F., Ortega-Carrasco, E. and Filatovas, E.},
  journal={IEEE Micro},
  volume={?},
  number={?},
  pages={?},
  year={2024},
  publisher={Springer}
}
```
