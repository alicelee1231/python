import os

def read_text_file(filepath):
    outputs = []
    for file in os.listdir(filepath):
        if file.endswith(".txt"):
            target_path = f"{filepath}/{file}"
            with open(target_path, 'r') as f:
                outputs.append(f.read().strip('\n'))
    return outputs

print(read_text_file("../source/27-1"))
print()

import glob

def read_text_file2(filepath):
    outputs = []
    for file in glob.glob(filepath + '/*.txt'):
        with open(file,'r')as f :
            outputs.append(f.read().strip('\n'))
    return outputs
print(read_text_file2("../source/27-1"))