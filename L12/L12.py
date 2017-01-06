gfx = open("evil2.gfx" , "rb")

data = gfx.read()
gfx.close()

li = [
        open("1.jpg" ,"wb"),
        open("2.jpg" ,"wb"),
        open("3.jpg" ,"wb"),
        open("4.jpg" ,"wb"),
        open("5.jpg" ,"wb"),
    ]

for j in range(5):
    li[j].write(data[j::5])
    li[j].close



