test = {
    'a': {'Id':['Tis ID'],
          'Longitude':['Tis Loing'],
          'Latitude':['Tis LAt']
          },
    'b': []
}

print(test['a']['Id'])
print(test['a'])
a = test['a']
id = test['a']['Id']
print(type(a))
print(type(id))

Test2 = {
    '1': [('Id1', 'Long1', 'Lat1'), ('Id2', 'Ling2', 'Lat2')],
    '2':'hi'
}

print(Test2['1'])
print(type(Test2['1']))
check = Test2['1']
print(check[1])

new_info = ('Id3', 'Long3', 'Lat3')
check.append(new_info)
print(check)

print(check[1][1])