# print("hello world")
# print("hello world"[:-1])

# name = "lee" 
# # 변수는 대소문자 구분하고 숫자 안됨, 특수문자도 _햣 밖에 안됨, if, else 등등 이름으로 안됨
# print(type(name))


# today = "수요일"
# if today == "월요일":
#     print("출근")
# elif today == "일요일":
#     print("today is holiday")
# else:
#     print("what day is it?")

# if today == "일요일":
#     print("오늘은 쉬는날")

pizza = True
hamburger = True

# if not pizza:
#     print("yaho~ i have a pizza and a hamburger")
# elif hamburger:
#     print("wow, i have a hamburger")
# else:
#     print("I have a nothing")


# food = ["pizza","hamburger",111]

# print(food[-1])
# food.append("love")
# print(food)

# food.insert(1,"hahah")
# print(food)
# food.remove(111)
# print(food)

# food1 = ["a","s","e","w"]
# food1.sort(reverse=True)
# food1.sort()
# print(food1)
# food1[0]="akakk"
# print(food1)

user = {"name":"sam", "job":"programmer"}

print(user)

user["age"] = 20
print(type(user))
del user["name"]

print(user)