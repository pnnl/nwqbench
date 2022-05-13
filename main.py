import os
import sys
import pathlib
import gc
from OpenQASMetric import QASMetric
import matplotlib.pyplot as plt
import json


def translate_qcode(file_name,target_file_name,code_style,parent_directory):
    print(target_file_name)
    print(parent_directory)
    os.system(f"q-convert -i {file_name} -s qasm -o {parent_directory+'/'+target_file_name} -d {code_style} -w")

if __name__ == '__main__':
    print("Starting Program...")
    path = str(pathlib.Path().absolute())
    print(path)
    path += "/NWQ_Bench"
    with open('qsharp_py.py','r') as file:
        qsharp_evaluator = file.read()
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.qasm' in file:
                files.append(os.path.join(r, file))
    code_style = ["pyquil","cirq","qsharp"]
    trailing = [".py",".py",".qs"]
    for file in files:
        for style,ending in zip(code_style,trailing):
            target_dir = '\\'.join(file.split('\\')[:-2])
            if not os.path.isdir(target_dir+"/"+style):
                os.mkdir(target_dir+"/"+style)
            new_file_name = file.strip('.qasm') + "_" + style + ending
            new_file_name = new_file_name.split('\\')[-1]
            tar = target_dir + "/" + style
            if style == "qsharp":
                tar = target_dir+"/"+style+"/"+new_file_name
                tar = tar.rstrip('.qs')
                if not os.path.isdir(tar):
                    os.mkdir(tar)
                with open(tar+'/'+'qsharp_py.py','w') as f:
                    f.write(qsharp_evaluator)
            translate_qcode(file,new_file_name,style,tar)