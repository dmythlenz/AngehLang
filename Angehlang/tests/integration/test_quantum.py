def test_quantum_entanglement():  
    code = "Entangle q1, q2 with coherence=0.99;"  
    qasm = compile_to_qasm(code)  
    assert "h q[0];" in qasm  # Hadamard gate on q1
    assert "cx q[0],q[1];" in qasm  # CNOT gate between q1 and q2