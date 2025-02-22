def generate_qir(ast):  
    # Converts AngehLang Entangle to Qiskit code  
    qc = QuantumCircuit()  
    qc.h(qubit1)  
    qc.cx(qubit1, qubit2)  
    return qasm.dumps(qc)  