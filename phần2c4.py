
import numpy as np

import matplotlib.pyplot as plt
from matplotlib import cm
#vẽ mặt yên ngựa
def do_thi_yen_ngua(x, y):
    x, y = np.meshgrid(x, y)
    z = (x/3)**2 - (y/2)**2
    fig, ax = plt.subplots(subplot_kw={"projection":"3d"})
    rosen_surf = ax.plot_surface(x, y, z,cmap=cm.gist_heat_r,linewidth=0, antialiased=False)

    fig.colorbar(rosen_surf, shrink=0.5, aspect=5)
    plt.show()

#vẽ đường hyperbol
def hyperbol(x, y):
    x, y = np.meshgrid(x, y)
    z1 =2*((x/3)**2 + (y/5)**2 - 1)**(1/2)
    z2 =-2*((x/3)**2 + (y/5)**2 - 1)**(1/2)
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    rosen_surf1 = ax.plot_surface(x, y, z1, cmap=cm.gist_heat_r, linewidth=0, antialiased=False)
    rosen_surf2 = ax.plot_surface(x, y, z2, cmap=cm.gist_heat_r, linewidth=0, antialiased=False)
    fig.colorbar(rosen_surf1, shrink=0.5, aspect=5)
    fig.colorbar(rosen_surf2, shrink=0.5, aspect=5)
    plt.show()


#vẽ hình cầu
def mat_cau(x, y):
    x, y = np.meshgrid(x, y)
    z1 = 4 + (-(x+2)**2 - (y-1)**2 + 4)**(1/2)
    z2 = 4 - (-(x+2)**2 - (y-1)**2 + 4)**(1/2)
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    rosen_surf1 = ax.plot_surface(x, y, z1, cmap=cm.gist_heat_r, linewidth=0, antialiased=False)
    rosen_surf2 = ax.plot_surface(x, y, z2, cmap=cm.gist_heat_r, linewidth=0, antialiased=False)
    fig.colorbar(rosen_surf1, shrink=0.5, aspect=5)
    fig.colorbar(rosen_surf2, shrink=0.5, aspect=5)
    plt.show()
def main():
    #1
    x = np.linspace(-20, 30, num=200)
    y = np.linspace(-15, 25, num=200)
    l = do_thi_yen_ngua(x, y)
    print(l)
    #2
    x = np.linspace(-9, 9, num=2000)
    y = np.linspace(-9, 9, num=2000)
    k = hyperbol(x, y)
    print(k)
    #3
    x = np.linspace(-4, 0, num=2000)
    y = np.linspace(-1, 3, num=2000)
    m = mat_cau(x, y)
    print(m)


if __name__ == '__main__':
    main()