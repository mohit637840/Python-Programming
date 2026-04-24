x,y,z=(input("enter three numbers")).split()
print("x=",x,"y=",y,"z=",z)
if x>y and x>z:
    print(x," is largest")
elif y>z:
    print(y," is largest")
else:
    print(z," is largest")