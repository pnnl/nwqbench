
# NWQBench - A variable benchmark suite for near term quantum processors

NWQBench presents a large corpus of quantum benchmark routine generators, written in Python.
These benchmarking schemes generated are compatible with the languages
PyQuil, Q#, Qiskit, and Cirq.

# Requirements

NWQBench operates on Python 3.7.0+, and the core packages described in requirements.txt.
To install these, run the bash command:
```bash
pip install -r requirements.txt
```
One additional requirement for the complete package of NWQBench to work, is to install [q-convert](https://npmjs.com/package/q-convert).
Q-convert provides the functionality of translating QASM code into Cirq, Q#, and PyQuil code.

# Generating Benchmarks

NWQBench is comprised of multiple benchmark generators, under the NWQ_Bench directory.
To generate a benchmark of size n, the python file is run with a sysarg n. This is as follows:

```bash
python BenchmarkName.py 5
```

In this example, we generate a BenchmarkName benchmark in QASM, comprising 5 qubits.
The sample generated will be a .qasm file (quantum assembly language). The script that translates this into the alternative quantum programming languages is main.py.

To convert these qasm files, simply run the following:

```bash
python main.py
```

This will iterate over all qasm files within the local directory, and generate the required other outputs.
Certain gates are not supported in all languages. If a user wants to mitigate this, they can set the transpile function to have a set of gates, or use the SUPPORTED_GATES file.
In this file, we describe a set of computationally complete gates that are used under the transpilation function in each NWQBench script.

# Benchmarks Structure

Within NWQBench, the benchmark suite is structured as follows. Each directory is named after a quantum routine, such as w_state or adder. Within each quantum routine directory, there is a python file named after the algorithm. This file generates the QASM code responsible for the algorithm, at a given number of qubits, and is stored under the QASM directory in the algorithm directory. To generate QSharp, Pyquil, and Cirq code, the main.py python file is induced. This script will process the prior generated QASM code into the desired languages.

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
