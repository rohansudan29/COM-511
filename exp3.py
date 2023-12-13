a="Welcome to Python world"
print("Given string is :",a)
ac=sum(1 for char in a if char.isalpha())
print("number of alphabet in given string : ",ac) 
si=int(input("Enter the starting address: "))
ei=int(input("Enter the end address: "))
print("Extracted string : ",a[si:ei])
print("The given is string alphanumeric : ",a.isalnum())
 
