a="Madres university"
print(a.center(80,"*"))  
print("1.administion, 2.student")
b=int(input("select any one"))
if b==1:
    c=int(input("enter a number of students"))      
    if c==1:
        s1=input("enter a student name")
        s2=(input("enter reg no"))
        s3=int(input("enter a tamil mark"))
        s4=int(input("enter a English mark"))
        s5=int(input("enter a Maths mark"))
        s6=int(input("enter a sciencee mark"))
        s7=int(input("enter a social mark"))
        print("uploaded sucessfully")
        print("1.administion, 2.student")
        d=int(input("select any one"))
        if d==2:
                     e=input("enter a student name: ")
                     f=(input("enter a reg no: "))
                     if s1==e and s2==f:
                         print(s3) ,print(s4),print(s5),print(s6),print(s7)
                         g=s3+s4+s5+s6+s7
                         print("result: total mark",g)
                         if s3>35 and s4>35 and s5>35 and s6>35 and s7>35:
                                 print("you are pass")
                         else:
                                 print("fail")
                                          
                     
    elif c==2:
        s1=input("enter a student name")
        s2=int(input("enter reg no"))
        s3=int(input("enter a tamil mark"))
        s4=int(input("enter a English mark"))
        s5=int(input("enter a Maths mark"))
        s6=int(input("enter a sciencee mark"))
        s7=int(input("enter a social mark"))
        print("uploaded sucessfully")
        print("1.administion, 2.student")
        d=int(input("select any one"))
         
        if d==2:
                 e=input("enter a student name: ")
                 f=int(input("enter a reg no: "))
                 if s1==e and s2==f:
                    print(s3) ,print(s4),print(s5),print(s6),print(s7)
                    g=s3+s4+s5+s6+s7
                    print("result: total mark",g)
                    if s3>35 and s4>35 and s5>35 and s6>35 and s7>35:
                        print("you are pass")
                    else:
                        print("fail")
         if d==2:
              marks1=input("enter a student name")
              marks2=int(input("enter reg no"))
              marks3=int(input("enter a tamil mark"))
              marks4=int(input("enter a English mark"))
              marks5=int(input("enter a Maths mark"))
              marks6=int(input("enter a sciencee mark"))
              marks7=int(input("enter a social mark"))
              print("uploaded sucessfully")
              print("1.administion, 2.student")
              d=int(input("select any one"))
     
              if d==2:
                 e1=input("enter a student name: ")
                 f1=int(input("enter a reg no: "))
                 if marks1==e1 and marks2==f1:
                    print(marks3) ,print(marks4),print(marks5),print(marks6),print(marks7)
                    g=marks3+marks4+marks5+marks6+marks7
                    print("result: total mark",g)
                    if marks3>35 and marks4>35 and marks5>35 and marks6>35 and marks7>35:
                        print("you are pass")

##                    else:
##                        print("fail")
##
##                  

else:
    print("NO DATA AVALIBLE")
    
