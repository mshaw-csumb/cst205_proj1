#must use getPixel(Picture,xpos,ypos) method, will help much

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
   
   

while(row < x):
  while (col < y and row < x):
    pixel = getPixel(pics[0],row,col)
    if (pixel.getBlue() < 50):
      setBlue(pixel,0)
    col = col + 1
    
  row = row + 1
  
      
      
      
explore(pics[0])

#print(pixels[1][:4])
#pixels[1][0] = pixels[1][2]
#print(pixels[1][:4])
#repaint(pics[1])

#pixels[1][0:20] = pixels[1][90:110]


