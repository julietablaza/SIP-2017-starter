from PIL import Image

# RGB values for recoloring.
color_scheme_input = input("What color sheme would you like? (classic, ocean, funky, or grayscale) ")

if color_scheme_input == "classic":
    color1 = (0, 51, 76) # dark blue
    color2 = (217, 26, 33) # red
    color3 = (112, 150, 158) # light blue
    color4 = (252, 227, 166) # yellow
elif color_scheme_input == "ocean":
    color1 = (59, 85, 147) # dark blue
    color2 = (42, 184, 145) # green
    color3 = (117, 203, 234) # light blue
    color4 = (254, 255, 206) # pale yellow
elif color_scheme_input == "grayscale":
    color1 = (40, 40, 40) # dark gray
    color2 = (107, 107, 107)
    color3 = (160, 160, 160)
    color4 = (224, 224, 224) # light gray
elif color_scheme_input == "funky":
    color1 = (93, 0, 160) # purple
    color2 = (69, 173, 211) # blue
    color3 = (255, 242, 73) # yellow
    color4 = (255, 168, 231) # pink
else:
    print("Valid color scheme not entered. (Default color scheme: classic)")
    color1 = (0, 51, 76) # dark blue
    color2 = (217, 26, 33) # red
    color3 = (112, 150, 158) # light blue
    color4 = (252, 227, 166) # yellow

# Import image.
image_input = input("What is the image name? It should be in the same folder as this .py file. (Ex. my_dog.jpg) ")
my_image = Image.open(str(image_input)) #change IMAGENAME to the path on your computer to the image you're using
image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.

recolored = [] #list that will hold the pixel data for the new image.

#YOUR CODE to loop through the original list of pixels and build a new list based on intensity should go here.
for pixel in image_list:
    if sum(pixel) < 182:
        recolored.append(color1)
    elif sum(pixel) < 364:
        recolored.append(color2)
    elif sum(pixel) < 546:
        recolored.append(color3)
    else:
        recolored.append(color4)


# Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", my_image.size) #Creates a new image that will be the same size as the original image.
new_image.putdata(recolored) #Adds the data from the recolored list to the image.
new_image.show() #show the new image on the screen
new_image.save("recolored_" + str(color_scheme_input) + "_" + str(image_input), "jpeg") #save the new image as "recolored.jpg"
