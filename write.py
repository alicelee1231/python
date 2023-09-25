import os

filenames = ["A","B","C","D","E","F"]
contents1 = ["python","js","rust","ruby","php"]
contents2 = [["python","js","rust","ruby","php"],["python","js","rust","ruby","php"],["python","js","rust","ruby","php"],["python","js","rust","ruby","php"],["python","js","rust","ruby","php"],["python","js","rust","ruby","php"]]

#방법1
def write_content1(filepath):
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    
    for n, c in zip(filenames, contents1):
        with open(filepath + n + '.txt','w')as file:
            file.write(c)
    
write_content1("../source/26-1/")

#방법2
def write_content2(filepath):
    if not os.path.exists(filepath):
        os.makedirs(filepath) #mkdir은 한 폴더만 생성이 가능함 makedirs는 ./a/b/c처럼 원하는 만큼 디렉토리를 생성할 수 있음
    
    for n, c in zip(filenames, contents1):
        with open(filepath + n + '.txt','w')as file:
            file.writelines(c + '\n' for c in c)
    
write_content1("../source/26-2/")