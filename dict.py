# 코딩 영역
import this
d = {'a': 8, 'b': 33, 'c': 15, 'd': 26, 'e': 12, 'f': 120}

c = dict(filter(lambda e : e[1]>=25,d.items()))
print(c)

ex2 = {k:v for k,v in d.items() if v >=25}
print(ex2)
