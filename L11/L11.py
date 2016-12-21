from PIL import Image

im = Image.open("cave.jpg")

width , height = im.size

array = im.load()

im1 = Image.new("RGB" , (width/2 , height/2))
im2 = Image.new("RGB" , (width/2 , height/2))



for i in range(height):
    for j in range(width):
        #print array[j,i]
        if (i+j)%2 == 0 :
            im1.putpixel((j/2,i/2), array[j,i]) 

        else :
            im2.putpixel((j/2,i/2), array[j,i]) 

        
im1.show()


im1.save("evil.jpg")
