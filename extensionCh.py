# 코딩 영역
import os
# path = "../source/42-1"
# dir_list = os.listdir(path)

#방법 1
# g = []
# for k in range(len(dir_list)):
#     if dir_list[k][-1] == "g":
#       g.append(dir_list[k])
# print(f'PNG file info : {g}', f'Count : ', len(g))

# f = []
# for i in range(len(dir_list)):
#   if dir_list[i][-1] == "y":
#       f.append(dir_list[i])
# print(f'PY file info : {f}',f'Count :', len(f))

#방법 2
# files = os.listdir('../source/42-1')
# # print(files)

# png_list1 = []
# py_list1=[]

# for f in os.listdir('../source/42-1'):
#      # print(f)
#     # print(os.path.splitext(f))#파일가 확장자를 나눠줌
#     # print(f.split(".")[-1])
#     ext = f.split(".")[-1]
#     if ext == 'png':
#         png_list1.append(f)
#     if ext == 'py':
#         py_list1.append(f)

# print('PNG file info : ', png_list1, " Count : ", len(png_list1))
# print('PY file info : ', py_list1, " Count : ", len(py_list1))

#방법 3

import glob
png_list2 = glob.glob1("../source/42-1","*.png") 
py_list2 = glob.glob1("../source/42-1","*.py") 
print(py_list2)

print('PNG file info : ', png_list2, " Count : ", len(png_list2))
print('PY file info : ', py_list2, " Count : ", len(py_list2))