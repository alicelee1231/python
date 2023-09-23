# a = 20

# def test():
#     # 지역변수
#     a = 35
#     return a

# print('step1 : ', a)

# a = 100

# print('step2 : ', a)
# print('step3 : ', test())

a =20

def test():
    global a
    print(f'3 {a}') 
    a =35
    return a
print(f'1 {a}') # 35

a =100
print(f'2 {a}') #100
print(f'네번{test()}')  # 20
print(f'마지막 {a}')  #100