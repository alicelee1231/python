x =10
y =20
serialno = 308276567
n='kim'

ex1 = 'n = %s, s=%x, sum=%d' % (n,serialno,(x+y))
print(ex1)

ex2 = 'n={n}, s={serialno}, sum={sum}'.format(n=n,serialno=serialno, sum=x+y)
print(ex2)

ex3 = f'n={n}, s={serialno}, sum={x+y}'
print(ex3)

from string import Template

ex4 = 'n = $n, s= $serialno, sum=$sum'
t = Template(ex4)
print(t.substitute(n=n, serialno = serialno, sum= x +y))


#다양한 F스트링 연습

#진수
#(2진수 : b, 8진수 : o, 16진수: x|X)

k = 77
print(f"k 2 : {k:b}, k 8:{k:o}")
print(f"k 16 : {k:x}, k 16:{k:X}")


#구분기호
m = 1000000000000000000
print(f'm:{m:,}')

#정렬
#^:가운데, <:왼쪽, >:오른쪽

g=20

print(f'g:{g:10}')
print(f'g center:{g:^10},')
print(f'g left: {g:<10}.')
print(f'g right:{g:>10}.')

#채우기
print(f'center:{g:*^10}')


# print(d[group2][0][name], d[group2][0]['age'], d['type']['b'])
# pritn(d.get('group2')[0].get('name'),d.get('group2')[0].get('age'),d.get('type').get('b'))