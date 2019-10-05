
#import skimage.io
from PIL import Image
import os
IMAGE_DIR="D:\\Tiffany\\retina-unet-master-breast\\dataset\\test\\images"
# Load a random image from the images folder

file_names = next(os.walk(IMAGE_DIR))[2]

quantity=(len([name for name in os.listdir(IMAGE_DIR) if os.path.isfile(os.path.join(IMAGE_DIR, name))]))
print(quantity)



for i in range(0, quantity):
    
    #image = skimage.io.imread(os.path.join(IMAGE_DIR, file_names[i]))
	im = Image.open(os.path.join(IMAGE_DIR, file_names[i]))
	#im = image.open( "sample01.jpg" )
	print(im.size)
    #width = 227
	#height = 227
	nim = im.resize( (227, 227), Image.BILINEAR )

	
	path_save="C:\\Users\\win\\Desktop\\test_images_resize"
	name = str(i+1) + "_manual1" + ".png"
	nim.save(os.path.join(path_save,name))
	
	print("resize後:")
	print(nim.size)
	print("------------------------------")
	#nim.save( "resized.jpg" )
