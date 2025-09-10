# --- Print first 10 fibonacci series
# --- write a function to print prime numbers
# when user enters the year it should display the calender
# --- Write a function to check whether the given year is leap year or not
# --- write a program to check armstrong number
# --- write a function to find the sum of natural numbers
# write a program to check the given number is happy number or not
# --- write a program to check the given number is positive , negative or zero
# write a program to convert user input to slug field
# convert the integer into binary
# --- harshad number
'''
#1
a=0
b=1
sum=0
print(a)
print(b)
for i in range(1,9):
    sum=a+b
    print(sum)
    a=b
    b=sum
    sum=0

#8
num=int(input("Enter num:"))
if num>0:
    print("Positive number")
elif num<0:
    print("Negative Number")
else:
    print("Zero")

#6
def sum_naturalnumbers(num):
    sum=0
    for i in range(1,num+1):
        sum+=i
    return sum
num=int(input("enter a num to find sum of natural numbers from 1 to the number given by you:"))
res=sum_naturalnumbers(num)
print("The sum of natural numbers:",res)

#11
#harshad number
num=int(input("Enter num:"))
num1=num
sum=0
while num>0:
 r   rem=num%10
    sum+=rem
    num//=10
if num1%sum==0:
    print("True")
else:
    print("False")

#4
def leapyear(year):
    if (year%4==0) or (year%100==0 and year%400==0):
        print("Leap year")
    else:
        print("Not a leap year")
year=int(input("Enter year:"))
leapyear(year)

#2
def prime_number(num):
    for i in range(1,num+1):
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        if count==2:
            print(i)
num=int(input("Enter num:"))
prime_number(num)

#5

num=int(input("Enter num:"))
num1=num
num2=num
count=0
while num1>0:
    rem=num%10
    count+=1
    num1//=10
sum=0
while num2>0:
    rem1=num2%10
    sum+=rem1**count
    num2//=10
if num==sum:
    print("Armstrong number")
else:
    print("Not an armstrong number")


#7
num=int(input("Enter num:"))
while num!=1 and num!=4:
    sum=0
    while num>0:
        rem=num%10
        sum+=rem**2
        num//=10
    num=sum
if num==1:
    print("Happy number")
else:
    print("Not a Happy number ")


#HOLLOW CUBE
num=int(input("ENTER ANY ODD NUMBER:"))
mid=(num+1)//2
mid1=mid//2
print(mid)
print(mid1)
for i in range(1,num+1):
    for j in range(1,num+1):
        if ((i==1 and j>mid1) or (j==mid1+1 and i<=num-mid1) or (i==num-mid1 and j>mid1) or (j==num and i<=num-mid1)) or ((i==mid1+1 and j<num-mid1) or (i>=mid1+1 and j==1) or (i==num and j<=num-mid1) or (i>mid1+1 and j==num-mid1)) or (i+j==mid1+2 and i<=mid1+1) or (i+j==num+1 and j>=num-mid1) or (i+j==num+1 and j<=mid1) or (i+j==(num*2)-mid1):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

#solid cube
num=int(input("ENTER ANY ODD NUMBER:"))
mid=(num+1)//2
mid1=mid//2
print(mid)
print(mid1)
for i in range(1,num+1):
    for j in range(1,num+1):
        if ((i>=1 and j>mid1 and i<=num-mid1)) or (i>=mid1+1 and j<=num-mid1) or ((i+j>=mid1+2 and i<mid1+1)) or (i+j<=(num*2)-mid1 and i>mid1):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
'''

num=9
mid=(num+1)//2
mid1=(mid)//2
for i in range(1,num+1):
    for j in range(1,num+1):
        if ((i==1 or j==num or j==1 or i==num)) or ((i==mid1+1 and j>mid1 and j<=num-mid1)) or (i>=mid1+2 and j==mid1 and i<num-mid1) or ((i==(num-mid1)) and j>mid1 and j<=num-mid1) or (i>=mid1+2 and j==num-1 and i<num-mid1) or (i+j>=9 and j>=mid1+1 and j<=num-mid1 and i<num-mid1 and i>mid1):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
