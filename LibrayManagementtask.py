a="LIBRAY MANAGEMENT"
print(a.center(80,"*"))
print("1.Administraction , 2.customer")
b=int(input("select any one"))
if b==1:
    c=int(input(" Enter the No of books"))
    if c==3:
        d=input("book name").lower()
        e=input("Author name ").lower()
        f=input("Year ")
        g=input("price")
        h=input("book name").lower()
        i=input("Author name ").lower()
        j=input("Year ")
        k=input("price")
        l=input("book name").lower()
        m=input("Author name ").lower()
        n=input("Year ")
        o=input("price")
        print("uploaded sucessfully")
        print("1.Administraction , 2.customer")
        p=int(input("select any one"))
        if p==2:
            print("1.select category 2.Rent")
            w=int(input("select any one"))
            if w==1:
                print(" 1.Book name  ,2.Author name, 3.Year ,4.Price ")
                print("select any one")
                q=int(input())
                if q==1:
                    r=input("enter the book name :")
                    if d==r:
                        print(" Python, Guido, 1970, 5000 ")
                    if h==r:
                        print("Java,   Arun, 1998, 7000")
                    if l==r:
                        print("React , Guido, 2010 ,6000")

                    else:
                        print(" Your choosing book name not avalible in libray")

                elif q==2:
                     s=input("enter the Author name")
                     if s==e :
                         print(" Python, Guido,1970,5000 ")
                     if s==i:
                         print("Java,   Arun, 1998, 7000")
                     if s==m:
                         print("React , Guido, 2010 ,6000")
                     else:
                         print(" Your choosing book name not avalible in libray")
                
                elif q==3:
                     t=int(input(" Enter the year "))
                    
                     if t> 2000:
                         print("Java,   Arun, 1998, 7000")
                         print(" Python, Guido,1970,5000 ")
                     elif t>2012:
                         print(" Python, Guido,1970,5000 ")
                         print("Java,   Arun, 1998, 7000")
                         print("React , guido, 2010 ,6000")

                     else:
                         print(" you selecting year of books not avalible in library")
                elif q==4:
                     v=int(input("enter the price"))
                     if v>6000:
                           print("Java,   Arun, 1998, 7000")
                     elif v>4000:
                         print(" Python, Guido,1970,5000 ")
                         print("Java,   Arun, 1998, 7000")
                         print("React , guido, 2010 ,6000")
                       
                     else:
                         print(" you selecting price of books not avalible in library")


            if w==2:
                print("Enter a book name")
                count1=input()
                print(" per day 100rs")
                N3=int(input("enter a number of days"))      
                N4=100*N3
                print(" your rent " ,N4)       
                print("Thanks for purchasing")

                print("1.BUY AGAIN 2.EXIT")
                N5=int(input("select any one"))
                if N5==1:
                     
                     print("Enter a book name")
                     N6=input().lower()
                     if count1==N6:
                             print("This Book is sold out, come back after ", N3 , "Days" )
                             print("available books")
                             print("1.Java, 2. React ")
                             N7=input("enter a book name").lower()
                             if N7==h or N7==l:
                                
                                print(" per day 100rs")
                                N9=100
                                N10=int(input("enter a number of days"))       
                                N11=100*N10
                                print(" your rent is " ,N11)       
                                print("Thanks for purchasing")
                                   
                             else:
                                 print(" this not available in our library")
                     elif N6==h:     
                            print(" per day 100rs")
                            j1=100
                            j2=int(input("enter a number of days"))       
                            j3=100*j2
                            print(" your rent is " ,j3)       
                            print("Thanks for purchasing")
                     else:
                             
                            print(" this not available in our library")
                     if N6==l:

                             print(" per day 100rs")
                             j1=100
                             j2=int(input("enter a number of days"))       
                             j3=100*j2
                             print(" your rent is " ,j3)       
                             print("Thanks for purchasing")
                     else:
                        print(" this not available in our library")
                                  
                      
                else:
                    print("EXIT")


else:
    print("No books avalible in library")
             


                
                    


                
                
                 
                 

            
        








          

