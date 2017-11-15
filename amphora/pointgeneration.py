"""
Routines for generating equidistant point clouds
"""
from __future__ import absolute_import
from .utility import *
from scipy.optimize import minimize
from scipy.spatial.distance import pdist


def coords_to_state(coords):
    """
    Converts [n, dim] coordinates to optimization state vector
    """
    p = coords
    return p.ravel()


def state_to_coords(x, dim):
    """
    Converts optimization state vector to [n, dim] coordinates
    """
    c = numpy.reshape(x, (len(x)/dim, -1))
    return c


def equidistance_cost_fun(state, dim):
    """
    Cost function for generating equidistant points.

    In practice the most robust method appears to be optimizing pairwise
    distances towards a pre-defined consntant in least-square sense.
    """
    coords = state_to_coords(state, dim)
    n, m = coords.shape
    distance = pdist(coords)
    mean_dist = numpy.mean(distance)
    # NOTE tuned for 2D ...
    target_dist = 2.2/n**(1.0/dim/3.0)

    cost = numpy.sum((distance - target_dist)**2)
    return cost


def normalize_points(points):
    """
    Normalizes point cloud to (-1, 1) range
    """
    mean = numpy.mean(points, axis=0)
    vmax = numpy.max(points, axis=0)
    vmin = numpy.min(points, axis=0)
    new_points = 2.0*(points - mean)/(vmax - vmin)
    return new_points


def generate_points(n, dim, normalize=False):
    """
    Generates a cloud of n equidistant points in (-1, 1)^dim square or cube.

    The generates cloud point does not necessarily fill the entire (-1, 1)
    range. If normalize=True, the point cloud is normalized to fill the range.

    Returns points as [n, dim] array.
    """
    # init_points = 2*numpy.random.rand(n, dim) - 1.0
    theta = numpy.linspace(0.0, 2*numpy.pi*(1.0 - 1.0/n), n)
    x = numpy.cos(theta)
    y = numpy.sin(theta)
    if dim == 2:
        init_points = numpy.vstack((x, y)).T
    else:
        z = numpy.linspace(-1.0, 1.0, n)
        init_points = numpy.vstack((x, y, z)).T

    init_guess = coords_to_state(init_points)

    # boundaries
    bnds = [(-1, 1)]*(dim*n)

    costfun = lambda x: equidistance_cost_fun(x, dim)
    res = minimize(costfun, init_guess, bounds=bnds)

    points = state_to_coords(res.x, dim)
    if normalize:
        # NOTE points do not necessary fill the entire space, normalize
        points = normalize_points(points)
    return points
