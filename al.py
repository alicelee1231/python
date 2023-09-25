# 코딩 영역
import this

# a = []
# for i in range(64,90):
#     i = i + 1
#     print(chr(i))


def write(filepath):
    with open(filepath,"w")as file:
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            file.write(letter + " ")
print(write("../source/23-1.txt"))


import string

def write2(filepath):
    with open(filepath,"w") as file:
        for letter in string.ascii_uppercase:
            file.write(letter + "\n")
print(write2("../source/23-1.txt"))