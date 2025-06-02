from temporary import Temporary
from undo_temporary import UndoTemporary
import builder
import cirq

n = 5 
a = [1, 1, 0, 1, 1] # a = 11011 (27)
b = [1, 1, 1, 0, 0] # b = 00111 (7)

circuito = builder.build_circuit(a, b, n)
print(circuito)
simulator = cirq.Simulator()
result = simulator.run(circuito, repetitions=1)
print(result) # 27 + 7 = 34 mod 2^5 = 3 (00011)
