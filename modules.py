# import random
# a=random.randint(1,10)
# print(a)

# b=random.randint(1000,9999)
# print(b)
# c=random.randrange(1,20)
# print(c)


import smtplib
import random

def generate_otp():
    otp = ""
    for _ in range(6):
        otp += str(random.randint(0, 9))
    return otp

def send_email_otp(sender_email, sender_password, recipient_email, otp):
    subject = "Your OTP"
    body = f"Your One-Time Password (OTP) is: {otp}"

    message = f"Subject: {subject}\n\n{body}"

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, message)
        print("OTP sent successfully!")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    sender_email = "naveensangar97@gmail.com"
    sender_password = "save adjg uxji uwbh"
    recipient_email = input("Enter recipient email: ")
    otp = generate_otp()
    send_email_otp(sender_email, sender_password, recipient_email, otp)

    received_otp = input("Enter the received OTP: ")

    if received_otp ==otp:
        print("Login successful!")
    else:
        print("Incorrect OTP. Login failed.")

