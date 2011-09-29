import Image
import os
import ImageEnhance
import sys
import getopt

class HDR:
	
	def __init__(self, folder="",out="out.jpg",blend=0.5,order=False):
		self.blend=blend
		
		if folder and os.path.isdir(folder):
			images=[Image.open("%s/%s" %(folder,fname)) for fname in sorted(os.listdir(folder),key=None,reverse=False)]
			images=self.sort(images,order)
			new=self.merge_all(images)
			new.save(out)
		else:
			print("Please specify a valid folder")
	

	def sort(self,imgs,order=False):
		val=[sum(img.convert(mode="L").getdata())/(1.0*img.size[0]*img.size[1]) for img in imgs]
		tosort=sorted(zip(val,imgs),reverse=order)
		val, imgs=zip(*tosort)
		
		return imgs


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
		
def usage():
	print("%s Version 0.5 (CC) BY-NC-SA 2011 Roberto Torella <rob@ganglio.eu>" % sys.argv[0])
	print("Usage %s [options]" % sys.argv[0])
	print("Creates a High Dynamic Range image from a list of files contained in a folder.")
	print
	print("Options:")
	print(" --help, -h              Shows this help.")
	print(" --folder, -f <string>   Select the folder from which load the images.")
	print(" --output, -o <string>   The output file.")
		
def main(argv):
	try:
		opts, args = getopt.getopt(argv,"hf:o:",["help","folder","output"])
		if len(opts)==0:
			usage()
			sys.exit(2)
			
		
	except getopt.GetoptError:
		usage()
		sys.exit(2)
	
if __name__ == "__main__":
	main(sys.argv[1:])
