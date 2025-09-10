# str1=input("Enter a string:")
# str2=""
# for i in str1:
#     if not(len(str1)>=1 and (i=="_" or 65<=ord(i)<=90)):
#         print("false")
#     else:
#         print("True")
#         print(len(str2.split("_")))

str1 = input("Enter a string:")
valid = True

for i in str1:
    if not (i == "_" or 65 <= ord(i) <= 90):
        valid = False
        break

if valid:
    print("True")
    print(len(str1.split("_")))
else:
    print("false")