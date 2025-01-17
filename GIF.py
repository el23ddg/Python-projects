import imageio.v3 as iio

filenames = ['dino1.png', 'dino2.png', 'dino3.png', 'dino4.png'] #we'll create a list that contains the locations of the image files
images = [ ] #created an empty list that will be used to store the actual image data from these files

#use a for loop to go through the file paths and read the images using imageio library’s .imread() method
#.imread() method loads an image based on the file path. So now, our images variable has all the images!
for filename in filenames:
  images.append(iio.imread(filename))

#use the .imwrite() method to turn the images into a GIF
iio.imwrite('dinodancer.gif', images, duration = 500, loop = 0)

