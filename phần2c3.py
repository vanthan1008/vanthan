import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
x = np.linspace(start=-10.0,stop=10.0, num=200)
y1 = x**4-2*x**2-3
y2 = 4*x**3-4*x
y3 = 12*x**2-4
y4 = 24*x
ax.plot(x, y1)
ax.plot(x, y2)
ax.plot(x, y3)
ax.plot(x, y4)
ax.plot(x, y1, label=r'$y=x^4-2x^2-3$')
ax.plot(x, y2, label=r'$đạo hàm bậc 1 y=4x^3-4x$')
ax.plot(x, y3, label=r'$đạo hàm bậc 2 y=12x^2-4$')
ax.plot(x, y4, label=r'$đạo hàm bậc 3 y=24x$')
ax.set_xlabel("Trục hoành - x")
ax.set_ylabel("Trục tung - y")
ax.legend()
plt.show()
