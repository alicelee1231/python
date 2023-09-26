# 코딩 영역
import this

# d = {"group1":[
#                 {'name': 'Park', 'age': '32', 'sex': 'Male'},
#                 {'name': 'Cho', 'age': '44', 'sex': 'Female'},
#                 {'name': 'Kang', 'age': '39', 'sex': 'Female', 'married': 'No'}
#               ],
#      "group2":[
#                 {'name': 'Kim', 'age': '23', 'sex': 'Male', 'married': 'Yes'},
#                 {'name': 'Lee', 'age': '37', 'sex': 'Male', 'married': 'No'}
#               ],
#      "type" : {"a": "employee", "b": "officer", "c": "director", "d": "manager", "e": "service provider"}
#     }

# c= {"group1" : {'name': 'Jung', 'age': '22', 'sex': 'Male', 'married': 'Yes'}} 
    
    
# d['group1'].append({'name': 'Jung', 'age': '22', 'sex': 'Male', 'married': 'Yes'})
# d['type'].update({"f":"engineer"})
# print(d)


d.get('group1').append({'name': 'Jung', 'age': '22', 'sex': 'Male', 'married': 'Yes'})
d.get('type')['f']='engineer'
print(d)