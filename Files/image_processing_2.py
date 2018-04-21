from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

k = 1984

# Declaring two arrays which will be storing count of blue pixels representing water in the image and years.
count = np.array([])
years = np.array([])

while(k<2016):
    a = str(k)
    a = a + '_crop.jpg'
    b = 'Images/Cropped Images/' + a

    # Opening the image to be used in python
    im1 = Image.open(b, 'r')
    flag = 0
    blue = 0
    for i in range(im1.size[0]):
        for j in range(im1.size[1]):
            l = im1.getpixel((i,j))

            # If in (R,G,B) value of a pixel, value of B is more than 178 then it is a blue pixel representing water
            # Hence increament the local count for blue pixel of that image
            if(l[2]>178):
                blue=blue+1

    # Concatenate the newly updated values in the actual array
    ans = np.array([blue])
    count = np.concatenate((count, ans))
    year = np.array([k])
    years = np.concatenate((years, year))

    # Increament k to go to next year
    k = k + 1

# Plot the graph using plt
plt.plot(years,count)
plt.ylabel('Number of blue pixels representing water')
plt.xlabel('Years')
plt.grid(True)
plt.title('Count of blue pixels v/s Years')
plt.show()
