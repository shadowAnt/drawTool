import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


def draw1():
    '''
    折线图，y和x的一次关系
    :return:
    '''
    fig = plt.figure()
    ax = fig.add_subplot(111)
    x = np.arange(0.8, 8, 0.01)
    y1 = 4 * np.exp(x / 2) / (3 * (np.exp(x / 2) - 1) ** 2)
    ax.plot(x, y1, c='black', label='0')
    # ax.legend()
    ax_title_text = ax.set_title('relationship between wPP and w')
    ax_xlabel_text = ax.set_xlabel('number')
    ax_ylabel_text = ax.set_ylabel('Error')
    plt.ylim(0, 6)
    plt.legend()
    plt.show()

def draw2():
    '''
    z=x**2+y**2
    :return:
    '''
    # 在-1到1中间取31个值
    x, y = np.mgrid[-1: 1: 31j, -1: 1: 31j]
    z = x ** 2 - y ** 2
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_wireframe(x, y, z, **{'rstride': 2, 'cstride': 2})
    ax.plot([0], [0], [0], 'rx')
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    plt.show()


if __name__ == '__main__':
    draw2()
