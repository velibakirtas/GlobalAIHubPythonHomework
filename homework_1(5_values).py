import re
counter  = 0
while counter<5:
    value = input("Please enter a value: ")
    if value.isdigit(): # dizideki tüm karakterler rakamsa true
        valueInt = int(value)
        print(f"\nThe value you entered is {valueInt}, the type of the value is {type(valueInt)}\n")
    elif value.isalpha():# dizideki tüm karakterler harfse true
        print("\nThe value you enterd is {0}, the type of the value is {1}\n".format(value,type(value)))   
    elif value.isalnum(): # dizideki karakterler rakam ve harf karışıksa true        
        print(f"\nThe value you intered is {value}, the type of the value is {type(value)}\n")
    elif re.search("/s",value):    
        print(f"\nThe value you intered is {value}, the type of the value is {type(value)}\n")
    elif re.search(".",value) and re.search("[0-9]",value):
        if re.search("[a-z]",value) or re.search("[A-Z]",value):
            print("\nThe value you entered is {0}, the type of the value is {1}\n".format(value,type(value))) 
        elif re.search("[()}{/\'#$%&=?*_:,;!^+-]",value):
            print("\nThe value you entered is {0}, the type of the value is {1}\n".format(value,type(value)))          
        else:    
            valueFl = float(value)
            print("\nThe value you entered is {0}, the type of the value is {1}\n".format(valueFl,type(valueFl)))
    else:
        print(f"\nThe value you entered is {value}, the type of the value is {type(value)}\n")
    counter+=1
        
        
        
    