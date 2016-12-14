import re
from zipfile import *


myzip = ZipFile('channel.zip', 'r')
myzip.extractall()
    
number = "90052"
 

file = open( number + ".txt")

string = "1 "
list1 = []
while True :
    fileline = file.readlines()
    
    temp = re.search( r'nothing is (.*)' , fileline[0])
    if temp :
        string = temp.group()
        string = [x for x in string if x.isdigit()]
        string = ''.join(string)
    
        number = string
        file.close()
        file = open( number + ".txt")
        list1.append( myzip.getinfo(number + ".txt").comment )
        
    else :
        file.close()
        break
        


print ''.join(list1)


    
