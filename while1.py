# count = 1

# while True:
#     print(f"{count}바퀴째")
#     count +=1
#     if count == 11:
#         break

count = 0

while True:
    count +=1
    if count == 19:
        print("I need some breake")
        continue
    print(f"{count}바퀴째")
    if count == 20:
        break
print("over")