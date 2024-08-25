# Code for [Optimized design of a quantum modular adder over GF(2<sup>n</sup> − 1)](https://www.computer.org/csdl/magazine/mi)

**Francisco Orts, Elisabeth Ortega-Carrasco, and Ernestas Filatovas**

This repository contains all the written code for the paper "Optimized design of a quantum modular adder over GF(2<sup>n</sup> − 1)", written by Francisco Orts, Elisabeth Ortega-Carrasco, and Ernestas Filatovas. This code allows the construction of a quantum modular adder circuit for binary numbers of any size. You only have to specify the numbers to add ($a$ and $b$), and the modulus $2^n$ (you only need to specify $n$). The number of bits in $a$ and $b$ must be $n$, so fill in leading zeros if necessary.

The code is written in Python. These libraries are necessary:
* cirq
* texlive-latex-base (only for pdf writing functionality)
* latexmk (only for pdf writing functionality)

**Files included:**
* [toffoli.py](https://github.com/2forts/QuantumModularAdder/blob/main/toffoli.py): Implementation of the Toffoli gate used in the paper.
* [test_toffoli.py](https://github.com/2forts/QuantumModularAdder/blob/main/test_toffoli.py): Toffoli gate test.
* [temporary.py](https://github.com/2forts/QuantumModularAdder/blob/main/temporary.py): Implementation of the Temporary logical AND gate proposed by Gidney (see reference in paper).
* [test_temporary.py](https://github.com/2forts/QuantumModularAdder/blob/main/test_temporary.py): Temporary logical AND gate test.
* [undo_temporary.py](https://github.com/2forts/QuantumModularAdder/blob/main/undo_temporary.py): Uncomputation of the Temporary logical AND gate proposed by Jones (see reference in paper).
* [test_undotemporary.py](https://github.com/2forts/QuantumModularAdder/blob/main/test_undotemporary.py): Test of the uncomputation gate.
* [builder.py](https://github.com/2forts/QuantumModularAdder/blob/main/builder.py): Main code. Includes the method necessary to build the circuit for any specified size.
* [how_to_use.py](https://github.com/2forts/QuantumModularAdder/blob/main/how_to_use.py): Simple example of how to use the proposed code.
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
