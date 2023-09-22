# 코딩 영역
import this

x = [32,30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0, -6, -8,-10,-12]
e = []
for a in x:
    if a >= 0 :
        a = a -2
    elif a < 0 :
        a = a + 2
    e.append(a)
    
print(e)

ex1 = []
for i in range(30,-12,-2):
    ex1.append(i)
print(ex1)


ex2 = list(range(30,-12,-2))
print(ex2)
# list(lambda a : a -2,range(30,-12,-2))