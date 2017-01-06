from PIL import Image

im = Image.new("RGB", (100 , 100))
pix = im.load()


im1 = Image.open("wire.png")
pix1 = im1.load()


counter = -1


for i in range(100):
    for j in range(100):
        counter += 1
        pix[j,i] = pix1[counter , 0]



im.save("output1.png" , 'PNG')
