#!/bin/bash

# Update package lists
sudo apt-get update

# Install necessary dependencies
sudo apt-get install -y antlr4 llvm-dev

# Upgrade pip and install Python dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install torch==1.12.0 torchvision==0.13.0 onnxruntime-gpu==1.10.0

# Run the build process
mkdir -p build
cd build
cmake ..
make -j$(nproc)

# Run tests
pytest ../tests/ --verbose
python ../benchmarks/performance_test.py 
#!/bin/bash
# install/offline_install.sh

function validate_environment {
  # Verify cryptographic chain
  openssl dgst -sha3-512 \
    -verify containment/quantum_certificates/master.pub \
    -signature self_test/validate_integrity.sig \
    self_test/validate_integrity.angeh
  
  # Check quantum test vectors
  ./static_binaries/quantum_simulator \
    -input self_test/test_cases.qdat \
    -expected self_test/expected_results.bin
}
# install/offline_install.sh
#!/bin/bash
# Air-Gapped Installation Script

function install_system {
  # Cryptographic Verification
  openssl sha3-512 \
    -verify containment/qcerts/master.pub \
    -signature self_test/integrity.sig \
    self_test/validate_integrity.angeh

  # Platform Detection
  case $(uname -m) in
    x86_64) bin="wings_linux_x64";;
    arm64) bin="wings_mac_arm64";;
    *) echo "Unsupported arch"; exit 1;;
  esac

  # Secure Deployment
  install -m 755 "static_binaries/$bin" /usr/local/bin/wings
  cp -r containment/ /opt/angehlang/
}