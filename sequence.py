# 코딩 영역
import this
x = ["grapes", "mango", "orange", "peach", "apple", "lime", "banana", "cherry", "tomato", "kiwi", "blueberry", "watermelon"]
ex2=[]
for i in x:
    if i == "apple" or i == "kiwi":
     ex2.append(i)
     print(ex2)
a = [1]
b = [2]
c = a + b

a = str(x.index("apple"))
print(str(a))

print(c)
# r = list(map(lambda b: b.upper(),filter(lambda a : a =='apple' or a=='kiwi',x)))
# print(r)

# ex1 = []
# for i in range(len(x)):
#     if x[i]=='apple' or x[i]=='kiwi':
#         ex1.append(x[i].upper())
# print(ex1)

# ex3 = [a.upper() for a in x if a=="apple" or a == "kiwi"]
# print(ex3)
