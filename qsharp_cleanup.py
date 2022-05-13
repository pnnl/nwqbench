import os
import pathlib
import re
;
class qsharp_clean():
    def __init__(self,text):
        # Dictionary indicating a common operation not supported, linked to n_operations and operation
        self.OPERATION_TRANSLATE = { "yy" : ["Ry",2],
                                     "zz" : ["Rz",2],
                                     "xx" : ["Rx",2]}
        # Reconstruction goes: Pass in control qubits, pass in action qubits, pass in parameters
        self.RECONSTRUCTION_STRING = {"yy": (lambda x : f"Ry({x['Parameters'][0]},{x['ActionQubits'][0]});\nRy({x['Parameters'][0]},{x['ActionQubits'][1]});"),
                                      "zz": (lambda x : f"Rz({x['Parameters'][0]},{x['ActionQubits'][0]});\nRz({x['Parameters'][0]},{x['ActionQubits'][1]});"),
                                      "xx": (lambda x : f"Rx({x['Parameters'][0]},{x['ActionQubits'][0]});\nRx({x['Parameters'][0]},{x['ActionQubits'][1]});")}
        self.start_text = None
        self.end_text = None
        self.circuit_text = None
        self.find_circuit_definition(text)
        self.clean_circuit_text()
        self.recompile_text()

    def get_operation(self,line):
        operation = line.split('(')[0]
        return operation

    def find_circuit_definition(self,text):
        # Strip prepended information
        break_string = "operation Circuit()"
        start_text = text.find(break_string)
        self.start_text = text[:start_text+len(break_string)]
        text = text[start_text+len(break_string):]
        end_text =text.find("ResetAll")
        self.end_text = text[end_text:]
        self.circuit_text = text[:end_text]
        self.text = text

    def clean_circuit_text(self):
        text_list = self.circuit_text.split('\n')
        text_list = [a.strip(' ') for a in text_list]
        for index,line in enumerate(text_list):
            operation = self.get_operation(line)
            operation = operation.strip(' ')
            if operation in list(self.OPERATION_TRANSLATE.keys()):
                print(f"Warning! {operation} not supported!")
                params = self.extract_parameters(line)
                text_list[index] = self.replace_unsupported_operation(operation,params)
        self.new_text = '\n'.join(text_list)


    def extract_parameters(self,line):
        m = re.search(r"\((.*?)\)", line)
        m.group(1)
        # Assumption : No line will have multiple operations.
        data = m[1]
        parameters = {}
        control_qubits = re.findall(r"(qubits\[[A-Za-z0-9_]+\])", data)
        action_qubits = re.findall(r"(qubits\[[A-Za-z0-9_]+\])", data)
        gate_param = re.findall(r'[-+]?\d*\.?\d+',data)
        # Currently control qubits = action qubits.
        # Not developed as use case not found
        gate_param = [x for x in gate_param if "." in x]
        parameters['ControlQubits'] = []
        parameters['Parameters'] = gate_param
        parameters['ActionQubits'] = action_qubits
        print(parameters)
        return parameters


    def replace_unsupported_operation(self,operation,parameters):
        replacement_information = self.RECONSTRUCTION_STRING[operation](parameters)
        return replacement_information

    def recompile_text(self):
        self.recompiled_text = self.start_text+self.new_text+self.end_text

    def get_cleaned_text(self):
        return self.recompiled_text

if __name__ == "__main__":
    print("Starting Program...")
    print(qsharp_clean(text).get_cleaned_text())
    path = str(pathlib.Path().absolute())
    print(path)
    path += "/NWQBench"
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.qs' in file:
                files.append(os.path.join(r, file))
    for file in files:
        print(file)
        with open(file,'r') as raw_text:
            txt = raw_text.read()
            cleaned_text = qsharp_clean(txt).get_cleaned_text()
        with open(file,'w') as new_file:
            new_file.write(cleaned_text)