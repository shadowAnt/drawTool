import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm


def gd():
    '''
    一维y=x**2 初始x=10的梯度下降求最小值
    :return:
    '''
    x = 10
    result = [x]
    eta = 1.1
    for i in range(10):
        x -= eta * x * 2
        result.append(x)
    print(result)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    n = max(abs(min(result)), abs(max(result)), 10)
    print(n)
    x_line = np.arange(-n, n, 0.1)
    ax.plot(x_line, [x * x for x in x_line])
    ax.plot(result, [x * x for x in result], '-o')
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    plt.show()


def gd2():
    '''
    二维y=x**2+y**2 初始x=10的梯度下降求最小值
    :return:
    '''
    point = np.array([-5., -2.])
    result = []
    eta = 0.1
    for i in range(20):
        point = point - point * np.array([eta * 2, eta * 4])
        # point -= point * np.array([eta * 2, eta * 2])
        result.append(point)
    print(result)
    x_ = [result[i][0] for i in range(len(result))]
    y_ = [result[i][1] for i in range(len(result))]
    z_ = [result[i][0] ** 2 + result[i][1] ** 2 for i in range(len(result))]
    print(z_)
    Maxrange = np.max(np.abs(result)) + 1
    print(Maxrange)
    x, y = np.mgrid[-Maxrange: Maxrange: Maxrange * 21j, -Maxrange: Maxrange: Maxrange * 21j]
    z = x ** 2 + 2 * y ** 2
    fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    ax = fig.gca(projection="3d")
    ax.plot(x_, y_, z_, '-o', linewidth=1, color='black', label=' 1')
    ax.plot_wireframe(x, y, z, **{'rstride': 2, 'cstride': 2})
    # ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.GnBu, linewidth=0.5, antialiased=False)
    ax.plot([0], [0], [0], 'rx')

    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    plt.legend()
    plt.show()

    # TODO 制作动图  magick *.jpg images.gif
    # for angle in range(95, 180, 3):
    #     ax.set_zlabel("Angle: " + str(angle))
    #     ax.view_init(30, angle)
    #     filename = "./" + str(angle) + ".png"
    #     plt.savefig(filename)
    #     print("Save " + filename + " finish")

    return result


if __name__ == "__main__":
    result = gd2()
