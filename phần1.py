#câu1 Viết hàm sinh ngẫu nhiên các giá trị cho 1 list các số thực trong khoảng [a, b];
n=int(input('n = '))
a = float(input('nhập a='))
b = float(input('nhập b='))
import random
random.seed(100)

def sinh_ngau_nhien():
    c = [(b-a)*random.random()+a for i in range(n)]
    return c
print(sinh_ngau_nhien())
#câu2 Viết hàm sắp xếp list các số thực ở trên theo chiều tăng dần (nếu tham số reverse= True),giảm dần (nếu tham số reverse= False);
#sắp xếp theo thứ tự giảm dần
def giam_dan():
    y = sorted(sinh_ngau_nhien(), reverse=False)
    y[::-1]
    return y
print(giam_dan())
#sắp xếp theo thứ tự tăng dần
def tang_dan():
    x = sorted(sinh_ngau_nhien(), reverse=True)
    x[::-1]
    return x
print(tang_dan())
#. gán giá trị
random.seed(100)
c=sinh_ngau_nhien()
print('c=',c)
#câu3 Viết hàm tìm kiếm số n trong list:
#a. Nếu không tìm thấy thì thông báo ra màn hình là không tìm thấy số n trong list;
#b. Nếu tìm thấy thì hiển thị ra màn hình tất cả các vị trí trong list có giá trị bằng với n.
m = float(input('m= '))
def tim_kiem(m, c):
  vitri = []
  for i in range(len(c)):
    if c[i] == m:
      vitri.append(i)
  return vitri

vitri = tim_kiem(m, c)
if len(vitri) == 0:
    print('không tìm thấy số m trong list')
else:
    print('vị trí trong list có giá trị bằng với m:', vitri)
# câu 4.1Viết hàm lưu list vào tập tin có tùy chọn tham số để xác định là lưu tập tin văn bản

import pickle
import os

def ghi_hamvanban(thumuc: str, ten_taptin: str, objs: list[sinh_ngau_nhien()]):
    try:
        with open(os.path.join(thumuc, ten_taptin), 'wb') as f:
            pickle.dump(objs, f)
        print('Hoan thanh qua trinh ghi du lieu vao tap tin')
    except Exception as e:
        print(e)
        print('Xay ra loi trong qua trinh ghi file')
def main():
    path = 'C:\\than\\dulieu01'
    filename = 'hamvanban.txt'
    sv = sinh_ngau_nhien()
    ghi_hamvanban(path, filename, sv)
    print('ket thuc chuong trinh')
if __name__ == '__main__':
    main()
# câu 4.2 Viết hàm lưu list vào tập tin có tùy chọn tham số để xác định là lưu tập tin nhị phân\
import os
import pickle

def ghi_hamnhiphan(thumuc: str, ten_taptin: str, objs: list[sinh_ngau_nhien()]):
    try:
        with open(os.path.join(thumuc, ten_taptin), 'wb') as f:
            pickle.dump(objs, f)
        print('Hoan thanh qua trinh ghi du lieu vao tap tin')
    except Exception as e:
        print(e)
        print('Xay ra loi trong qua trinh ghi file')

def main():
    path = 'C:\\than\\dulieu01'
    filename = 'hamnhiphan.bin'
    sv = sinh_ngau_nhien()
    ghi_hamnhiphan(path, filename, sv)
    print('ket thuc chuong trinh')

if __name__ == '__main__':
    main()

