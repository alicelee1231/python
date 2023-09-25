# 코딩 영역
import this
#모든 인자가 디폴트 값이 있는 경우 -> 디폴트 값은 뒤로 가야함
#모든 인자가 디폴트 값이 없는 경우
#디폴트 값 인자가 뒤로 
def greet(name,msg="Good morning!"):
    return "Hi! " +name+ ' '+ msg

# 실행
print(greet("Kim"))
print(greet("Park", "How do you do?"))

#예제
def add1(a,b=10,c=10):
    print(a,b,c)
    return(a+b+c)
print(add1(15))
print(add1(b=19, c=20, a=1))

#예제3 *packing & unpacking, 그리고 literable한 값임 -> 순서가 있다는 뜻
def add2(*d):
      tot = 0
      for i in d:
           tot += i
      return tot
print(add2(10,20,50))