import sys
import os
from PIL import Image
import glob
import wand.image

# pillow library used
# wand (imagicMagick) library used

# *** TIFF Image LZW compression Converter ***
# Tool convert the No Compression (raw) image to LZW compression image
# Tool should check the images, it is present in "No Compression" and then convert to LZW compression

print("\n TIF Image: LZW Compression converter \n")

filepath = input("Enter the Input Image file path: ")
output_directory = "LZW"
output = filepath + "/" + output_directory + "/"

if os.path.exists(output):
    pass
else:
    os.mkdir(output)

for fname in glob.glob(filepath + "/" + "*.tif"):
	input_image = fname
	name1 = os.path.basename(fname)
	print(name1)
	image1 = Image.open(input_image)
	comp_img = str(image1.info['compression'])
	text_file = filepath + "/" + "output.log"
	if comp_img == "raw":
		with wand.image.Image(filename = input_image) as img:
			img.compression = "lzw"
			img.save(filename=output + name1)
	elif comp_img == "tiff_lzw":
		f = open(text_file, "a+")
		f.write(name1 + ": Image already in LZW Compression\n")
		f.close()
	else:
		f = open(text_file, "a+")
		f.write(name1 + ": Image not in No Compression\n")
		f.close()
