url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

import requests ,re 
number = "12345"

res = requests.get(url + number)

string = ""

for i in range(250):
    temp = re.search( r'next nothing is (.*)' , res.text)
    
    if string == "16044" :
        string = "8022" # Hard Coded By Observation
    else :
        string = temp.group()
        string = [x for x in string if x.isdigit()]
        string = ''.join(string)
    res = requests.get(url + string)
    print res.text , "    " , i 
    
    
