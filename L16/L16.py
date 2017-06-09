from PIL import Image
import numpy as np

im = Image.open('mozart.gif')
print im.mode

npix = np.array(im)
arr = []

count = 0
for row in npix :
    element = row.tolist().index(195)
    npix[count] = np.roll(row, -element)
    count += 1

im1 = Image.fromarray(npix , im.mode)
im1.show()
