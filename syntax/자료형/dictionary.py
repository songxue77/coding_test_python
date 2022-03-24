dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}

dic['email'] = '123@abc.com'

del dic['email']

# Key 리스트 만들기(keys)
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.keys()) # dict_keys(['name', 'phone', 'birth'])
list(a.keys())

# Value 리스트 만들기(values)
print(a.values()) # dict_values(['pey', '0119993323', '1118'])

print(a.items()) # dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')])

# Key: Value 쌍 모두 지우기(clear)
a.clear()

# Key로 Value얻기(get)
a.get('name') # a['name']와 같음
a.get('foo', 'bar') # foo에 해당하는 값이 없으면 bar 리턴

# 해당 Key가 딕셔너리 안에 있는지 조사하기(in)
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print('name' in a) # True
print('email' in a) # False
