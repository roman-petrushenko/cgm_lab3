import matplotlib.pyplot as plt
import math
a1 = list()
b1 = list()
f1 = open("DS3.txt", "r")
while True:
    c1 = f1.readline().split(" ")
    if (c1[0] == ""):
        break
    a1.append(int(c1[0]))
    b1.append(int(c1[1].replace("\n","")))
a2 = list()
b2 = list()
i = 0
while (i<len(a1)):
    t = 40*math.pi/180
    a2.append((int(a1[i])-480)*math.cos(t)+(int(b1[i])-480)*(-1)*math.sin(t)+480)
    b2.append((int(a1[i])-480)*math.sin(t)+(int(b1[i])-480)*math.cos(t)+480)
    i+=1
plt.figure(figsize=(960/100, 960/100))
plt.scatter(a2,b2)
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("cgr.png")
plt.show()