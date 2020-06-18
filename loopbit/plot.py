
from itertools import product
from scipy.ndimage import gaussian_filter
import matplotlib.pyplot as plt
import numpy as np

def contour_90deg_thresh(matrix, axe=None, gaussian=4., superimpose=False,
                         pin_point_loops=True, **kwargs):
    """
    Draw triangular matrix
    """
    if axe is None:
        axe = kwargs.get('axe', plt.subplot(111))
    size = matrix.shape[0]
    if 'vmin' not in kwargs and 'vmax' not in kwargs:
        try:
            kwargs['vmin'] = np.min(matrix[np.isfinite(matrix)])
            kwargs['vmax'] = np.max(matrix[np.isfinite(matrix)])
        except ValueError:  # probably empty
            pass
    # create rotation/scaling matrix
    rot = np.array([[1, 0.5], [-1, 0.5]])
    # create coordinate matrix and transform it
    A = np.dot(np.array([(j + 0.5, i + 0.5) for i, j in product(range(size - 1,  -1, -1),
                                                    range(0, size, 1))]), rot)
    # plot
    contour = plt.contour if superimpose else plt.contourf
    im = contour(A[:,1].reshape(size, size),
                 A[:,0].reshape(size, size),
                 np.flipud(gaussian_filter(matrix, gaussian)),
                 levels=5, cmap='Reds')

    if pin_point_loops:
        cmap = plt.cm.get_cmap('Reds')
        for j in range(size):
            for i in range(j, size):
                I = i + 0.5
                J = j + 0.5
                if matrix[i, j]:
                    col = cmap(matrix[i, j] / 10)
                    plt.plot([(I + J) / 2 - 0.25, (I + J) / 2 + 0.25], [I - J - 0.5, I - J + 0.5], c=col, lw=0.5)
                    plt.plot([(I + J) / 2 + 0.25, (I + J) / 2 - 0.25], [I - J - 0.5, I - J + 0.5], c=col, lw=0.5)
                    # plt.text((I + J) / 2, I - J, round(matrix[i, j], 3), size=4)

    if not superimpose:
        im.cmap.set_under('white')
    im.set_clim(0.02, 0.1)
    axe.spines['right'].set_visible(False)
    axe.spines['left'].set_visible(False)
    axe.spines['top'].set_visible(False)
    axe.spines['bottom'].set_visible(False)
    axe.set_xticks([])
    axe.set_yticks([])
    return im


def pcolormesh_45deg(matrix, axe=None, **kwargs):
    """
    Draw triangular matrix
    """
    if axe is None:
        axe = kwargs.get('axe', plt.subplot(111))
    size = matrix.shape[0]
    if 'vmin' not in kwargs and 'vmax' not in kwargs:
        try:
            kwargs['vmin'] = np.min(matrix[np.isfinite(matrix)])
            kwargs['vmax'] = np.max(matrix[np.isfinite(matrix)])
        except ValueError:  # probably empty
            pass
    # create rotation/scaling matrix
    rot = np.array([[1, 0.5],[-1, 0.5]])
    # create coordinate matrix and transform it
    A = np.dot(np.array([(j, i) for i, j in product(
        range(size, -1, -1), range(0, size + 1, 1))]), rot)
    # plot
    im = axe.pcolormesh(A[:,1].reshape(size + 1,size + 1),
                        A[:,0].reshape(size + 1,size + 1),
                        np.flipud(matrix),**kwargs)
    axe.spines['right'].set_visible(False)
    axe.spines['left'].set_visible(False)
    axe.spines['top'].set_visible(False)
    axe.spines['bottom'].set_visible(False)
    axe.set_xticks([])
    axe.set_yticks([])
    return im
