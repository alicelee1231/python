# 코딩 영역
import this
d = {'a': 'apple', 'b': 'grape'}
d['c'] = 'banana'
d['d']= 'kiwi'
print(d.keys())

e = {'a': 'apple', 'b': 'grape'}
e.update({'c': 'banana', 'd': 'kiwi'})
print(e)

# 코딩 영역
import this
d = {'a': 17,'b': 114,'c': 247, 'd': 362, 'e': 220, 'f': 728, 'g': -283, 'h': 922}
print(d.get("a")+d.get("b"))
print(sum(d.values()))
print(d.keys())
a = 0
for i in d.values():
    a += i
print(a)