class QASMGenerator:
    def __init__(self):
        self.qubit_counter = 0
        self.code = []
        self.header = """OPENQASM 2.0;
include "qelib1.inc";\n"""
        
    def generate(self, ast):
        self.code.append(self.header)
        
        for node in ast:
            if node['type'] == 'qubit_declaration':
                self._allocate_qubit(node['name'])
            elif node['type'] == 'quantum_gate':
                self._apply_gate(node['gate'], node['targets'])
                
        return '\n'.join(self.code)
    
    def _allocate_qubit(self, name):
        self.code.append(f"qreg {name}[1];")
        
    def _apply_gate(self, gate, targets):
        if gate == 'entangle':
            self.code.append(f"h {targets[0]};")
            self.code.append(f"cx {targets[0]},{targets[1]};")