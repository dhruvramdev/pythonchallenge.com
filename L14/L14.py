from PIL import Image

im = Image.new("RGB", (100 , 100))
pix = im.load()


im1 = Image.open("wire.png")
pix1 = im1.load()

counter = 0
number = 0

# Generating Sequnce to Sum Up 10000

li = []
b = 100
for a in range(199):
    li.append(b)
    if a %2 == 0:
        b -= 1

print li

sign = [1,1,-1,-1]

constant = ['row' , 0 ]

variable = ['+' , 0]


for x in li :
    print "Current Element is " , x 
    temp = sign[number%4]
    l = []
    if constant[0] == 'row' :
        if temp == 1 :
            l = range(variable[1] , variable[1]+x)
        else :
            l = range(variable[1] - 2  , variable[1] - x - 2 , -1)

        #print "ROW Constant \n \n List ::::         \n"
        #print l , '\n Tuples'
        for i in l :
            pix[i , constant[1]] = pix1[counter , 0]
            counter += 1

        constant[0] = 'column'
        variable[1] , constant[1] = constant[1] + 1 , l[-1]

    else :
        if temp == 1 :
            l = range(variable[1] , variable[1]+x)
        else :
            l = range(variable[1] -2  , variable[1] - x - 2, -1)

        #print "Column Constant \n \n List ::::         \n"
        #print l , '\n Tuples'
        for i in l :
            pix[constant[1] , i] = pix1[counter , 0]
            counter += 1
 
        constant[0] = 'row'
        variable[1] , constant[1] = constant[1] + 1 , l[-1]


    number += 1    
##    print  '\n\n'


im.save("output2.png" , 'PNG')


                
            

    
    




