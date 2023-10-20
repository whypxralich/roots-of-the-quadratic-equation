print("Hello! I'll help you find the roots of the quadratic equation!")

print("Enter a")
a = int(input())
print("Enter b")
b = int(input())
print("Enter c")
c = int(input())

discriminant = ((b**2) - (4*a*c))
if discriminant > 0 or discriminant == 0:
    x1 = ((-b) + (discriminant ** 0.5)) / (2*a)
    x2 = ((-b) - (discriminant ** 0.5)) / (2*a)
    print ("The first root of the equation:", x1)
    print ("The second root of the equation:", x2)

if discriminant < 0: 
    print ("It is impossible to find a discriminant (D<0)")