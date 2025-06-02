import cirq

class Toffoli(cirq.Gate):
    def __init__(self):
        super(Toffoli, self)
    def _num_qubits_(self):
        return 3
    def _decompose_(self, qubits):
        c1, c2, t = qubits
        Tadj = cirq.inverse(cirq.T)

        yield cirq.H(t)
        yield cirq.T(c1)
        yield cirq.T(c2)
        yield cirq.T(t)
        yield cirq.CX(c2, c1)
        yield cirq.CX(t, c2)
        yield cirq.CX(c1, t)
        yield Tadj(c2)
        yield cirq.CX(c1, c2)
        yield Tadj(c1)
        yield Tadj(c2)
        yield cirq.T(t)
        yield cirq.CX(t, c2)
        yield cirq.CX(c1, t)
        yield cirq.CX(c2, c1)
        yield cirq.H(t)
        
    def _circuit_diagram_info_(self, args):
        return ["Toffoli"] * self.num_qubits()