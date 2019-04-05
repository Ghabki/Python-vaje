import math
a = 9.81

b = float(input("Vstavi hitrost iztrelka"))
c = float(input("Vstavi kot iztrelka"))

c = math.radians(c)
d = (b**2*math.sin(2*c))/a

print("Razdaljad ",d)