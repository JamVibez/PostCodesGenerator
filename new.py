import math

a = input()
b = input()

a1 = (a[0:2])
a2 = (a[3:7])
inta = (int(a1)*1000)+int(a2)

b1 = (b[0:2])
b2 = (b[3:7])
intb = (int(b1)*1000)+int(b2)

c = int(math.fabs(inta-intb))
if inta>intb:
    y = intb
elif intb>inta:
    y = inta
else:
    print("Nie ma kodów pomiędzy!")

for x in range (1,c):
    newpostcode = y + x
    strnewpostcode = str(newpostcode)
    print(strnewpostcode[0:2]+"-"+strnewpostcode[2:])