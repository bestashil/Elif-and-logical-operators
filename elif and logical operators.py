#Q1 Print day name using day number (1–7)---------->
Day=int(input("Enter a day :"))
if Day==1 :
    print("Monday")
elif Day==2 :
    print("Tuesday")
elif Day==3 :
    print("Wednesday")
elif Day==4 :
    print("Thursday")
elif Day==5 :
    print("Friday")
elif Day==6 :
    print("Saturday")
elif Day==7 :
    print("Sunday")
else :
    print("This day number is not exist !")

#Q2 Print month name using month number--------------->
months=int(input("Enter a months :"))
if months==1 :
    print("January")
elif months==2 :
    print("February")
elif months==3 :
    print("march")
elif months==4 :
    print("April")
elif months==5 :
    print("May")
elif months==6 :
    print("June")
elif months==7 :
    print("July")
elif months==8 :
    print("August")
elif months==9 :
    print("September")
elif months==10 :
    print("October")
elif months==11 :
    print("November")
elif months==12 :
    print("December")
else :
    print("This day number is not exist !")

#Q3 Display bonus percentage based on experience years-------------------->

ER=int(input("Enter your experience year:"))
if ER>=5 :
    print("70% bonus on your experience ")
elif ER>=3 :
    print("50% bonus on your experience ")
elif ER>=2 :
    print("35% bonus on your experience ")
elif ER>=1 :
    print("25% bonus on your experience ")
else :
    print("15% bonus Your experience is normal")

#Q4 Identify traffic signal meaning------------->
signal=input("Enter signal: ")

if signal=="red" :
    print("Stop")
elif signal=="yellow" :
    print("Ready")
elif signal=="green" :
    print("Go")
else :
    print("traffic signal not work in proper way")

#Q5 Categorize temperature as Cold / Warm / Hot--------------->
temp=int(input("Enter temperature : "))

if temp<=15 :
    print("cold")
elif temp<=30 :
    print("warm")
else :
    print("Hot")

#Q6 Categorize employee based on salary range------------------->

salary = int(input("Enter your salary: "))
if salary >=100000 :
    print("You are a enter in A grade categorize")
elif salary >=80000 :
    print("You are a enter in B grade categorize")
elif salary >=60000 :
    print("You are a enter in C grade categorize")
elif salary >=30000 :
    print("You are a enter in D grade categorize")
else :
    print("You are a enter in E grade categorize")

#Q7 Print discount percentage based on purchase amount----------------->
pamount=int(input("Enter the  purchase amount : "))

if pamount >=10000:
    print("25% Discount ")
elif pamount>8000 :
    print("18% Discount ")
elif pamount>=6000 :
    print("12% Discount ")
else :
    print("8% Discount ")

#Q8 Identify number type: single-digit / double-digit / multi-digit--------->
number=int(input("Enter a number: "))

if number>=0 and number<=9 :
    print("Single digit number ")
elif number>9 and number<=99 :
    print("Double digit number ")
else :
    print("Multi digit number ")

#Q9 Check whether a number is divisible by 5 and 11-------------->
number = int(input("Enter a number: "))
if number%5==0 or number%11==0 :
    print("divisible ")
else :
    print("not divisible ")

#Q10 Check if a person is eligible for loan:
# ● age ≥ 21
# ● salary ≥ 25,000
# ● credit score ≥ 700

age=int(input("Enter your age:"))
salary=int(input("Enter your salary:"))
creditscore=int(input("Enter your credit score:"))

if age>=21 :
   if salary>=25000 :
       if creditscore>=700 :
         print("You are a eligible")
       else :
         print("You are not eligible")
   else :
       print("You are not eligible")
else :
   print("You are not eligible")

#Q11 Validate login using username AND password------->
username=input("Enter your username: ")
password=input("Enter your password: ")

if username=="admin" and password=="admin123":
    print("Validate login ")
else:
    print("Invalid username or password")

#Q12 Create an ATM withdrawal program with balance checks-------->
#ATM Withdrawal Program

balance = int(input("Enter your account balance: "))
withdraw = int(input("Enter withdrawal amount: "))

if withdraw > 0:
    if withdraw <= balance:
        balance = balance - withdraw
        print("Withdrawal successful!")
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance!")
else:
    print("Invalid withdrawal amount!")

