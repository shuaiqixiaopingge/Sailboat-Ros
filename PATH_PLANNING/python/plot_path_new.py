import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.interpolate import splprep, splev
import os


def get_spline(path_x, path_y, heading):
    headingVecLength = 0.5
    headingVec = [headingVecLength * math.cos(math.pi - heading), headingVecLength * math.sin(math.pi - heading)]
    pts = []
    for i, (x, y) in enumerate(zip(path_x, path_y)):
        if i == 1:
            pts.append((path_x[0] + headingVec[0], path_y[0] + headingVec[1]))
        pts.append([x, y])
    pts = np.array(pts)
    tck, u = splprep(pts.T, u=None, s=0.2, per=0)
    u_new = np.linspace(u.min(), u.max(), 1000)
    x_new, y_new = splev(u_new, tck, der=0)
    return x_new, y_new


if __name__ == '__main__':

    obs_x, obs_y = [], []
    with open('map_new.txt', 'r') as f:
        for row, line in enumerate(f.readlines()):
            line = line.rstrip('\n').rstrip(' ').split(' ')
            for col, num in enumerate(line):
                if int(num) == 1:
                    obs_x.append(row)
                    obs_y.append(col)
    n_row, n_col = row + 1, col + 1
    print(n_row, n_col)
    print(obs_x)
    print(obs_y)

    with open('path_new.txt', 'r') as f:
        path_x, path_y = [], []
        path_x_f, path_y_f = [], []
        for line in f.readlines():
            if line.startswith('heading'):
                heading_tmp = line.rstrip('\n').split(',')
                heading = float(heading_tmp[1])
                continue
            elif line.startswith('wind'):
                wind_tmp = line.rstrip('\n').split(',')
                wind = float(wind_tmp[1])
                continue
            elif line == '####\n':
                path_x_f, path_y_f = get_spline(path_x, path_y, heading)
                break
            line = line.rstrip('\n').split(',')
            path_x.append(int(line[0]))
            path_y.append(int(line[1]))

    print('wind: {}'.format(wind))
    print('heading: {}'.format(heading))

    windVecLength = 1
    windVec = [windVecLength * math.cos(wind), windVecLength * math.sin(wind)]

    headingVecLength = 1
    headingVec = [headingVecLength * math.cos(heading), headingVecLength * math.sin(heading)]

    plt.figure(dpi=200)
    # plt.figure(figsize=(6, 4), dpi=98)
    p1 = plt.subplot(111)
    p1.plot(np.array(path_y), np.array(path_x), label='path')
    p1.plot(np.array(path_y_f), np.array(path_x_f), label='path_f')
    p1.plot(np.array(obs_y), np.array(obs_x), 'ro', label='obstacle')
    p1.scatter([path_y[0], path_y[-1]], [path_x[0], path_x[-1]], s=50, c='green')

    x, y = np.array([2, 2 + windVec[1]]), np.array([2, 2 + windVec[0]])
    p1.quiver(x[:-1], y[:-1], x[1:] - x[:-1], y[1:] - y[:-1])
    p1.text(0, 0, s='wind', fontsize=10, color='magenta')

    x, y = np.array([path_y[0], path_y[0] + headingVec[1]]), np.array([path_x[0], path_x[0] + headingVec[0]])
    p1.quiver(x[:-1], y[:-1], x[1:] - x[:-1], y[1:] - y[:-1], color='green')

    p1.text(path_y[0], path_x[0], s='Start', fontsize=12, color='green')
    p1.text(path_y[-1], path_x[-1], s='End', fontsize=12, color='green')

    # p1.set_title('upwind')
    p1.legend()
    p1.axis([0, n_col - 1, n_row - 1, 0])
    p1.set_xticks(np.arange(-1, n_col + 1, 1))
    p1.set_yticks(np.arange(-1, n_row + 1, 1))
    p1.xaxis.tick_top()
    p1.grid(True)

    file_folder = 'test_imgs/'
    if not os.path.exists(file_folder):
        os.system('mkdir -p ' + file_folder)
    file_path = os.path.join(file_folder, '{}.png'.format("test"))
    print("saving file {} ...".format(file_path))
    plt.savefig(file_path)
    plt.show()

    plt.close('all')
