import Image
import ImageEnhance
import math

out = "pippo.jpg"

numImg=3

im=dict()
for i in range(numImg):
	im[i] = Image.open("%d.jpg" % (i, ))
imOut = out

image_width = im[1].size[0]
image_height = im[1].size[1]

print(image_width)
print(image_height)

p=dict()
l=dict()
v=dict()
np=dict()

#comment

for x in range(image_width):
	for y in range(image_height):
		for i in range(numImg):
			p[i] = im[i].getpixel((x,y))
			l[i]=math.sqrt(p[i][0]*p[i][0]+p[i][1]*p[i][1]+p[i][2]*p[i][2])/(255.0*math.sqrt(3))
			v[i]=math.fabs(l[i]-0.5)
		
		b = dict(map(lambda item: (item[1],item[0]),v.items()))
		min_key = b[min(b.keys())]
		
		for i in range(3):
			np[i]=p[min_key][i]

		im[1].putpixel((x,y),(np[0],np[1],np[2]))

	if x % 100 == 0:
		print(x)

im[1].save(imOut)

print("end")
