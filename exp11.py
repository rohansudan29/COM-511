hyp=float(input("enter the length of hypoteneus : "))
base=float(input("enter the length of base : "))
per=float(input("enter the length of perpendicular : "))
x=((base**2)+(per**2))**0.5
if x==hyp:
    print("The triangle is right angled triangle")
else:
    print("The triangle is not right angled triangle")
s=(hyp+base+per)/2
print(s)
a=s*(s-hyp)*(s-base)*(s-per)
if a>0:
    area=a**0.5
    print("Area of triangle is : ",area)
else:
    print("Triangle is not valid")
