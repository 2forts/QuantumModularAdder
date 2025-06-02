import cirq

class Temporary(cirq.Gate):
    def __init__(self):
        super(Temporary, self)
    def _num_qubits_(self):
        return 3
    def _decompose_(self, qubits):
        c1, c2, t = qubits
        Tadj = cirq.inverse(cirq.T)

        yield cirq.H(t)
        yield cirq.T(t)
        yield cirq.CX(c1, t)
        yield cirq.CX(c2, t)
        yield cirq.CX(t,c2)
        yield cirq.CX(t,c1)
        yield Tadj(c1)
        yield Tadj(c2)
        yield cirq.T(t)
        yield cirq.CX(t,c1)
        yield cirq.CX(t,c2)
        yield cirq.H(t)
        yield cirq.S(t)
    def _circuit_diagram_info_(self, args):
        return ["Temporary"] * self.num_qubits()

temporary = Temporary()

