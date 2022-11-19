# programa que suma 2 numeros

# existen variables comunes
# estas variables tienen un tipo cada una
# estos tipos son, string()


a= int(input("input numero a: "))
b= int(input("input numero b: "))
# "9"
# "6"
# al sumar strings se le denomina concatenacion y es juntar estos dos strings 
# 96


def suma(a,b):
    c= a+b
    return c

c= suma(a,b)
print(c)