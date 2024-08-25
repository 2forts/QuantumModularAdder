from temporary import Temporary
from undo_temporary import UndoTemporary
import cirq

c =1
n = 4
x = [0, 1, 0, 1]
y = [0, 1, 1, 0]
temporary = Temporary()
undo = UndoTemporary()
reg = cirq.LineQubit.range(3*n+1)

circuito = cirq.Circuit()
if c == 1:
    circuito.append(cirq.X(reg[0]))
for i in range(n):
    if x[i] == 1:
        circuito.append(cirq.X(reg[3*i+1]))
    if y[i] == 1:
        circuito.append(cirq.X(reg[3*i+2]))
    circuito.append(temporary(reg[3*i+1],reg[3*i+2],reg[3*i+3]))
    circuito.append(undo(reg[3*i+1],reg[3*i+2],reg[3*i+3]))

    circuito.append(cirq.measure(reg[3*i+1], key = 'x' + str(i)))
    circuito.append(cirq.measure(reg[3*i+2], key = 'y' + str(i)))
    
circuito.append(cirq.measure(reg[3], reg[6], reg[9], reg[12],key = 'AND'))
print(circuito)
simulator = cirq.Simulator()
result = simulator.run(circuito, repetitions=1)
print(result)
