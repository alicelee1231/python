# 코딩 영역
import this
d = {'USA': 36, 'Germany': 17,'France':32, 'Australia': 77, 'South Africa': 99, 'India': 108, 'South Korea': 200}

# print(d['France'])
# print(d.keys())
# a = input().lower()
# for i in range(len(d)):
#     if d.keys() != a:
#      print('No results were found for your search.')
#      print(a)

#방법 1
# def search_dict(word):
#     try:
#         c = dict((new_k.lower(),new_val) for new_k, new_val in d.items())
       
#         return c[word]
#     except: 
#         return 'No results were found for your search.'

# txt = input().lower()
# print(search_dict(txt))


#방법2
def search_dic(word):
    c = dict((new_k.lower(), new_val) for new_k, new_val in d.items())
    return c.get(word, 'No results were found for your search.')


txt = input().lower()
print(search_dict(txt))