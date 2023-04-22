

import imageio
filenames = ["Image-Slideshow/mountains.jpg","Image-Slideshow/lakes.png"]
images = []
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('Image-Slideshow/movie.gif', images,'GIF',duration=1)