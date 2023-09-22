import this
def tt(n):
    return str(n * 10)
x= list(map(tt,range(1,16)))
print(x)

y = list(map(lambda x : str(x * 10), range(1,16)))
print(y)

z= [str(x*10) for x in range(1,16)]
print(z)