
# NWQBench - A variable benchmark suite for near term quantum processors

NWQBench presents a large corpus of quantum benchmark routine generators, written in Python.
These benchmarking schemes generated are compatible with the languages
PyQuil, Q#, Qiskit, and Cirq. 

# Requirements

NWQBench operates on Python 3.7.0+, and the core packages described in requreiemnts.txt.
To install these, run the bash command:
```bash
pip install -r requirements.txt
```
One additional requirement for the complete package of NWQBench to work, is to install [q-convert](https://npmjs.com/package/q-convert).
Q-convert provides the functionality of translating QASM code into Cirq, Q# and PyQuil code. 

# Generating Benchmarks

NWQBench is comprised of multiple benchmark generators, under the NWQ_Bench directory. 
To generate a benchmark of size n, the python file is run with a sysarg n. This is as follows:

```bash
python BenchmarkName.py 5
```

In this example, we generate a BenchmarkName benchmark in QASM, comprising 5 qubits.
The sample generated will be a .qasm file (quantum assmebly language). The script that translates this into the alternative quantum programming languages is main.py

To convert these qasm files, simply run the following:

```bash
python main.py
```

This will iterate over all qasm files within the local directory, and generate the required other outputs.
Certain gates are not supported in all languages. If a user wants to mitigate this, they can set the transpile function to have a set of gates, or use the SUPPORTED_GATES file.
In this file, we describe a set of computationall complete gates that are used under the transpilation function in each NWQBench script.

# Generating Benchmarks with Docker

Because NWQBench's dependencies are pinned to 2021-era releases (Python 3.9,
qiskit 0.26, etc.), a Dockerfile is provided so you don't have to fight
setup/build toolchain issues locally. Build the image from the repo root:

```bash
docker build -t nwqbench .
```

Then generate QASM for one benchmark at a given size, or all of them, writing
output to a mounted `./output` directory:

```bash
docker run --rm -v "$(pwd)/output:/output" nwqbench bv 8
docker run --rm -v "$(pwd)/output:/output" nwqbench all 8
docker run --rm -v "$(pwd)/output:/output" nwqbench qnn_qf 4 3 2   # n k depth
```

The container runs `generate_benchmarks.py`, which invokes the matching
`NWQ_Bench/<name>/<script>.py` generator and copies its `qasm/*.qasm` output
into `/output/<name>/`. Notes:

- `boolean_satisfaction`, `grover_search`, and `statevector_encoder` hardcode
  their circuit size in the script itself and ignore the qubit argument.
- `adder` interprets its argument as the number of bits per operand (must be
  a multiple of 4), not the final qubit count.
- The container only produces QASM; converting to Cirq/Q#/PyQuil via
  `main.py` still requires `q-convert` (Node.js) and, for Q#, a .NET/IQ#
  install, which are intentionally not part of this image.

# Benchmarks Structure

Within NWQBench, the benchmark suite is structured as follows. Each directory is named after a quantum routine, such as wstate or adder. Within each quantum routine directory, there is a python file named after the algorithm. This file generates the QASM code responsible for the algorithm, at a given number of qubits, and is stored under the QASM directory in the algorithm directory. To generate QSharp,Pyquil and Cirq code, the main.py python file is induced. This script will process the prior generated QASM code into the desired languages. 

# Characterizing Benchmark Circuits 

To generate the circuit characterizing metrics, OpenQASMetric.py is included in the package. The metrics described in  "QASMBench: A Low-level QASM Benchmark Suite for NISQ Evaluation and Simulation" are computed using this script.
To compute these metrics, the following outline demonstrates the implementation:
```python
from OpenQASMetric import QASMetric
# The QASM-String you want to evaluate can be loaded simply reading a QASM file and storing it as a string
evaluation = QASMetric(QASM-String)
metrics = evaluation.evaluate_qasm()
```
## Citation format

For research articles, please cite our paper:

- Ang Li, Samuel Stein, Sriram Krishnamoorthy and James Ang, "QASMBench: A Low-level QASM Benchmark Suite for NISQ Evaluation and Simulation" [[arXiv:2005.13018]](https://arxiv.org/abs/2005.13018).

Bibtex:
```text
@article{li2021qasmbench,
    title={QASMBench: A Low-level QASM Benchmark Suite for NISQ Evaluation and Simulation},
    author={Li, Ang and Stein, Samuel and Krishnamoorthy, Sriram and Ang, James},
    journal={arXiv preprint arXiv:2005.13018},
    year={2021}
}

```



## License

This project is licensed under the BSD License, see [LICENSE](LICENSE) file for details.

# Acknowledgements 
**PNNL-IPID: 32218-E**

This material is based upon work supported by the U.S. Department of Energy, Office of Science,
National Quantum Information Science Research Centers, Co-design Center for Quantum Advantage (C2QA) under contract number DE-SC0012704.
The Pacific Northwest National Laboratory is operated by Battelle for the U.S. Department of Energy under contract DE-AC05-76RL01830.
