#must use getPixel(Picture,xpos,ypos) method, will help much
#for each point on the picture, take the 9 pixels from each picture, sort them, then take the median
#the pixels of the guy will always be an outlier, and then the median of those 9 pixels will be the accurate
#pixel to put into the new picture so that the guy is erased from the frame
import os
from javax.swing import JButton, JFrame
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

def colorSort(data):
  temp = 0
  for k in range(0,len(data)-1):
    for j in range(0,len(data)-1):
      if(data[j] > data[j+1]):
        temp = data[j]
        data[j] = data[j+1]
        data[j+1] = temp

def medianIndex(list):
  median = 0
  median = (len(list)/2)+1
  return median

def sortRGB(data):
  #get red values for pixel data
  redVals = []
  for i in data:
    redVals.append(getRed(i))
  #get blue values for pixel data
  blueVals = []
  for i in data:
    blueVals.append(getBlue(i))
  #get green values for pixel data
  grnVals = []
  for i in data:
    grnVals.append(getGreen(i))
  
  #sort each of them
  colorSort(redVals)
  colorSort(blueVals)
  colorSort(grnVals)
  #put them in separate lists
  #take median of each
  redIndex = medianIndex(redVals)
  blueIndex = medianIndex(blueVals)
  grnIndex = medianIndex(grnVals)
  
  accuratePixel =[redVals[redIndex],grnVals[grnIndex],blueVals[blueIndex]]
  #return list of rgb
  return accuratePixel
  #put that rgb value into finalPic
  

  
def getNinePixels(pics,x,y,data):
  counter = 0
  data = []
  while(counter < 9 ):
     
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

while (x < width):  
  while(y < height):
    
    
    data = getNinePixels(pics,x,y,data) 
    
    #print(data)
    
    bubbleSort(data) #sort
    accuratePixel = sortRGB(data)
    #medianPixel = median(data)#put median pixel into new pixel
    
    
    setRed(getPixel(finalPic,x,y),accuratePixel[0])
    setGreen(getPixel(finalPic,x,y),accuratePixel[1])
    setBlue(getPixel(finalPic,x,y),accuratePixel[2])
    #repaint(finalPic)
    
    y = y + 1
    
    if(counter >= 8):
        counter = 0
  x = x + 1
  y = 0
  #data = []

explore(finalPic)
writePictureTo(finalPic,"C:\\Users\\Markus\\School\\CST 205\\projects\\proj1\\cst205_proj1\\finalpic\\finalpic.jpg")




