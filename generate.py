# 코딩 영역
import random 
from datetime import datetime

c = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
d = c.split()
print(d)
# b=random.sample("abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?",6)
print(b)
result = ''.join(s for s in b)
print(result)
a=[]
for i in range(0,5): 
    b = random.sample(c,6)
    result = ''.join(s for s in b)
    a.append(result)
    if len(a) <= 4 :
        continue
    print(a)


def generate_coupon_code(n):
    c = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

    code_list = []
    random.seed(None)

    for i in range(0,n):
        chosen = random.sample(c,6)
        code = "".join(chosen)
        code_list.append(code)
    return code_list
print(generate_coupon_code(5))










