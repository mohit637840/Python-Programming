n=6
sum=0
num=int(input("Enter n digit number"))
for i in range(1,n+1):
    digit=num%10
    num=num//10
    sum+=digit
print(sum)