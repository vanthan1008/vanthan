#Xây dựng lớp NhanVien có các thuộc tính là hoten, tuoi, luong;
class NhanVien:
    def __init__(self, fullname: str, yob: int, wage: float):
        self.hoten = fullname
        self.tuoi = yob
        self.luong = wage

    def __str__(self) -> str:
        NhanVien = '[họ tên: ' + self.hoten + '; tuoi: ' \
                  + str(self.tuoi) + '; lương: ' \
                  + str(self.luong) + ']'
        return NhanVien

#Viết hàm nhập dữ liệu cho 1 list các đối tượng thuộc lớp NhanVien;
import pickle
import os
def list_nhan_vien():
    nv = [NhanVien('NGUYỄN THỊ LƯƠNG THẾ',16,1000),NhanVien('trần hữu huy',17,165739),NhanVien('trần bình',16,167853),NhanVien('lê văn tuấn',15,651651)]
    return nv
def in_list_NhanVien():
    t = list_nhan_vien()
    return t
print(in_list_NhanVien())
# sắp xếp
class NhanVien:
    def __init__(self, fullname: str, yob: int, wage: float):
        self.hoten = fullname
        self.tuoi = yob
        self.luong = wage

    def __str__(self) -> str:
        NhanVien = '[họ tên: ' + self.hoten + '; tuoi: ' \
                  + str(self.tuoi) + '; lương: ' \
                  + str(self.luong) + ']'
        return NhanVien
    def __gt__(self, obj):
        return (self.tuoi > obj.tuoi)
    def __ge__(self, obj):
        return (self.tuoi >= obj.tuoi)
    def __lt__(self, obj):
        return (self.tuoi < obj.tuoi)
    def __le__(self, obj):
        return (self.tuoi <= obj.tuoi)
    def __eq__(self, obj):
        return (self.tuoi == obj.tuoi)
def main():
    nv= sorted(list_nhan_vien(), reverse = True)
    for item in nv:
        print(item)
if __name__== '__main__':
    main()
#ghi nhân viên
def ghi_Nhanvien(thumuc: str, ten_taptin: str, obj:in_list_NhanVien()):
    try:
        with open(os.path.join(thumuc, ten_taptin), 'wb') as f:
            pickle.dump(obj, f)
        print('Hoan thanh qua trinh ghi du lieu vao tap tin')
    except Exception as e:
        print('Xay ra loi trong qua trinh ghi file')
def doc_Nhanvien(thumuc: str, ten_taptin: str) -> NhanVien:
    try:
        with open(os.path.join(thumuc, ten_taptin), 'rb') as f:
            sv = pickle.load(f)
        return sv
    except Exception as e:
        return None

def in_list_Nhanvien1(content: list[NhanVien]):
    for item in content:
        print(item)
def main():
    path = 'C:\\than\\dulieu01'
    filename = 'NhanVien.bin'
    ghi_Nhanvien(path, filename, in_list_NhanVien())
    noidung = doc_Nhanvien(path, filename)
    in_list_Nhanvien1(noidung)
    print('ket thuc chuong trinh')

if __name__== '__main__':
    main()