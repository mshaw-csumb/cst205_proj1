#must use getPixel(Picture,xpos,ypos) method, will help much
#for each point on the picture, take the 9 pixels from each picture, sort them, then take the median
#the pixels of the guy will always be an outlier, and then the median of those 9 pixels will be the accurate
#pixel to put into the new picture so that the guy is erased from the frame
import os
#import os.path
path = pickAFolder()

#numfiles = len([f for f in os.listdir(path)#find reference link from stack overflow
               # if os.path.isfile(os.path.join(path,f))])
#print(numfiles)

image_paths = os.listdir(path)

print(image_paths)

mypicture = image_paths[0]

pic = makePicture(path + "\\" + image_paths[0])

#show(pic)
pics = []
limit = 0
while( limit < 9 ):
  pic = makePicture(path + "\\" + image_paths[limit])
  pics.append(pic)
  #show(pic)
  limit+=1
#print(pics)

#show(pics[1])

i = 0
pixels = []
while(i < 9):
  pixels.append(pics[i].getPixels())
  i = i+1
x = 0
y = 0;
height = pics[0].getHeight()
width = pics[0].getWidth()


while (x < width):  
  while(y < height):
    pixel = getPixel(pics[0],x,y)
    if(pixel.getGreen() > 50):
      setGreen(pixel,0)
    y = y + 1
  x = x + 1
  y = 0
   
   
  
      

      
explore(pics[0])

#print(pixels[1][:4])
#pixels[1][0] = pixels[1][2]
#print(pixels[1][:4])
#repaint(pics[1])

#pixels[1][0:20] = pixels[1][90:110]


