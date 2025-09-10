'''
#30-04-2025
#1
char=input("Enter a character:")
if char in ('a','e','i','o','u','A','E','I','O','U'):
	print("VOWEL")
elif (65 <= ord(char) <= 90 or 97 <= ord(char) <= 122):
	print("CONSONANT")

#2
num=int(input("Enter num:"))
if num>=1 and num<=100:
	print("IN RANGE")
else:
	print("OUT OF RANGE")

#3
num=int(input("Enter num:"))
if num%2==0:
	print("EVEN")
	print(num**4)
else:
	print("ODD")

#4
num=int(input("ENTER NUM:"))
rem=num%10
if rem>5:
	print(rem, "is greater then 5")
else:
	print(rem, "is not greater than 5")

#5
num=int(input("ENTER NUM:"))
if num%3==0 and num<30:
	print(num**2)
elif num%3==0 and num>30:
	print(num,"is divisible by 3 but not less than 30")
elif num%3!=0 and num<30:
	print(num,"is not divisible by 3 but less than 30")
else:
	print(num , "is not divisible by 3 and not less than 30")

#6
num=int(input("Enter num:"))
if num%2==0:
	if num%4==0:
		print(num**3)
	else:
		print(num, "is even but not divisible by 4")
else:
	print(num,"is not even")

#7
num=int(input("Enter num:"))
if num%2==1:
	num-=1
	print(num)
else:
	print(num,"is EVEN ")

#8
num=int(input("Enter num:"))
if num>=10 and num<=45:
	print("IN RANGE")
else:
	print("OUT OF RANGE")

#9
age=int(input("Enter age:"))
weight=float(input("Enter weight (IN KGS): "))
if age>=18 and age<=65:
	if weight>=50:
		print("Eligible for blood donation")
	else:
		print("Your weight must be greater than 50")
else:
	print("Your age must be 18+")

#10
num=int(input("ENTER NUM:"))
if num%3==0 and num>90:
	print(num,"is divisible by 3 and greater than 90")
elif num%3==0 and num<90:
	print(num,"is divisible by 3 but not greater than 90")
elif num%3!=0 and num>90:
	print(num,"is not divisible by 3 but greater than 90")
else:
	print(num , "is not divisible by 3 and not greater than 90")

#11
char=input("ENTER CHARACTER:")
if 65<=ord(char)<=90:
	print(char, "is uppercase")
else:
	print("not uppercase")


#01-05-2025

#1
char=input("Enter character:")
if 97<=ord(char)<=122:
	print("LOWERCASE")
else:
	print("NOT LOWERCASE")

#2
char=input("Enter character:")
if 48<=ord(char)<=57:
	print("DIGIT")
else:
	print("NOT A DIGIT")

#3
char=input("Enter character:")
print(ord(char))

#4
num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
if num1>num2:
	print(num1," is greater than ",num2)
else:
	print(num2," is greater than ",num1)

#4.1
num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
num3=int(input("Enter number 3:"))
if num1>num2 and num1>num3:
	print(num1," is greater than ",num2 , num3)
elif num2>num1 and num2>num3:
	print(num2," is greater than ",num1 , num3)
else:
	print(num3," is greater than ",num1 , num2)

#5
num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
if num1<num2:
	print(num1," is lesser than ",num2)
else:
	print(num2," is lesser than ",num1)

#6
count=0
str1="HELLO WASTE FELLOW"
for i in range (0,len(str1)):
	if str1[i]!=" ":
		count+=1
if count%2==0:
	print("Even length of characters")

#7
age1=int(input("Enter person 1 age :"))
age2=int(input("Enter person 2 age :"))
if 18<=age1<=65 and 18<=age2<=65:
	print("Both persons can play chess")
elif 18<=age1<=65:
	print("Only Person 1 can play chess")
elif 18<=age2<=65:
	print("Only Person 2 can play chess")
else:
	print("Both cannot play chess")

#8
age=int(input("Enter age:"))
sex=input("Sex:").upper()
marital_status=input("Marital Status:").upper()
if 20<=age<=50 and (sex=="FEMALE") and (marital_status=="MARRIED" or marital_status=="UNMARRIED"):
	print("JOB LOCATION: HYDERABAD")
elif 20<=age<=50 and sex=="MALE" and (marital_status=="UNMARRIED" or marital_status=="MARRIED"):
	print("JOB LOCATION: BENGALURU")
else:
	print("NO LOCATION FOUND")


#9
character=input("Enter a character:")
char=ord(character)
if 65 <= char <= 90 or 97 <= char <= 122:
	print("ALPHABETS")
elif (48<=char<=57):
	print("Digit")
else:
	print("Special character")

#10
A1='A'
for i in range(1,27):
	print(A1,":", ord(A1))
	A1=chr(ord(A1)+1)

#11
attendance=float(input("Enter your attendance percentage:"))
if attendance>75.0:
	print("ALLOWED TO WRITE EXAMS")
else:
	print("NOT ALLOWED TO WRITE EXAMS")


#12
year_of_service=int(input("Enter year of service:"))
if year_of_service>5:
	print("10% BONUS IS ADDED")
else:
	print("NO BONUS")


#04-05-2025

#1
runs=int(input("Enter the runs scored :"))
if runs>100:
	print("BEST PERFORMANCE")
elif 50<runs<=100:
	print("BETTER PERFORMANCE")
elif 20<=runs<=50:
	print("GOOD PERFORMANCE")
else:
	print("BAD PERFORMANCE")

#2
num=int(input("Enter num:"))
if num%6==0:
	print(num," is divisible by 6")
else:
	print(num," is not divisible by 6")

#3
num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
if num1>num2:
	print(num1," is greater than ",num2)
else:
	print(num2," is greater than ",num1)

#4
num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
num3=int(input("Enter number 3:"))
if num1>num2 and num1>num3:
	print(num1," is greater than ",num2 , num3)
elif num2>num1 and num2>num3:
	print(num2," is greater than ",num1 , num3)
else:
	print(num3," is greater than ",num1 , num2)

#5
num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
if num1<num2:
	print(num1," is lesser than ",num2)
else:
	print(num2," is lesser than ",num1)

#6
num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
num3=int(input("Enter number 3:"))
if num1<num2 and num1<num3:
	print(num1," is lesser than ",num2 , num3)
elif num2<num1 and num2<num3:
	print(num2," is lesser than ",num1 , num3)
else:
	print(num3," is lesser than ",num1 , num2)

#7
for year in range(1,2026):
	if year%4==0 and (year%100!=0 or year%400==0):
		print(year)

#8
num=int(input("Enter num:"))
if num%8==0:
	print(num," is multiple of 8")
else:
	print(num," is not multiple of 8")

#9

price=int(input("Enter price of the t-shirt:"))
if 1500<=price<=2000:
	print("30% DISCOUNT")
elif 1000<=price<1500:
	print("20% DISCOUNT")
elif 500<=price<1000:
	print("10% DISCOUNT")
else:
	print("NO DISCOUNT APPLIED")


#10
sum=0
count=0
for num in range(1,101):
	sum+=num
	count+=1
avg=sum/count
print("SUM OF NATURAL NUMBERS FROM 1 TO 100: ",sum)
print("AVERAGE OF NATURAL NUMBERS FROM 1 TO 100: ",avg)

#11
odd_sum=0
even_sum=0
for num in range(1,101):
	if num%2==0:
		even_sum+=num
	else:
		odd_sum+=num
print(even_sum)
print(odd_sum)


#05-05-2025

#1
print("SIMPLE INTEREST")
principal=int(input("Enter principal amount:"))
rate_of_interest=float(input("Enter rate of interest:"))/100
years=int(input("Enter years:"))
Simple_Interest=(principal*rate_of_interest*years)/100
print(Simple_Interest)

#2
print("NATURAL NUMBERS FROM 1 TO 1000")
num=int(input("ENTER NUMBER:"))
for i in range(1,num+1):
    print(i)
    
#3
print("NATURAL NUMBERS FROM 1 TO 1000")
num=int(input("ENTER NUMBER:"))
for i in range(num,0,-1):
    print(i)

#4    
print("SUM AND AVERAGE OF NATURAL NUMBERS")
sum=0
count=0
for num in range(1,101):
	sum+=num
	count+=1
avg=sum/count
print("SUM OF NATURAL NUMBERS FROM 1 TO 100: ",sum)
print("AVERAGE OF NATURAL NUMBERS FROM 1 TO 100: ",avg)

#5
print("FACTORIAL FOR EACH NUMBER FROM 1 to N")
num=int(input("Enter num:"))
for i in range(1,num+1):
    num=i
    fact=1
    while i>0:
          fact*=i
          i-=1
    print(num ,":",fact)

#6
print("PRIME NUMBERS FROM 1 TO 10")
for i in range(1,11):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
            print(i)

#7
print("SUM OF PRIME NUMBERS FROM 1 TO 100")
sum=0
for i in range(1,101):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
            sum+=i
print(sum)

#8
print("SUM OF PERFECT NUMBERS FROM 1 TO 100")
sum1=0
for i in range(1,101):
    sum=0
    for j in range(1,i):
        if i%j==0:
            sum+=j
    if i==sum:
        sum1+=i
print(sum1)

#9
print("PALINDROMES FROM 1 TO 100")
for i in range(1,101):
    num=i
    rev=0
    while i>0:
           rem=i%10
           rev=rev*10+rem
           i//=10
    if rev==num:
            print(num)

#10
print("SUM OF PALINDROMES FROM 1 TO 100")
sum=0
for i in range(1,101):
    num=i
    rev=0
    while i>0:
           rem=i%10
           rev=rev*10+rem
           i//=10
    if rev==num:
            sum+=num
print(sum)

#11
print("COMPOSITE NUMBERS FROM 10 TO 1")
for i in range(10,0,-1):
    count=0
    for j in range(i,0,-1):
        if i%j==0:
            count+=1
    if count>2:
        print(i)

#12
print("SUM OF COMPOSITE NUMBERS FROM 1 TO 50")
sum=0
for i in range(1,51):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count>2:
            sum+=i
print(sum)

print("NUMBER IS PRIME PALINDROME OR NOT")
num=int(input("Enter num:"))
no=num
rev=0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num//=10
if rev==no:
    print(no)
    count=0
    for i in range(1,no+1):
           if no%i==0:
                count+=1
    if count==2:
        print(no," IS PRIME PALINDROME")
    else:
        print(no," IS NOT A PRIME BUT A PALINDROME")
else:
	print(no," IS NOT A PALINDROME")
'''
#06-05-2025

print("NUMBER OF PRIME PALINDROME FROM 1 to 1000")

for i in range(1,1001):
	count=0
	for j in range(1,i+1):
		if i%j==0:
			count+=1
	if count==2:
		num=i
		rev=0
		while num>0:
			rem=num%10
			rev=rev*10+rem
			num//=10
		if rev==i:
			print(i)

print("COUNT OF PRIME PALINDROMES FROM 1 to 1000")
count1=0
for i in range(1,1001):
	count=0
	for j in range(1,i+1):
		if i%j==0:
			count+=1
	if count==2:
		num=i
		rev=0
		while num>0:
			rem=num%10
			rev=rev*10+rem
			num//=10
		if rev==i:
			count1+=1
print(count1)

print("SUM OF PRIME PALINDROMES FROM 1 to 1000")
sum=0
for i in range(1,1001):
	count=0
	for j in range(1,i+1):
		if i%j==0:
			count+=1
	if count==2:
		num=i
		rev=0
		while num>0:
			rem=num%10
			rev=rev*10+rem
			num//=10
		if rev==i:
			sum+=i
print(sum)