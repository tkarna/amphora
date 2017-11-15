import numpy
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors
from scipy.interpolate import interp1d
from . import colorconversion


def gen_linear_colormap(name, color_list, l_min, l_max, n=256):
    """
    Generates a linear colormap where luminance varies linearly from
    l_min to l_max.
    """

    # convert all colors to lab space
    rgb = color_list
    lab = colorconversion.rgb_to_lab(rgb)
    # generate full color sequence
    nodes = numpy.linspace(0, 1, lab.shape[0])
    nodes_out = numpy.linspace(0, 1, n)
    lab_out = interp1d(nodes, lab.T)(nodes_out).T

    # replace l values with linearly interpolated l
    lumi = numpy.linspace(l_min, l_max, n)
    lab_out[:, 0] = lumi
    # convert to rgb
    rgb_out = colorconversion.lab_to_rgb(lab_out)
    # make colormap
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list(name,
                                                               rgb_out,
                                                               N=n)
    return cmap

