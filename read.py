import os

def read_text_file1(file_path):
    outputs = []

    for file in os.listdir(file_path):
        if file.endswith(".txt"):
            target_path = f"{file_path}\{file}"

           # print(target_path)
        with open(target_path,'r')as f:
            outputs.append(f.read().strip('\n'))
    return outputs
print(read_text_file1("../source/27-1"))
print()

import glob

def read_text_file2(file_path):
    outputs = []
    for file in glob.glob(file_path + '\*.txt'):
        with open(file,'r')as f :
            outputs.append(f.read().strip('\n'))
    return outputs

print(read_text_file2('../source/27-1'))
print()