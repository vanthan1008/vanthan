from sympy import symbols, Eq, solve
#1. Viết hàm giải hệ phương trình: {2x − 5y + z = −5,4x + 2y − 2z = 2,x + y − z = 0}
def bt_3_an():
  x, y, z = symbols('x y z')
  bt1 = Eq(2*x - 5*y + z,-5)
  bt2 = Eq(4*x + 2*y -2*z,2)
  bt3 = Eq(x + y - z,0)
  answer = solve((bt1 , bt2, bt3), (x,y,z))
  return answer
print('kết quả là ', bt_3_an())

#viết hàm tính giới hạn
from sympy import *
def tinh_gioi_han():
  x = symbols('x')
  f = ((x**3-3*x**2)**1/3)+(x**2-2*x)**1/2
  gioihan = limit(f, x, +oo)
  return gioihan
print('giới hạn biểu thức là ', tinh_gioi_han())

#hàm tính đạo hàm
def tinh_dao_ham():
  x = symbols('x')
  f = (2*x-1)/(x+2)
  daoham = diff(f, x)
  return daoham
print('giá trị đạo hàm là ', tinh_dao_ham())
#hàm tính nguyên hàm
def tinh_nguyen_ham():
  x = symbols('x')
  f = x/(x**2+1)
  nguyenham = integrate(f, x)
  return nguyenham
print('giá trị nguyên ham là ', tinh_nguyen_ham())
#hàm tính tích phân:
def tinh_tich_phan():
  x = symbols('x')
  f = (1- x *tan(x))/(x**2*cos(x)+x)
  tichphan = integrate(f, (x,pi, 2*pi/3))
  return tichphan
print("giá trị tích phân là ",tinh_tich_phan())
# chương trình chính gọi thực hiện các hàm ở trên
#1
def bt_3_an():
  x, y, z = symbols('x y z')
  bt1 = Eq(2*x - 5*y + z,-5)
  bt2 = Eq(4*x + 2*y -2*z,2)
  bt3 = Eq(x + y - z,0)
  answer = solve((bt1 , bt2, bt3), (x,y,z))
  return answer
#2
def tinh_gioi_han():
  x = symbols('x')
  f = ((x**3-3*x**2)**1/3)+(x**2-2*x)**1/2
  gioihan = limit(f, x, +oo)
  return gioihan
#3
def tinh_dao_ham():
  x = symbols('x')
  f = (2*x-1)/(x+2)
  daoham = diff(f, x)
  return daoham
#4
def tinh_nguyen_ham():
  x = symbols('x')
  f = x/(x**2+1)
  nguyenham = integrate(f, x)
  return nguyenham
#5
def tinh_tich_phan():
  x = symbols('x')
  f = (1- x *tan(x))/(x**2*cos(x)+x)
  tichphan = integrate(f, (x,pi, 2*pi/3))
  return tichphan
def main():
    l=tinh_nguyen_ham()
    print(l)
    q=tinh_dao_ham()
    print(q)
    e=tinh_tich_phan()
    print(e)
    t=tinh_gioi_han()
    print(t)
    g=bt_3_an()
    print(g)
if __name__== '__main__':
    main()