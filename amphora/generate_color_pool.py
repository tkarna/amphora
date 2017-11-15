"""
Routines for generating colors that are euqally distant from each other.

This boils down to filling a constrained space with N equidistant points.

Depends: numpy, scipy, skimage

Tuomas Karna 2016-06-08
"""



#p = generate_points(35, 2)
#plot_2d_points(p)

# Examples

# a few colors with constant luminosity
lab = equidistant_color_sequence(9, lum=60.0)
plot_lab_points(lab)
rgb = lab_to_rgb(lab)
plot_color_sequence(rgb)

# a few lab colors -- narrow luminosity range
lab = equidistant_color_sequence(10, lum_min=40, lum_max=80)
plot_lab_points(lab)
rgb = lab_to_rgb(lab)
plot_color_sequence(rgb)

# a lot of colors -- larger luminosity range
lab = equidistant_color_sequence(20, lum_min=20, lum_max=90)
plot_lab_points(lab)
rgb = lab_to_rgb(lab)
plot_color_sequence(rgb)




#rgb = numpy.array([1.0, 1.0, 1.0])
#print color.rgb2lab(rgb[numpy.newaxis, numpy.newaxis, :])[0, 0, :]

#hsv = numpy.array([[v, 0.8, 0.7] for v in numpy.linspace(0.0, 5.0/6.0, 12)])
#print hsv

#rgb = color.hsv2rgb(hsv[numpy.newaxis, :, :])[0, :, :]
#print rgb


#plot_color_sequence(rgb)

#lab = color.rgb2lab(rgb[numpy.newaxis, :, :])[0, :, :]
#print lab
