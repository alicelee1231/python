# import time 
# # 모듈은 IMPORT로 써야함
# import random
# import os

# print(1)
# time.sleep(2)
# print(2)

# for i in range(1,10):
#     print(f"{i}:안녕")
#     time.sleep(1)

# x = random.random()
# print(x)

# x = random.randint(1,20)
# print(x)



# x = list(range(1,10))
# print(x)

# print(os.getcwd())
# print(os.listdir())

class User:
    def __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email = email

    def hello(self):
        print("heelkkk")

user_1=User("dd",12,"ddd")
user_1.hello()
print(user_1.name)