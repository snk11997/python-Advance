a=int(input("enter no"))
if a%2==0:
   print("it is even number")
if a%2==1:
   print("odd no")

a=input("enter your name")
b=a[::-1]
if b==a:
    print("it is a palindrome")
else:
    print("it is a not palindrome")
    
     
a=input("enter your name")   
for i in range(len(a)):
    print("it is a string")
    print(a[i])
def reverse(a_string):
    """
    Reverse a string.

    Args:
        a_string (str): The string to reverse.

    Returns:
        str: The reversed string.

    """
    return a_string[::-1]


def is_palindrome(a_string):
    """
    Check if a string is a palindrome.

    Args:
        a_string (str): The string to check.

    Returns:
        bool: Whether the string is a palindrome or not.

    """
    return a_string == reverse(a_string)


a = input("Enter a string: ")
if is_palindrome(a):
    print(f"{a} is a palindrome.")
else:
    print(f"{a} is not a palindrome.")def reverse(a_string):
        """
        Reverse a string.
    
        Args:
            a_string (str): The string to reverse.
    
        Returns:
            str: The reversed string.
    
        """
        return a_string[::-1]
    
    
    def is_palindrome(a_string):
        """
        Check if a string is a palindrome.
    
        Args:
            a_string (str): The string to check.
    
        Returns:
            bool: Whether the string is a palindrome or not.
    
        """
        return a_string == reverse(a_string)
    
    
    a = input("Enter a string: ")
    if is_palindrome(a):
        print(f"{a} is a palindrome.")
    else:
        print(f"{a} is not a palindrome.")def reverse(a_string):
            """
            Reverse a string.
        
            Args:
                a_string (str): The string to reverse.
        
            Returns:
                str: The reversed string.
        
            """
            return a_string[::-1]
        
        
        def is_palindrome(a_string):
            """
            Check if a string is a palindrome.
        
            Args:
                a_string (str): The string to check.
        
            Returns:
                bool: Whether the string is a palindrome or not.
        
            """
            return a_string == reverse(a_string)
        
        
        a = input("Enter a string: ")
        if is_palindrome(a):
            print(f"{a} is a palindrome.")
        else:
            print(f"{a} is not a palindrome.")def reverse(a_string):
                """
                Reverse a string.
            
                Args:
                    a_string (str): The string to reverse.
            
                Returns:
                    str: The reversed string.
            
                """
                return a_string[::-1]
            
            
            def is_palindrome(a_string):
                """
                Check if a string is a palindrome.
            
                Args:
                    a_string (str): The string to check.
            
                Returns:
                    bool: Whether the string is a palindrome or not.
            
                """
                return a_string == reverse(a_string)
            
            
            a = input("Enter a string: ")
            if is_palindrome(a):
                print(f"{a} is a palindrome.")
            else:
                print(f"{a} is not a palindrome.")