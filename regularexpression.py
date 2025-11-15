import re
string="happy learning"
# a=re.findall("g",string)
# print(a)

# result=re.search("g",string)
# print(result)
# print(result.start())

# result=re.search("g",string)
# print(result.span())
# print(result.string)

# string="happy learning"
# result=re.split("h",string)
# print(result)

# string="happy learning"
# result=re.split(" ",string)
# print(result)

# string="happy learning"
# result=re.split("",string)
# print(result)

# string="happy learning have a grear day"
# result=re.split(" ",string,3)
# print(result)

# string="happy learning have a grear day"
# result=re.sub(" ","-",string)
# print(result)


# string="happy learning have a grear day"
# result=re.sub(" ","-",string)
# print(result)

# string="happy learning have a grear day"
# result=re.sub("a","A",string)
# print(result)

# string="happy learning have a grear day"
# result=re.sub("a","*",string,6)
# print(result)


# Mete characters

# string="happy learning have a grear day"
# result=re.findall("[a]",string)
# print(result)

# string="happy learning have a grear day"
# result=re.findall("[Z]",string)
# print(result)


# string="happy learning have a grear day"
# result=re.findall("^hap",string)
# print(result)


# string="happy learning have a grear day"
# result=re.findall("ay$",string)            # to check end in list use in doller simple
# print(result)



# string="happy learning have a grear day"
# result=re.findall("l........",string)
# print(result)     

# string="happy learning have a grear day"
# result=re.findall("h........",string)
# print(result)  



# string="happy learning have a grear day"
# result=re.findall("...........h",string)
# print(result) 

# string="happy learning have a grear day"
# result=re.findall("..a",string)
# print(result) 


import re 
# strl="let us see what is meta character"
# result=re.findall("ee*",strl)

# print(result)


# strl="let us see what is meta character"
# result=re.findall("e*",strl)
# print(result)

# strl="let us see what is meta character"
# result=re.findall("et+",strl)
# print(result)

# strl="let us see what is meta character"
# result=re.findall("e{2}",strl)
# print(result)

# strl="let us see what is meta character"
# result=re.findall("\s",strl)
# print(result)

# strl="let us see what is meta character"
# result=re.findall("\S",strl)
# print(result)

# strl="let us see what is meta character12364"
# result=re.findall("\d",strl)
# print(result)

# strl="let us see what is meta character12364"
# result=re.findall("\D",strl)
# print(result)


# strl="let us see what is meta character12364"
# result=re.findall("\w",strl)
# print(result)

# strl="let us see what is meta character12364"
# result=re.findall("\W",strl)
# print(result)


# strl="let us see what is meta character12364"
# result=re.findall("[123]",strl)
# print(result)


# strl="let us see what is meta character12364"
# result=re.findall("[^123]",strl)
# print(result)

# strl="let us see what is meta character12364"
# result=re.findall("[0-4]",strl)
# print(result)



# strl="let us see what is meta character123"
# result=re.findall("[0-9][0-9][0-9]",strl)
# print(result)


# strl="let us see what is meta character123"
# result=re.findall("[0-9][0-9]",strl)
# print(result)



# strl="let us see what is meta character123"
# result=re.findall("[a-c]",strl)
# print(result)

# strl="let us see what is meta character123"
# result=re.findall("[a-f]",strl)
# print(result)



# def validate_phone_number(phone_number):
#     pattern="^[789]\d{9}$"
#     if re.match(pattern,phone_number):
#         return True
#     else:
#          return False
# phone_numbers=["9786699395","12347855909","888844321","23133453"]
# for number in phone_numbers:
#     if validate_phone_number(number):
#         print(f"{number} is a valid phone number")
#     else:
#         print(f"{number} is not a valid phone number")

  

# def is_valid_email(email):
#     pattern=r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-z]{5}/.[a-z]{2,3}$"
    
#     return bool (re.match(pattern,email))
    
# email="naveenkumarsj@gmail.com"
# if is_valid_email(email): 
#         print(f"{email} is a valid email address ")
# else:
#           print(f"{email} is  not a valid email address ")   
        
    

