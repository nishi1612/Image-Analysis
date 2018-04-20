from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

k = 1984
b = '2016_crop.jpg'
count = np.array([])
years = np.array([])

while(k<2016):
    a = str(k)
    a = a + '_crop.jpg'
    im1 = Image.open(a, 'r')
    flag = 0
    blue = 0
    for i in range(im1.size[0]):
        for j in range(im1.size[1]):
            l = im1.getpixel((i,j))
            if(l[2]>178):
                blue=blue+1
    ans = np.array([blue])
    count = np.concatenate((count, ans))
    year = np.array([k])
    years = np.concatenate((years, year))
    k = k + 1

plt.plot(years,count)
plt.show()
