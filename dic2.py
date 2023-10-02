# 코딩 영역

l = ["Red", "Green", "Black", "Blue", "Orange", "Purple"]
result1 = list(enumerate(l))
result1_dic = {int:i for int,i in enumerate(l)}
result2 = {int:i for int,i in enumerate(l,start=100)}
print(result1_dic)
print(result2)
print(type(result1))

d1 = dict(enumerate(l))
print(d1)
print("EEEeee")

dic= {}
for i in range(0,6):
    dic[i] = l[i]
print(dic)