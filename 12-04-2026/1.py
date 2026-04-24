# num=int(input("enter three digit number"))
# sum=0
# first_num=num%10
# num=num//10
# second_num=num%10
# num=num//10
# third_num=num%10
# num=num//10
# sum=first_num+second_num+third_num
# print(sum)

num=int(input("enter a number"))
total=0
while num>0:
    digit=num%10
    total+=digit
    num=num//10
print(total)
