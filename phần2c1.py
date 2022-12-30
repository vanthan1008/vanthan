# viết hàm tính tích của 2 ma trận x ; A
import numpy as np
n = abs(int(input('n= ')))
x= np.linspace(start=-2,stop=5,num=n,dtype=int)
print('ma trận x là ', x)
m = int(input('m= '))
A=np.random.random((m,n))
print('ma trận A là ', A)
#viết hàm tính tích x.
def tinh_tich():
    v = x*A
    return v
print(tinh_tich())
#Cho C, B ∈ Rm×n
C = np.random.random((m,n))
print('ma trận C là', C)
B = np.random.random((m,n))
print('ma trận b là', B)
#hàm tính A°B
def tinh_toan():
    d = np.multiply(C, B)
    return d
print('giá trị hàm tính A°B là ', tinh_toan())
#hàm tính Ct.B
def ham_tinh_vecto():
    f = np.transpose(C)*B
    return f
print('giá trị Ct.B', ham_tinh_vecto())
#Viết chương trình chính gội các hàm trên.
#1
def tinh_tich():
    v = x*A

    return v
#2
def tinh_toan():
    d = np.multiply(C, B)
    return d
#3
def ham_tinh_vecto():
    f = np.transpose(C)*B
    return f
def main():
    t=tinh_toan()
    print("tính toán",t)
    v=tinh_tich()
    print('tính tích',v)
    f=ham_tinh_vecto()
    print('tính vecto',f)

if __name__== '__main__':
    main()