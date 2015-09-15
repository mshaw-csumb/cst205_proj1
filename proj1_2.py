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
counter = 0;

def median(list):
  median = 0
  median = (len(list)/2) + 1
  return list[median]

list = [1,2,3,4,5]

#print(median(list))

def bubbleSort(data):
  # get rgb values
  _ = 0
  
  while(_ < len(data)-1):
    colorTotal = 0
    #print("Getting j pixel data")
    colorTotal = colorTotal + getRed(data[_])
    colorTotal = colorTotal + getGreen(data[_])
    colorTotal = colorTotal + getBlue(data[_])
    
    colorTotal2 = 0
    #print("Getting j+1 pixel data")
    colorTotal2 = colorTotal2 + getRed(data[_+1])
    colorTotal2 = colorTotal2 + getGreen(data[_+1])
    colorTotal2 = colorTotal2 + getBlue(data[_+1])
    
    #print("Swapping")
    if(colorTotal > colorTotal2):
      tempPixel = data[_]
      data[_] = data[_+1]
      data[_+1] = tempPixel
    _ = _ +1

    
    
def getNinePixels(pics):
  counter = 0
  while(counter < 9 ):
      #print("putting 9 pixels into list")
      pixel = getPixel(pics[counter],x,y)
      data.append(pixel)
      counter = counter+1 
return data
    
#create new blank picture
finalPic = makeEmptyPicture(width,height,black)

#loop pseudo code
#take all 9 pixels at picture at particular x,y
#sort
#take the pixel at median index
#set pixel at x,y on new blank picture to rgb values of median pixel

data = []
counter = 0
show(finalPic)
while (x < width):  
  while(y < height):
    
    while(counter < 9 ):
      #print("putting 9 pixels into list")
      pixel = getPixel(pics[counter],x,y)
      data.append(pixel)
      counter = counter+1 
     
    #print(data)
    #print("Sorting")
    bubbleSort(data) #sort
  
    medianPixel = median(data)#put median pixel into new pixel
    #print("Median Pixel: ")
    #print(medianPixel)
    
    setRed(getPixel(finalPic,x,y),getRed(medianPixel))
    setGreen(getPixel(finalPic,x,y),getGreen(medianPixel))
    setBlue(getPixel(finalPic,x,y),getBlue(medianPixel))
    repaint(finalPic)
    
    y = y + 1
    
    if(counter >= 8):
        counter = 0
  x = x + 1
  y = 0
  data = []
  
 
  

#while(row < x):
 # while (col < y and row < x):
  #  pixel = getPixel(pics[0],row,col)
   # if (pixel.getBlue() < 50):
    #  setBlue(pixel,0)
    #col = col + 1
    
  #row = row + 1
  
      
#explore(pics[0])

#print(pixels[1][:4])
#pixels[1][0] = pixels[1][2]
#print(pixels[1][:4])
#repaint(pics[1])

#pixels[1][0:20] = pixels[1][90:110]


