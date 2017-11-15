"""
Methods for converting colors between color spaces
"""
from __future__ import absolute_import
from .utility import *
import skimage.color

def expand_ab_sequence_to_lab(ab, luminosity):
    """
    Expand (a,b) points to (L,a,b) colors by assigning a constant luminosity
    value.
    """
    n, m = ab.shape
    p = numpy.tile(luminosity, (n, 1))
    lab = numpy.hstack((p, ab))
    return lab


def lab_to_rgb(lab):
    """
    Converts Lab color sequence [n, 3] to rgb space.
    """
    p = lab[numpy.newaxis, :, :]
    rgb = skimage.color.lab2rgb(p)[0, :, :]
    rgb[rgb < 0.0] = 0.0
    rgb[rgb > 1.0] = 1.0
    return rgb


def rgb_to_lab(rgb):
    """
    Converts rgb color sequence [n, 3] to Lab space.
    """
    p = rgb[numpy.newaxis, :, :]
    lab = skimage.color.rgb2lab(p)[0, :, :]
    return lab


def rgb_to_hex(rgb):
    """
    Converts rgb color sequence [n, 3] to a list of hex color strings
    (a.k.a. HTML color codes)
    """
    hex_list = [matplotlib.colors.rgb2hex(c) for c in rgb]
    return hex_list


def hex_to_rgb(hex_list):
    """
    Converts a list of hex color strings to a [n, 3] rgb array.
    """
    rgb_list = [matplotlib.colors.hex2color(c) for c in hex_list]
    return numpy.array(rgb_list)


def rgb_to_hsv(rgb):
    """
    Converts rgb color sequence [n, 3] to hsv color space
    """
    return matplotlib.colors.rgb_to_hsv(rgb)


def hsv_to_rgb(hsv):
    """
    Converts hsv color sequence [n, 3] to rgb color space
    """
    return matplotlib.colors.hsv_to_rgb(hsv)
