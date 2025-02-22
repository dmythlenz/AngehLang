use rayon::prelude::*;
use std::f64::consts::SQRT_2;

/// Represents a complex number used in quantum state vectors.
#[derive(Copy, Clone)]
struct Complex(f64, f64);

/// Represents the quantum state of a system of qubits.
pub struct QuantumState {
    state: Vec<Complex>,
    qubits: usize,
}

impl QuantumState {
    /// Creates a new quantum state with all qubits initialized to |0>.
    pub fn new(num_qubits: usize) -> Self {
        let size = 1 << num_qubits;
        let mut state = vec![Complex(0.0, 0.0); size];
        state[0] = Complex(1.0, 0.0);  // Initialize the first element to |0>
        Self { state, qubits: num_qubits }
    }

    /// Applies the Hadamard gate to a specified qubit.
    /// The Hadamard gate creates a superposition state from a basis state.
    pub fn apply_hadamard(&mut self, qubit: usize) {
        if qubit >= self.qubits {
            panic!("Qubit index out of bounds");
        }
        let step = 1 << qubit;
        self.state.par_chunks_mut(step << 1).for_each(|chunk| {
            for i in 0..step {
                let a = chunk[i];
                let b = chunk[i + step];
                chunk[i] = Complex((a.0 + b.0) / SQRT_2, (a.1 + b.1) / SQRT_2);
                chunk[i + step] = Complex((a.0 - b.0) / SQRT_2, (a.1 - b.1) / SQRT_2);
            }
        });
    }
}