# 코딩 영역
import this


# k = input()
# print(type(len(k)))
# with open('../source/44-1.txt','w+') as p:
#     # while len(k) > 0:
#     print(k)
    
    
file_path = '../source/44-1.txt'
intro = "Select a menu number : "
file = open(file_path,'a+')

while True :
    print('---------------------------')
    print("1. read")
    print("2. write")
    print("3. exit")
    print('---------------------------')

    menu = int(input(intro))

    if menu == 1 :
        file = open(file_path, 'r')
        print(file.read())

        file = open(file_path,'a+')
        print()
        print('---------------------------')
        print(">> Data read is completed")
        print('---------------------------')
    elif menu == 2 :

        text = input('Write a text')
        file.write(text + '/n')
        print()

        print('---------------------------')
        print(">> Data write is completed")
        print('---------------------------')
    
    elif menu == 3 :
        file.close()
        print()
        
        print('---------------------------')
        print(">> The function of data exit is working")
        print('---------------------------')
        break
