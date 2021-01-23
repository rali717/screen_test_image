#import Image
from PIL import Image

img = Image.new( 'RGB', (1440,900), "black") # create a new black image
pixels = img.load() # create the pixel map

for i in range(img.size[0]):    # for every pixel:
    for j in range(0,img.size[1],2):

		pixels[i,j] = (255, 255, 255) # set the colour accordingly
            
img.save("1440x900_h.bmp")
#img.show()




img = Image.new( 'RGB', (1920,1080), "black") # create a new black image
pixels = img.load() # create the pixel map

for i in range(img.size[0]):    # for every pixel:
    for j in range(0,img.size[1],2):

		pixels[i,j] = (255, 255, 255) # set the colour accordingly
            
img.save("1920x1080_h.bmp")
#img.show()





img = Image.new( 'RGB', (3840,2160), "black") # create a new black image
pixels = img.load() # create the pixel map

for i in range(img.size[0]):    # for every pixel:
    for j in range(0,img.size[1],2):

		pixels[i,j] = (255, 255, 255) # set the colour accordingly
            
img.save("3840x2160_h.bmp")
#img.show()





## Vertical ####################################################################

img = Image.new( 'RGB', (1440,900), "black") # create a new black image
pixels = img.load() # create the pixel map

for i in range(0,img.size[0],2):    # for every pixel:
    for j in range(img.size[1]):

		pixels[i,j] = (255, 255, 255) # set the colour accordingly
            
img.save("1440x900_v.bmp")
#img.show()




img = Image.new( 'RGB', (1920,1080), "black") # create a new black image
pixels = img.load() # create the pixel map

for i in range(0,img.size[0],2):    # for every pixel:
    for j in range(img.size[1]):

		pixels[i,j] = (255, 255, 255) # set the colour accordingly
            
img.save("1920x1080_v.bmp")
#img.show()

################################################################################

#hier
img = Image.new( 'RGB', (1920,1080), "black") # create a new black image
pixels = img.load() # create the pixel map

for i in range(0,img.size[0],2):    # for every pixel:
    for j in range(0,img.size[1],2):

		pixels[i,j] = (255, 255, 255) # set the colour accordingly
            
img.save("1920,1080_sq_black.bmp")
#img.show()



img = Image.new( 'RGB', (1920,1080), "white") # create a new black image
pixels = img.load() # create the pixel map

for i in range(0,img.size[0],2):    # for every pixel:
    for j in range(0,img.size[1],2):

		pixels[i,j] = (0, 0, 0) # set the colour accordingly
            
img.save("1920,1080_sq_white.bmp")
#img.show()

################################################################################

img = Image.new( 'RGB', (3840,2160), "black") # create a new black image
pixels = img.load() # create the pixel map

for i in range(0,img.size[0],2):    # for every pixel:
    for j in range(img.size[1]):

		pixels[i,j] = (255, 255, 255) # set the colour accordingly
            
img.save("3840x2160_v.bmp")
#img.show()










################################################################################

img = Image.new( 'RGB', (3840,2160), "black") # create a new black image
pixels = img.load() # create the pixel map

for i in range(0,img.size[0],2):    # for every pixel:
    for j in range(0,img.size[1],2):

		pixels[i,j] = (255, 255, 255) # set the colour accordingly
            
img.save("3840x2160_sq_black.bmp")
#img.show()



img = Image.new( 'RGB', (3840,2160), "white") # create a new black image
pixels = img.load() # create the pixel map

for i in range(0,img.size[0],2):    # for every pixel:
    for j in range(0,img.size[1],2):

		pixels[i,j] = (0, 0, 0) # set the colour accordingly
            
img.save("3840x2160_sq_white.bmp")
#img.show()


################################################################################
################################################################################

img = Image.new( 'RGB', (3840,2160), "red") # create a new black image
pixels = img.load() # create the pixel map

for i in range(0,img.size[0],1):    # for every pixel:
    for j in range(0,img.size[1],1):

		pixels[i,j] = (255, 0, 0) # set the colour accordingly
            
img.save("3840x2160_red.bmp")
#img.show()

################################################################################

img = Image.new( 'RGB', (3840,2160), "red") # create a new black image
pixels = img.load() # create the pixel map

for i in range(0,img.size[0],1):    # for every pixel:
    for j in range(0,img.size[1],1):

		pixels[i,j] = (255, 0, 0) # set the colour accordingly
            
img.save("3840x2160_red.bmp")
#img.show()

################################################################################

img = Image.new( 'RGB', (3840,2160), "green") # create a new black image
pixels = img.load() # create the pixel map

for i in range(0,img.size[0],1):    # for every pixel:
    for j in range(0,img.size[1],1):

		pixels[i,j] = (00, 255, 0) # set the colour accordingly
            
img.save("3840x2160_green.bmp")
#img.show()

################################################################################

img = Image.new( 'RGB', (3840,2160), "blue") # create a new black image
pixels = img.load() # create the pixel map

for i in range(0,img.size[0],1):    # for every pixel:
    for j in range(0,img.size[1],1):

		pixels[i,j] = (0, 0, 255) # set the colour accordingly
            
img.save("3840x2160_blue.bmp")
#img.show()

################################################################################
################################################################################


img = Image.new( 'RGB', (1920,1080), "red") # create a new black image
pixels = img.load() # create the pixel map

for i in range(0,img.size[0],1):    # for every pixel:
    for j in range(0,img.size[1],1):

		pixels[i,j] = (255, 0, 0) # set the colour accordingly
            
img.save("1920,1080_red.bmp")
#img.show()

################################################################################

img = Image.new( 'RGB', (3840,2160), "red") # create a new black image
pixels = img.load() # create the pixel map

for i in range(0,img.size[0],1):    # for every pixel:
    for j in range(0,img.size[1],1):

		pixels[i,j] = (255, 0, 0) # set the colour accordingly
            
img.save("1920,1080_red.bmp")
#img.show()

################################################################################

img = Image.new( 'RGB', (3840,2160), "green") # create a new black image
pixels = img.load() # create the pixel map

for i in range(0,img.size[0],1):    # for every pixel:
    for j in range(0,img.size[1],1):

		pixels[i,j] = (00, 255, 0) # set the colour accordingly
            
img.save("1920,1080_green.bmp")
#img.show()

################################################################################

img = Image.new( 'RGB', (3840,2160), "blue") # create a new black image
pixels = img.load() # create the pixel map

for i in range(0,img.size[0],1):    # for every pixel:
    for j in range(0,img.size[1],1):

		pixels[i,j] = (0, 0, 255) # set the colour accordingly
            
img.save("1920,1080_blue.bmp")
#img.show()


