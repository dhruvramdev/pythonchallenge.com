from PIL import Image
import string , sys

im = Image.open("oxygen.png")

li= im.load()

width , height = im.size[0] , im.size[1]

posn_of_bar = 0

#finding the height of bar
for i in range(height):
    temp = li[1 ,i]
    if temp[0] == temp[1] == temp[2] :
        posn_of_bar = i
        
#finding the width of box-elements in bar
l1 = []
last = 0
color = li[0 , posn_of_bar][0]
for i in range(width):
    temp = li[i, posn_of_bar]
    if temp[0] != color :
        l1.append(i-last)
        last = i
        color = temp[0]

#print l1
# hence width of block is 7 , to see how remove commen of printing l1

sum1 = l1[0]
for i in l1 :
    if i%7 == 0 :
        sum1 += i

#print sum1    
        
         
str1 = ""    

for i in range(l1[0] - 1 , sum1 + 7 , 7):
    temp = li[i ,posn_of_bar]
    #sys.stdout.write(chr(temp[0]))
    str1 += chr(temp[0])

str2 = ""

for  i in str1 :
    if i.isdigit() :
        str2 += i
    
for i in range(0 , len(str2) , 3):
    sys.stdout.write( chr(int(str2[i:i+3])))


        
            
