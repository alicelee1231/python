user_data = {"name" : "dd", "age" : 20, "email" : "ddd@ddd.com"}

# 1
# for data in user_data:
#     print(f"{data}:{user_data[data]}")

# 2
for data  in user_data.items():
    print(f"{data[0]} : {data[1]}")