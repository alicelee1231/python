# 코딩 영역
import time
# c=0
# def time1():
#     for i in range(1,7):
#         c = c + 0.5
# a = 0
# n =.5
# for i in range(1,7):
#     a = a+0.5
#     n += 0.5
#     time.sleep(n)
#     if n > 3.5:
#         break
#     print(a)

#방법1
# for i in [.5,1,1.5,2,2.5,3]:
#     time.sleep(i)
#     print(i)

#방법2
# k=0
# while True:
#     time.sleep(k)
#     k += 0.5
#     if k >= 3.5 :
#         break
#     print(k)

#방법3



def sleep_out(n=1):
    time.sleep(n)
    print(sleep_out(n))
for n in[.5,1,1.5,2,2.5,3,3.5]:
    sleep_out(n)

