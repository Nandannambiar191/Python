b = {"Name": "Nandan", "age": 10}
print(b["Name"])
print(b.get('age'))
b["age"] = 17
print(b)
b['address'] = 'City'
print(b)
b.pop('age')
print(b)
print("Address :", b.get('address'))
b.clear()
print(b)