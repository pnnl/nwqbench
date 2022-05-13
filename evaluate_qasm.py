import os
import sys
import pathlib
import gc
from OpenQASMetric import QASMetric
import matplotlib.pyplot as plt
import json


if __name__ == '__main__':
    print("Starting Program...")
    path = str(pathlib.Path().absolute())
    print(path)
    path += "/NWQBench"
    files = []

    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.qasm' in file:
                files.append(os.path.join(r, file))
                print(f"Root:{r}")
                print(f"Directory:{d}")
                print(f"Files:{f}")

    suc = 0
    fail = 0
    results = {}
    # Print all available backends
    # Set simulator to the aer simulator (Similar gate selection to QasmSimulator, but QasmSimulator is deprecated)
    for file in files:
        with open(file, 'r') as loaded_file:
            try:
                loaded_qasm = loaded_file.read()
            except Exception as e:
                print(f"{file} failed to load")
                print(e)
                continue
        file_name = file.split("\\")[-1]
        print('-'*20)
        print(f"Metrics for {file_name}")
        print('-'*20)
        try:
            evaluation = QASMetric(loaded_qasm)
            metrics = evaluation.evaluate_qasm()
            results[str(metrics['qubit_count'])] = metrics
            suc +=1
        except Exception as e:
             print(e)
             print(f"{file_name} failed to evaluate")
             fail +=1
        with open(f"{file.strip('.qasm')}_results.json",'w') as file:
            json.dump(metrics,file)
    print(results)
    max_num = max([int(x) for x in results.keys()])
    min_num = min([int(x) for x in results.keys()])
    index_keys = [int(x) for x in results.keys()]
    keys = list(metrics.keys())
    result_track = [[] for _ in range(len(keys))]
    print(f"Total Success Rate: {100*suc/(suc+fail)}")