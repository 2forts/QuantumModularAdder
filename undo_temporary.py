import cirq

class UndoTemporary(cirq.Gate):
    def __init__(self):
        super(UndoTemporary, self)
    def _num_qubits_(self):
        return 3
    def _decompose_(self, qubits):
        c1, c2, t = qubits

        #yield cirq.H(t)
        yield cirq.measure(t, key='a')
        yield cirq.CZ(c1, c2).with_classical_controls('a')
    def _circuit_diagram_info_(self, args):
        return ["UndoTemporary"] * self.num_qubits()
