import Image
import ImageEnhance
import math

class HDR:
	
	def __init__(self, numImg=1,out="out.jpg",blend=0.5):
		self.blend=blend
		
		images=[Image.open("%d.jpg" % i) for i in range(numImg)]
		new=self.merge_all(images)
		new.save(out)
		

	def get_masks(self,imgs):
		masks=[]
		masks_cnt=len(imgs)-1
		
		bws=[img.convert(mode='L') for img in imgs]
		
		for i in range(masks_cnt):
			m=Image.blend(bws[i],bws[i+1],self.blend)
			masks.append(m)
		
		return masks
		
	def merge(self,imgs):
		masks=self.get_masks(imgs)
		imx=lambda i:Image.composite(imgs[i],imgs[i+1],masks[i])
		
		return [imx(i) for i in range(len(masks))]
		
	def merge_all(self,imgs):
		
		while len(imgs)>1:
			print("Curr %d" % len(imgs))
			imgs=self.merge(imgs)
		
		return imgs[0]
		
HDR(numImg=3)
