print("Password checker")
print("1.Sigin 2.Login")
print("select any one")
a=int(input())
if a==1:
    print("enter your name")
    b=input()
    print("enter your password")
    c=input()
    
    x=len(c)
    
    if x>=8:
        #if "1" in c or "2" in c or "3" in c or "4" in c or "5" in c or "6" in c or "7" in c or "8" in c or "9" in c or "0" in c:
            if "!" in c or "@" in c or "#" in c or "%"in c or "^" in c or "&" in c or "*" in c or "$" in c:
                #if c.isalpha() :
                if c.isalnum():
                    print("registered sucessfully")
                    print("1 Sigin 2.Login ")
                    m=input("enter username")
                    n=input("enter password")
                    if m==b and n==c:
                        print("login sucessfully") 
                    else:
                        print("password invalid")
                else:
                    print("Min one alphabets and numbers  ")
            else:
                print("min 1 specia")
        #else:
            #print("MIn 1 number")
    else:   
        print("min 8 character")

else:
     print("You have to signin first")






           
##    if x>8:
##        print("password must contain 8 character")
##
##        y=1,2,3,4,5,7,8,9,0
##        z=x.find("1,2,3,4,5,6,7,8,9,0")
##        if x>8 and c is z :
##            
##            print("passsword contain minimum one number")
##            e=" $,%,^,&,*,#,!"
##            m=x.find("$,%,^,&,*,#,!")
##            if x>8 and c is z and m is c:
##                print("password contain minimum one special character")
##            if  x>8 and c is z and m is c:
##                print("registered sucessfully")
##                
##                print("registered sucessfully")
##                print("1 Sigin 2.Login ")
##                b=input("enter username")
##                c=input("enter password")
##                print("login sucessful") 
##
##            else:
##                    print("password invalid")
##                
##                    
##else:
##     print("You have to signin first")
            
            
            
            
              
