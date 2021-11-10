f = open('input.txt', 'r')
i=1
x=[]
y=[]
z=[]
for line in f:
    for word in line.split():
        if i%3==1:
            x.append(word)
        elif i%3==2:
            y.append(word)
        else:
            z.append(word)
        i+=1
f.close()

xString = yString = zString = '['

for i in range(len(x)-1):
    xString += (str(x[i]))
    xString += "; "
xString += str(x[-1])
xString += ']'

for i in range(len(y)-1):
    yString += (str(y[i]))
    yString += "; "
yString += str(y[-1])
yString += ']'

for i in range(len(z)-1):
    zString += (str(z[i]))
    zString += "; "
zString += str(z[-1])
zString += ']'

out = open('outputTIN.txt', 'w')
out.write("x = " + xString)
out.write('\n\n')
out.write("y = " + yString)
out.write('\n\n')
out.write("z = " + zString)
out.write('\n\n')
out.close()

