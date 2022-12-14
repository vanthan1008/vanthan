from student import SinhVien
import pickle
import os


#Duong dan ten tap tin
path = 'C:\\than\\data'
filename = 'sinhvien.dat'

#Luu tru
with open(os.path.join(path, filename), 'rb') as f:
    sv = pickle.load(f)
print(type(sv))
print(sv)
print('Ket thuc qua trinh luu du lieu')