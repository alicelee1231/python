# 코딩 영역
import glob
import os

# txt_list1 = glob.glob1("../source/43-1","*.png", "*.txt", root_dir = None, recursive=False) 

# print("TXT file info : ", txt_list1, "Count : ",len(txt_list1))

# s = os.walk('../source/*.txt')
# for file in os.walk(s):
#     print(file)

# def search(dirname):
#     filenames = os.listdir(dirname)
#     for filename in filenames:
#         ext = os.walk(filename)[-1]
#         if ext == '.txt':
#             print(filename)
                        

# search("../source")


#방법 1
# txt_list1 = []
# png_list1 = []

# a = os.walk('../source/43-1')

# for root, dirnames, filenames in os.walk('../source/43-1'):
#         # print(root, '>>>', dirnames ,'>>>',filenames)
#     for f in filenames :
#         ext = f.split(".")[-1]
#         # print(ext)
#         if ext == "txt" :
#             txt_list1.append(f)
#         if ext == "png":
#             png_list1.append(f)
# print('TXT file info :', txt_list1, 'Count : ',len(txt_list1)) 
# print()
# print('PNG file info :', png_list1, 'Count : ',len(png_list1)) 

#방법 2

txt2 = glob.glob("../source/43-1/**/*.txt", recursive=True)
png2 = glob.glob("../source/43-1/**/*.png", recursive=True)
print('TXT file info :', txt2, 'Count : ',len(txt_list1)) 
# print()
print('PNG file info :', png2, 'Count : ',len(png_list1)) 