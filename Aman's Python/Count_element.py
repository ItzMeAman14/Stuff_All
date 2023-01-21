d = dict() 
line = 'This is a sample text'
for i in line:
    if i in d:
        d.update({i: d.get(i)+1})
    else:
        d.update({i: 1})

d = sorted(d.items())

print(d)