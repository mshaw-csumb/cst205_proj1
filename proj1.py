
#Markus Shaw

#must use getPixel(Picture,xpos,ypos) method, will help much
#for each point on the picture, take the 9 pixels from each picture, sort them, then take the median
#the pixels of the guy will always be an outlier, and then the median of those 9 pixels will be the accurate
#pixel to put into the new picture so that the guy is erased from the frame
import os
from javax.swing import JButton, JFrame
#import os.path

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
  blueVals = []
  grnVals = []
  
  for i in data:
    redVals.append(getRed(i))
    blueVals.append(getBlue(i))
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


def main():
  print("It seems that you want to filter some pictures")
  print("Choose an option: ")
  print("1. Median Filter")
  print("2. Average Filter (less quality)")
  
  choice = input("What do you choose?: ")
  
  if(choice == 1):
    print("Here we go!")
    median()
  else:
    print("Here we go! But it probably won't look as nice as Median...")
    average()
#median function

#average rgb values
def avgRGB(data):
  redVals = []
  blueVals = []
  grnVals = []
  
  redSum = 0
  blueSum = 0
  grnSum = 0
  
  for i in data:
    redVals.append(getRed(i))
    blueVals.append(getBlue(i))
    grnVals.append(getGreen(i))
  for k in range(0,9):
    redSum = redSum + redVals[k]
    blueSum = blueSum + blueVals[k]
    grnSum = grnSum + grnVals[k]
  redSum = redSum / 9
  blueSum = blueSum / 9
  grnSum = grnSum / 9
  
  avgPixel = []
  avgPixel.append(redSum)
  avgPixel.append(grnSum)
  avgPixel.append(blueSum)
  return avgPixel
  

#average function
def average():
  path = pickAFolder()
  image_paths = os.listdir(path)
  pics = []
  for limit in range(0,9):
    pic = makePicture(path + "\\" + image_paths[limit])
    pics.append(pic)
  pixels = []

  for i in range(0,9):
    pixels.append(pics[i].getPixels())
  height = pics[0].getHeight()
  width = pics[0].getWidth()
   #create new blank picture
  finalPic = makeEmptyPicture(width,height,black)
  data = []

  for x in range(0,width):
    for y in range(0,height):
      data = getNinePixels(pics,x,y,data)
      #print(data)
      #bubbleSort(data) #sort
      avgPixel = avgRGB(data)
      #medianPixel = median(data)#put median pixel into new pixel
      setRed(getPixel(finalPic,x,y),avgPixel[0])
      setGreen(getPixel(finalPic,x,y),avgPixel[1])
      setBlue(getPixel(finalPic,x,y),avgPixel[2])
      #repaint(finalPic)

  explore(finalPic)
  path = pickAFolder()
  writePictureTo(finalPic , path + "finalpic_avg.jpg")
  print("Check out the picture, it should be in this directory: ",path)

def median():
  path = pickAFolder()
  image_paths = os.listdir(path)

  #print(image_paths)

  mypicture = image_paths[0]

  pic = makePicture(path + "\\" + image_paths[0])

  #show(pic)
  pics = []
  #limit = 0
  
  for limit in range(0,9):
    pic = makePicture(path + "\\" + image_paths[limit])
    pics.append(pic)
  
 
  #i = 0
  pixels = []

  for i in range(0,9):
    pixels.append(pics[i].getPixels())

  height = pics[0].getHeight()
  width = pics[0].getWidth()
 
  #create new blank picture
  finalPic = makeEmptyPicture(width,height,black)

  #loop pseudo code
  #take all 9 pixels at picture at particular x,y
  #sort
  #take the pixel at median index
  #set pixel at x,y on new blank picture to rgb values of median pixel

  data = []

  for x in range(0,width):
    for y in range(0,height):
      data = getNinePixels(pics,x,y,data)
      #print(data)
      bubbleSort(data) #sort
      accuratePixel = sortRGB(data)
      #medianPixel = median(data)#put median pixel into new pixel
      setRed(getPixel(finalPic,x,y),accuratePixel[0])
      setGreen(getPixel(finalPic,x,y),accuratePixel[1])
      setBlue(getPixel(finalPic,x,y),accuratePixel[2])
      #repaint(finalPic)

  explore(finalPic)
  path = pickAFolder()
  writePictureTo(finalPic , path + "finalpic_median.jpg")
  print("Check out the picture, it should be in this directory: ",path)
  #while (x < width):  
   # while(y < height):
  #    data = getNinePixels(pics,x,y,data) 
  #    #print(data)
  #    bubbleSort(data) #sort
  #    accuratePixel = sortRGB(data)
  #medianPixel = median(data)#put median pixel into new pixel
  #    setRed(getPixel(finalPic,x,y),accuratePixel[0])
  #    setGreen(getPixel(finalPic,x,y),accuratePixel[1])
  #    setBlue(getPixel(finalPic,x,y),accuratePixel[2])
  #repaint(finalPic)
  #    y = y + 1
  #    if(counter >= 8):
  #        counter = 0
  #  x = x + 1
  #  y = 0
    #data = []

main()




