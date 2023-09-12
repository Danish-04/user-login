import random
n=0
while(n<3):
    userid=input("Enter the user name")
    password=(input("Enter the password"))

    if userid == "Danishkhan" and password=="Danish123":
        Generateotp=random.randint(1111,9999)
        print(Generateotp)
        otp=int(input("Please enter the OTP :-"))
        if otp == Generateotp:
            print("Login Successfull..!")   
            break

    else:
        print("Login Failed...!")
        n+=1

