## 코딩 영역
import this
import json


phonebook = {
                0: {'Name': 'Kim', 'Phone': '45648733'},
                1: {'Name': 'Lee', 'Phone': '89376333'},
                2: {'Name': 'Park', 'Phone': '36457818'},
                3: {'Name': 'Chung', 'Phone': '76891234'},
                4: {'Name': 'Choi', 'Phone': '67451237'}
            }

# file_path = '../source/45-1.json'
# check = open(file_path,'a+')
# intro = ("Please select your choice :")

# while True :
#     print('-------MAIN MENU-----------')
#     print('1 : List phonebook')
#     print('2 : Add a new member')
#     print('3 : Delete a member')
#     print('4 : Program exit')
#     menu = int(input(intro))
    
#     if menu < 0 or menu > 4:
#         print("The menu can't be found")

#     elif menu == 1 : 
#         file = open(file_path,'r')
#         print(file.read())
#         file = open(file_path,'a+')
        
#         print()
#         print('---------------------------')
#         print(">> Data read is completed")
#         print('---------------------------')
        
#     elif menu == 2 :
#         name = input("Write a new member's name :")
#         phone = input("Phone number: ")
#         newNember = {
#             "name : " : name,
#             "phone :" : phone
#         }

#         # with open(file_path, "r") as check :
#         #     for key in check:
#         #         if name == check.values():
#         #             print("The member already exsit")
                
#         with open(file_path, 'a+') as file:
#             file.write(str(newNember))
         
#         # d= file.write( + '/n')
        
#         print()
#         print('---------------------------')
#         print(">> New member is added")
#         print('---------------------------')

#     elif menu == 3 :
#         deleted : input("Enter the name : ")
#         with open(file_path, 'r') as p:
#             if p.get() == deleted:
#                 p.remove()
#             else : 
#                 print("There is no person who have that name")

#     elif menu == 4 :
#         file = open(file_path,'r')
#         file.close()
#         print()
        
#         print('---------------------------')
#         print(">> The exit function is working")
#         print('---------------------------')
#         break




def list_phonebook(d):
    """List member in phone book."""
    for pid in d:
        print(pid+1)
        for p_info in d[pid]:
            print(p_info + ':', d[pid][p_info])
            # print('PID:',countMember(phonebook))

# def countMember():
#     for key, value in dict.items(phonebook):
#             count = 0
#             count += 1
#             print(count)  

def add_member(d):
    """Add a new member to the phone book. """
    print('/n Enter the infomation of the member')

    name = input("Name : ")
    phone = input("Phone : ")

    name_check = False
    for pid in d :
        if name == d[pid].get("Name"):
            name_check = True


    if name_check is True :
        print('/n# The member is already in the phone book')
    else:
        d[len(d)] = { 'Name' : name, "Phone" : phone}
        print('# The phone number has been added to the phone book')
    return d

def delete_member(d):
    """Delete the pointed name"""
    print('/nEnter the name')

    name = input('name: ')
    for pid in d:
        if name == d[pid].get("Name"):
            del d[pid]
            print('/n The member has been deleted')
            return d
    print('/n The member is not in the phone book')


def mainmenu():    
    while True :
        menu =  input("""
        '-------MAIN MENU-----------'
        '1 : List phonebook'
        '2 : Add a new member'
        '3 : Delete a member'
        '4 : Program exit'
         Please enter your choice :
       """)
        if menu == "1" :
            print('1')
            list_phonebook(phonebook)
            
        elif menu == "2":    
             add_member(phonebook)
        elif menu == "3": 
            delete_member(phonebook)
        elif menu == "4":
            print('exit')
            break

        else:
            print('/n Nemu can not be found')


mainmenu()
