d = dict(one = list(range(1,11)),two = list(range(11,23)),three=list(range(23,37)))
print(d.get("one"))
print(len(d))
p = d.get("one")

print(f'{list(d.keys())}')

print(d.items())
a = 0
for i in range(len(d)):
    a = a+1
print(a)
print(type(d))

#방법 1...
for i in range(len(d.get("one"))):
    i = i+1
print(f" key'one'has values {(d.get('one'))} -> total : {i}")

#방법 2..
c = (lambda i : i + 1 for i in range(len(d.get("one"))))

#방법 3..
print(d.items())
for k, v in d.items():
    print(f"key '{k}' has values {v} -> total {len(v)}")
    
