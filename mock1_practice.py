#prime number
count=0
num=int(input("Enter num:"))
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count==2:
    print("prime number")
else:
    print("Not a prime number")

#prime numbers from 1 to 100 , count ,sum
count1=0
sum=0
for i in range(1,101):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        print(i)
        count1+=1
        sum+=i
print(sum)
print(count1)

#composite number
count=0
num=int(input("Enter num:"))
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count>2:
    print("composite number")
else:
    print("Not a composite number")

#composite numbers from 1 to 100 , count , sum
count1=0
sum=0
for i in range(1,101):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count>2:
        print(i)
        count1+=1
        sum+=i
print(sum)
print(count1)

#Perfect number
sum=0
num=int(input("Enter num:"))
for i in range(1,num):
    if num%i==0:
        sum+=i
if num==sum:
    print("Perfect number")
else:
    print("Not a perfect number")

#Perfect numbers from 1 to 1000 , count,sum
sum1=0
count1=0
for i in range(1,1001):
    sum=0
    for j in range(1,i):
        if i%j==0:
            sum+=j
    if sum==i:
        print(i)
        count1+=1
        sum1+=i
print(sum1)
print(count1)

#factorial of a number
num=int(input("Enter num:"))
fact=1
for i in range(1,num+1):
    fact*=num
    num-=1
print(fact)

#factorial of 1 to 100 numbers,sum
sum=0
for i in range(1,11):
    fact=1
    for j in range(1,i+1):
        fact*=j
    sum+=fact
    print(i,"!= ",fact)
print(sum)

#Strong number
num=int(input("Enter num:"))
num1=num
sum=0
while num>0:
    rem=num%10
    num//=10
    fact=1
    for i in range(1,rem+1):
        fact*=i
    sum+=fact
if sum==num1:
    print("Strong Number")
else:
    print("Not a strong number")

#strong numbers from 1 to 100, count,sum
count=0
sum1=0
for i in range(1,10001):
    num1=i
    sum=0
    while num1>0:
        rem=num1%10
        num1//=10
        fact=1
        for j in range(1,rem+1):
            fact*=j
        sum+=fact
    if sum==i:
        print(i)
        count+=1
        sum1+=i
print(sum1)
print(count)

#armstrong number
num=int(input("Enter num:"))
num1=num
num2=num1
count=0
while num>0:
    count+=1
    num//=10
sum=0
while num1>0:
    pow=1
    rem=num1%10
    pow=rem**count
    sum+=pow
    num1//=10
if sum==num2:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

#armstrong numbers from 1 to 100,count ,sum
count1=0
sum1=0
for i in range(1,1001):
    num1=i
    num2=i
    count=0
    while num1>0:
        count+=1
        num1//=10
    sum=0
    while num2>0:
        pow=1
        rem=num2%10
        pow=rem**count
        sum+=pow
        num2//=10
    if sum==i:
        print(i)
        count1+=1
        sum1+=i
print(count1)
print(sum1)

#palindrome numbers
num=int(input("Enter num:"))
num1=num
rev=0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num//=10
if num1==rev:
    print("Palindrome number")
else:
    print("Not a palindrome number")

#palindrome numbers from 1 to 100 , count, sum
count=0
sum=0
for i in range(1,101):
    num1=i
    rev=0
    while num1>0:
        rem=num1%10
        rev=rev*10+rem
        num1//=10
    if rev==i:
        print(i)
        count+=1
        sum+=i
print(count)
print(sum)

#prime palindrome
for i in range(1,101):
    num1=i
    rev=0
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:        
        while num1>0:
            rem=num1%10
            rev=rev*10+rem
            num1//=10
    if rev==i:
        print(i)
            # count+=1
            # sum+=i  