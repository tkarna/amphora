"""
Examples of color sequence generation
"""
from amphora import *

## a few colors with constant luminosity
#lab = equidistant_color_sequence(9, lum=60.0)
#plot_lab_points(lab)
#rgb = lab_to_rgb(lab)
#plot_colorsequence_lines(rgb)

## a few lab colors -- narrow luminosity range
#lab = equidistant_color_sequence(10, lum_min=40, lum_max=80)
#plot_lab_points(lab)
#rgb = lab_to_rgb(lab)
#plot_colorsequence_lines(rgb)

# a lot of colors -- larger luminosity range
lab = equidistant_color_sequence(22, lum_min=18, lum_max=88)
#plot_lab_points(lab)
rgb = lab_to_rgb(lab)
n = rgb.shape[0]/2*2
rgb2 = numpy.ones((n, 3))
rgb2[::2, :] = rgb[:n/2, :]
rgb2[1::2, :] = rgb[n/2:n, :]
rgb = rgb2
# a = numpy.vstack((rgb[1::2, :], rgb[::2, :]))
plot_colorsequence_lines(rgb)

# print sequence as HTML hex strings
print(rgb_to_hex(rgb))

