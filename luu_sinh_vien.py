from student import SinhVien
import pickle
import os

#Tao 1 doi tuong thuoc lop sinhvien
sv = SinhVien('Le Ngoc Thuan', 2004, 10.0)

#Duong dan ten tap tin
path = 'C:\\than\\data'
filename = 'sinhvien.dat'

#Luu tru
with open(os.path.join(path, filename), 'wb') as f:
    pickle.dump(sv, f)
print('Ket thuc qua trinh luu du lieu')