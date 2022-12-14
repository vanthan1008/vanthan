from student import SinhVien
import os
import pickle

def ghi_sinhvien(thumuc: str, ten_tap_tin: str, obj: SinhVien):
    try:
        with open(os.path.join(thumuc, ten_tap_tin), 'wb') as f:
            pickle.dump(obj, f)
        print('hoan thanh qua trinh ghi file')
    except Exception as e:
        print(e)
        print('xay ra loi trong qua trinh ghi file')

def doc_sinhvien(thumuc: str, ten_tap_tin: str) -> SinhVien:
    try:
        with open(os.path.join(thumuc, ten_tap_tin), 'rb') as f:
            sv = pickle.load(f)
        return sv
    except Exception as e:
        return None

def main():
    path = 'C:\\than\\data'
    filename = 'sinhvien2.txt'
    sv1 = SinhVien('văn thân', 2004, 10)
    ghi_sinhvien(path, filename, sv1)
    noidung = doc_sinhvien(path, filename)
    print(noidung)
    print('ket thuc chuong trinh')

if __name__=='__main__':
    main()

