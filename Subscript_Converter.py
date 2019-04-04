# -*- coding: utf-8 -*-
 
 
my_dict = {
    "1"  : "\u00B9",
    "2"  : "\u00B2",    
    "3"  : "\u00B3",
    "4"  : "\u2074",
    "5"  : "\u2075",
    "6"  : "\u2076",
    "7"  : "\u2077",
    "8"  : "\u2078",
    "9"  : "\u2079",
    "+"  : "\u207A",
    "-"  : "\u207B"
    }
 
 
 
def check(string, char):
    number = False
    n = 0
    x = list(string)
     
    for i in x:
        if number == True:
            if i.isnumeric() == True or i == "-" or i == "+":
                if char == "^":
                    for key, value in my_dict.items():
                         
                        if key == i:
                            x[n] = value
                            print(x)
                elif char == "_":
                    x[n] = "\\u208{0}".format(i).encode('utf-8').decode('unicode-escape')
                    print(x)
            else:
                number = False
         
        if i == char:
            number = True
         
        n += 1
     
    string = "".join(x)
    string = string.replace(char, "")
    return string
 
def convert(string):
     
    string = check(string, "_")
    string = check(string, "^")
    print(string)
     
string = "123456789H_123456789H^123456789+-"
convert(string)

