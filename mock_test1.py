# Program to print last character of your name using pattern programming
# Sum of leap years from 2000 to 2025
# Fibonicci Series
# Sad numbers from 1 to 1000
# Program to find the given number is Neon Number or not
# Program to find the given number is Spy Number or not
# Program to find the given number is Harshad Number or not
# Program to find given number is prime palindrome or not
# Program to print armstrong numbers from 1000 to 500
# Swastik Pattern
# pattern : 2  4  6  8
#           10 12 14 16
#           18 20 22 24
#           26 28 30 32
# pattern: 2
#          4 6
#          8 10 12
#          14 16 18 20
#          22 24 26 28 30

#1
print("Program to find given number is prime palindrome or not")
num=int(input("Enter num:"))
count=0
num1=num
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count==2:
    rev=0
    while num1>0:
        rem=num1%10
        rev=rev*10+rem
        num1//=10
    if rev==num:
        print("Prime Palindrome")
else:
    print("Not a Prime Palindrome")

#2
print("Program to print armstrong numbers from 1000 to 500")
for num in range(1000,500,-1):
    count=0
    num1=num
    num2=num
    while num1>0:
        count+=1
        num1//=10
    sum=0
    while num2>0:
        pow=1
        rem=num2%10
        for i in range(1,count+1):
            pow*=rem
        sum+=pow
        num2//=10
    if sum==num:
        print(num)

#3
print("Swastik Pattern")
num=11
for i in range(1,num+1):
    for j in range(1,num+1):
        if (i==1 and j>(num+1)//2) or (i==num and j<(num+1)//2) or (j==1 and i<(num+1)//2) or (j==num and i>(num+1)//2) or (j==(num+1)//2 and i!=1 and i!=num and i!=(num+1)//2) or (i==(num+1)//2 and j!=1 and j!=num and j!=(num+1)//2):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

#4
print("Program to find the given number is Harshad Number or not")
num=int(input("Enter num:"))
sum=0
num1=num
while num1>0:
    rem=num1%10
    sum+=rem
    num1//=10
if num%sum==0:
    print("Harshad Number")
else:
    print("Not an Harshad Number")

#5
print("Program to find the given number is Spy Number or not")
num=int(input("Enter num:"))
num1=num
num2=num
sum=0
product=1
while num1>0:
    rem=num1%10
    sum+=rem
    num1//=10
while num2>0:
    rem=num2%10
    product*=rem
    num2//=10
if sum==product:
    print("Spy number")
else:
    print("Not a Spy Number")

#6
print("Program to find the given number is Neon Number or not")
num=int(input("Enter num:"))
square=num**2
sum=0
while square>0:
    rem=square%10
    sum+=rem
    square//=10
if num==sum:
    print("Neon number")
else:
    print("Not a Neon number")

#7
print("Sad numbers from 1 to 1000")
count=0
for num in range(1,1001):
    num1=num
    while num1!=1 and num1!=4:
        sum=0
        while num1>0:
            rem=num1%10
            sum+=rem**2
            num1//=10
        num1=sum
    if num1!=1:
        print(num)
        count+=1
print(count)

#8
print("Fibonicci Series")
a=0
b=1
print(a)
print(b)
for i in range(1,11):
    sum=a+b
    print(sum)
    a=b
    b=sum

#9
print("Sum of leap years from 2000 to 2025")
sum=0
for y in range(2000,2026):
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        sum+=y
print(sum)

#10
num1=2
num=4
for i in range(1,num+1):
    for j in range(1,num+1):
        print(num1,end=' ')
        num1+=2
    print()

#11
num1=2
num=5
for i in range(1,num+1):
    for j in range(1,num+1):
        if i>=j:
            print(num1,end=' ')
            num1+=2
    print()

#12
print("Program to print last character of your name using pattern programming")
num=9
for i in range(1,num+1):
    for j in range(1,num+1):
        if (i==1 and j!=1 and j!=num) or (j==1 and i!=1) or (j==num and i!=1) or (i==(num+1)//2):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

