# # 코딩 영역
# import this
# with open('../source/41-1.txt')as a:
#     b = list(a)
#     # print(len(b))
#     # print(b[:2])
#     for i in range(len(b)):
#          # print(b[i])
#        v=b[i].find(",")
#        m = b[:v]
#        # print(m)
#        n = b[i][0]
#        if n == 'C':
#         print(b[i])
#        else : 
#            continue

def read_text_file(file_path):
    value_list = []
    with open(file_path,'r')as f :
        # print(f.readline())
        lines = f.readlines()

        for line in lines:
            country, value = line.rstrip().split(",")
            print(value)
            if country.lower().startswith('c'): #if country.lower()[0]== "c"
                # print(country)
                value_list.append(int(value))
    return value_list
result = read_text_file("../source/41-1.txt")
print(result)
print(sum(result))