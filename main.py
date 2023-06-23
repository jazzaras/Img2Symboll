import cv2

# this line reads the image and turns it into a black and white image
img = cv2.imread("imageHere",cv2.IMREAD_GRAYSCALE)

# greyImage = cv2.colorChange(img, cv2.COLOR_BGR2GRAY)

# gitting the hight and width of the p
h, w = img.shape[:2]

# # the symbolls that we are going to use in order... if the back ground was white we should use the next line...
# symbolls = list(reversed([".", "/", "+", "%", "#", "@"]))
# # in cmd we need to use the next line because the background is black... we can make white
symbolls = [" ", "/", "+", "%", "#", "@"]

# resizeing the image... this may look like we are changing the image dimantions.. but when printing.. lines are far from each other so it looks good
resizedImage = cv2.resize(img, (400, int((h * 200)/w)))

# this method loops through every pixle in the image and decide what symboll to print for every pixle
def slow(image):
    img = image.copy()
    height, width = img.shape
    for i in range(0, height):             #looping at python speed...
       for j in range(0, (width)):
           # every pixle has a value from 0 - 255 ... and the next line transelate this to be a value from 0 - 6 ... to use the value as an index
           value = int((img[i,j] / 255.0) * 6)
           try:
               print(symbolls[value], end="")
           except:
               print(symbolls[value-1], end="")
      
       # new line after every row
       print("")
        
         
        
    return img

x = slow(resizedImage)



# writing the image to another output file 
cv2.imwrite("output.jpg", resizedImage)

