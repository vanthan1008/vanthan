import os

path = 'C:\\than\\data'
filename = 'dulieu.txt'

#cách 1:
f = open("C:/than/data/dulieu.txt", 'rt')
content = f.readlines()
f.close()
print(content)

#cách 2:
with open(os.path.join(path, filename), 'rt') as f:
    content = f.readlines()
print(content)

#cách 3:
try:
    f = open(os.path.join(path, filename), 'rt')
    content = f.readlines()
    f.close()
    print(content)
except Exception as e:
    print('error:',e)

print('ketthuc chuong trinh')



