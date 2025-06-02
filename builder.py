from temporary import Temporary
from undo_temporary import UndoTemporary
import cirq

def build_circuit(a, b, n):
    temporary = Temporary()
    undo_temporary = UndoTemporary()
    reg = cirq.LineQubit.range(2*n+2)

    circuito = cirq.Circuit()

    # Steps 1 and 2
    circuito.append(cirq.X(reg[0]))
    for i in range(n):
        if b[i] == 1:
            circuito.append(cirq.X(reg[2*i+1]))
        if a[i] == 1:
            circuito.append(cirq.X(reg[2*n+1]))
        circuito.append(temporary(reg[2*i+1],reg[2*n+1],reg[2*i+2]))
        if a[i] == 1:
            circuito.append(cirq.X(reg[2*i+1]))
            circuito.append(cirq.X(reg[2*n+1]))

        circuito.append(cirq.CCX(reg[2*i],reg[2*i+1],reg[2*i+2]))
     
    for i in reversed(range(n-1)):
        circuito.append(cirq.CCX(reg[2*i],reg[2*i+1],reg[2*i+2]))

    # Step 3
    circuito.append(cirq.CX(reg[2*n], reg[0]))
    circuito.append(cirq.X(reg[0]))

    # Step 4
    for i in range(n-1):
        circuito.append(cirq.CCX(reg[2*i],reg[2*i+1],reg[2*i+2]))
    circuito.append(cirq.CX(reg[2*(n-1)], reg[2*(n-1)+1]))

    for i in reversed(range(n-1)):
        circuito.append(cirq.CCX(reg[2*i],reg[2*i+1],reg[2*i+2]))

        if a[i] == 1:
            circuito.append(cirq.X(reg[2*i+1]))
            circuito.append(cirq.X(reg[2*n+1]))
        circuito.append(undo_temporary(reg[2*i+1],reg[2*n+1],reg[2*i+2]))
        if a[i] == 1:
            circuito.append(cirq.X(reg[2*i+1]))
            circuito.append(cirq.X(reg[2*n+1]))
        circuito.append(cirq.CX(reg[2*i], reg[2*i+1]))

    # Step 5
    circuito.append(cirq.CX(reg[2*n], reg[0]))

    for i in range(n):
        circuito.append(cirq.measure(reg[2*i+1], key = 's' + str(i)))

    return circuito
