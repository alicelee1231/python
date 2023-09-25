# 코딩 영역
import this

#sigma method 만들기

#방법 1
n = 0
for i in range(1,11):
    n = i + n
print(n)

#방법2
def sigma_sum(n):
    tot = 0
    for i in range(1,n+1):
        tot = tot + i
    return tot
print(sigma_sum(10))

#방법 3
def sigma_sum2(n):
    return n * (n+1)//2
print(sigma_sum2(10))

# 방법 4
def sigma_sum3(n):
    return sum(range(n+1))
print(sigma_sum3(10))