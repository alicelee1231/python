# 코딩 영역
import this

password1 = input()
# print(len(password1))

# def check(password1):
#     if len(password1) >= 8:
#        check_al()
#     else : 
#         print("비밀번호 조건이 맞지 않습니다.")
        
# def check_al(password1):
#     while len(password1) >=8:
#         print("비밀번호 조건이 맞지 않습니다.")
# check_al(password1)


while True:
    result = []
    psw = input("Enter the password:")
    print()


    if not any(i.isdigit() for i in psw):
        result.append("There must be at least one number.")
    if not any(i.isupper() for i in psw):
        result.append("There must be at least one capital letter.")
    if len(psw) < 8 :
        result.append("password should be 8 more number.")

    if len(result) == 0:
        print("correct password")
        break
    else:
        print("it is not enough to satisfy the password condition")
        for txt in result:
            print("-->", txt)