// bootstrap/micro_rust/simulator.rs
#![no_std]
#![no_main]

use quantum_lib::embedded_sim;
use containment::preverified::qasm_gates;

#[panic_handler]
fn panic(_info: &core::panic::PanicInfo) -> ! { loop {} }

#[no_mangle]
pub extern "C" fn simulate(code: *const u8) -> i32 {
  let circuit = unsafe { parse_qasm(code) };
  let result = embedded_sim::run(circuit);
  write_result(SRAM_ADDRESS, result);
  0
}
// bootstrap/micro_rust/simulator.rs
#![no_std]
#![feature(start)]

#[start]
pub fn _start(qasm: *const u8) -> ! {
  let circuit = parse_qasm(unsafe { 
    core::slice::from_raw_parts(qasm, 1024) 
  });
  
  let result = simulate(
    circuit,
    SimFlags::AIRGAP_MODE
  );
  
  write_to_vram(result.as_bytes());
  loop {}
}

#[panic_handler]
fn panic(_: &core::panic::PanicInfo) -> ! { loop {} }