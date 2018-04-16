import os 
from PIL import Image

img = []
filepath = './original'
for i in range(100):
    full_name = os.path.join(filepath, str(i)+'.JPG')
    if os.path.isfile(full_name):
        im = Image.open(full_name)
        im.thumbnail(size=(60,60), resample= Image.ANTIALIAS)
        img.append(im)
    #     plt.imshow(im)
        im.save('./' + str(i) + '.png')
    else: 
        continue