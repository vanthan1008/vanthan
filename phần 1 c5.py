#câu 5 Viết chương trình chính thực hiện theo kịch bản sau:
#a. Sinh ngẫu nhiên list các số thực;
#b. Lưu list vào tập tin văn bản;
#c. Sắp xếp list theo chiều giảm dần;
#d. Lưu list ở câu (c) vào tập tin văn bản;
#e. Tìm kiếm số n trong list ở câu (d);
import random

n=int(input('n= '))
def sinh_ngau_nhien_list():
    a = 9
    b = 2
    c= [(b-a)*random.random()+a for i in range(n)]
    return c
print(sinh_ngau_nhien_list())
#Lưu list vào tập tin văn bản;
import pickle
import os
path = 'C:\\than\\dulieu01'
filename = 'luutru.txt'
with open(os.path.join(path, filename), 'wb') as f:
    pickle.dump(sinh_ngau_nhien_list(), f)
print('Ket thuc qua trinh luu du lieu')
#sắp xếp giảm dần
random.seed(1)
def sap_xep_giam_dan():
    x=sorted(sinh_ngau_nhien_list(), reverse= True)
    x[::-1]
    return x
print(sap_xep_giam_dan())


# gán giá trị
random.seed(1)
d = sap_xep_giam_dan()
print('d=', d)
#Lưu list ở câu (c) vào tập tin văn bản;
path = 'C:\\than\\dulieu01'
filename = 'luutru1.txt'
with open(os.path.join(path, filename), 'wb') as f:
    pickle.dump(d, f)
print('Ket thuc qua trinh luu du lieu')

#Tìm kiếm số n trong list ở câu (d);
m = float(input('m= '))
def tim_kiem(d, m):
  vitri = []
  for i in range(len(d)):
    if d[i] == m:
      vitri.append(i)
  return vitri
position = tim_kiem(d, m)
if len(position) == 0:
  print('không tìm thấy giá trị m trong list')
else:
  print('Cac vi tri xuat hien la: ', position)