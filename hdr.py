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

for x in range(image_width):
	for y in range(image_height):
		l_tot=0
		for i in range(numImg):
			p[i] = im[i].getpixel((x,y))
			l[i]=(max((p[i][0],p[i][1],p[i][2]))-min((p[i][0],p[i][1],p[i][2])))/510.0
			l_tot+=l[i]
			
		for i in range(numImg):
			v[i]=l[i]/l_tot
		
		b = dict(map(lambda item: (item[1],item[0]),v.items()))
		best_one = b[max(b.keys())]
		
		for i in range(3):
			np[i]=p[best_one][i]

		im[1].putpixel((x,y),(np[0],np[1],np[2]))

	if x % 100 == 0:
		print(x)

im[1].save(imOut)

print("end")
