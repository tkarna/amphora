"""
Methods for generating color sequences.
"""
from __future__ import absolute_import
from .utility import *
from . import pointgeneration
from . import colorconversion

def generate_ab_color_sequence(n, const_luminosity=70.0):
    """Generates a color sequence by sampling (a,b) space"""
    points = pointgeneration.generate_points(n, 2)

    # cast to (a,b) space by scaling
    max_chroma = 82.0
    ab_offset = 12.0
    ab_points = max_chroma*points
    ab_points[:, 0] += ab_offset
    ab_points[:, 1] += ab_offset
    lab = colorconversion.expand_ab_sequence_to_lab(ab_points, const_luminosity)
    return lab


def generate_lab_color_sequence(n, lmin=20.0, lmax=85.0):
    """Generates a color sequence by sampling (L,a,b) space"""
    points = pointgeneration.generate_points(n, 3)

    max_chroma = 82.0
    ab_offset = 12.0
    # cast to (a,b) space by scaling
    l = points[:, 0]
    points[:, 0] = (lmax - lmin)*0.5*(l + 1.0) + lmin
    points[:, 1] *= max_chroma
    points[:, 2] *= max_chroma
    points[:, 1] += ab_offset
    points[:, 2] += ab_offset
    lab = points
    return lab


def equidistant_color_sequence(n, lum=None, lum_min=20.0, lum_max=85.0, sort='chroma'):
    """
    Generates a sequence of n colors that are perceptually as different as
    possible.

    s = equidistant_color_sequence(n, lum=75.0)

    Generates sequence with constant luminosity.

    s = equidistant_color_sequence(n, lum_min=20.0, lum_max=85.0)

    Generates sequence where luminosity is limited to range [lum_min, lum_max].

    If sort='chroma' the color sequence is re-ordered by lab color saturation.

    If sort='suffle' the color sequence is re-ordered to maximize difference
    between consecutive colors.

    Output s is a n-by-3 array of colors in Lab space.

    """
    if lum is not None:
        lab = generate_ab_color_sequence(n, lum)
    else:
        lab = generate_lab_color_sequence(n, lum_min, lum_max)
    # cast to rgb to remove undefined colors
    rgb = colorconversion.lab_to_rgb(lab)
    lab = colorconversion.rgb_to_lab(rgb)
    if sort == 'chroma':
        lab = sort_by_chroma(lab)
    elif sort == 'suffle':
        lab = suffle_sequence(lab)
    return lab


def suffle_sequence(rgb):
    """
    Re-orders color sequence by trying to maximize the distance between
    consecutive colors

    Note that the color disnance is computed in the same space as the color
    sequence is in. Arguably this should be performed in Lab space.
    """
    def seqdistance(rgb):
        """Computes the sum of consecutive color differences"""
        return numpy.sum(numpy.diff(rgb, axis=0))
    nperm = 1000
    dist = seqdistance(rgb)
    out = rgb
    for i in range(nperm):
        new_rgb = numpy.random.permutation(rgb)
        new_dist = seqdistance(new_rgb)
        if new_dist > dist:
            dist = new_dist
            out = new_rgb
    return new_rgb


def sort_by_chroma(lab):
    """
    Sorts lab color sequence by color saturation (chroma)
    """
    chroma = numpy.sqrt(lab[:, 1]**2 + lab[:, 2]**2)
    # multiply chroma by L to emphasize light intense colors
    c = chroma * lab[:, 0]
    index = numpy.argsort(-c)
    new = lab[index, :]
    return new

