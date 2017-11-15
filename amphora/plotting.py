"""
Plotting routines
"""
from __future__ import absolute_import
from .utility import *
from . import colorconversion


def plot_points(points):
    """
    Plots points in (x,y) space
    """
    fig, ax = plt.subplots()
    ax.plot(points[:, 0], points[:, 1], 'ko')
    ax.axis('equal')
    ax.set_xlim([-1.1, 1.1])
    ax.set_ylim([-1.1, 1.1])
    plt.show()


def plot_lab_points(lab):
    """
    Plots sequence of Lab colors in (a,b) plane
    """
    rgb = colorconversion.lab_to_rgb(lab)
    fig, ax = plt.subplots()
    ax.scatter(lab[:, 1], lab[:, 2], s=60, c=rgb, edgecolors='none')
    ax.axis('equal')
    ax.set_xlim([-105., 105.])
    ax.set_ylim([-105., 105.])
    ax.set_xlabel('a')
    ax.set_ylabel('b')
    plt.show()


def plot_colorsequence_lines(rgb_colors):
    """
    Plots a series of lines with given colors
    """
    fig, ax = plt.subplots()
    ncolors = rgb_colors.shape[0]
    for i, c in enumerate(rgb_colors):
        y = float(i)/ncolors + 0.5/ncolors
        ax.plot([0, 1], [y, y], color=c, lw=4)
    plt.show()


def plot_cmap(cmap, ax=None, aspect=10.):
    if ax is None:
        fig, ax = plt.subplots()

    gradient = numpy.linspace(0, 1, 256)
    gradient = numpy.vstack((gradient, gradient))

    ax.imshow(gradient, aspect=aspect, cmap=cmap)
    pos = list(ax.get_position().bounds)
    x_text = pos[0] - 0.01
    y_text = pos[1] + pos[3]/2.
    fig.text(x_text, y_text, cmap.name, va='center', ha='right', fontsize=10)
    ax.set_axis_off()


def plot_cmap_list(cmap_list):
    nrows = len(cmap_list)
    fig, axes = plt.subplots(nrows=nrows)
    fig.subplots_adjust(top=0.95, bottom=0.01, left=0.2, right=0.99)

    for ax, cmap in zip(axes, cmap_list):
        if isinstance(cmap, str):
            c = plt.get_cmap(c)
        else:
            c = cmap
        plot_cmap(cmap, ax)
