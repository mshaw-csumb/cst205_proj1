import os.path
path = pickAFolder()

numfiles = len([f for f in os.listdir(path)#find reference link from stack overflow
                if os.path.isfile(os.path.join(path,f))])
print(numfiles)

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

show(pics[1])

i = 0
pixels = []
while(i < 9):
  pixels.append(pics[i].getPixels())
  i = i+1

#print(pixels[1][:4])
#pixels[1][0] = pixels[1][2]
#print(pixels[1][:4])
#repaint(pics[1])

#pixels[1][0:20] = pixels[1][90:110]

setRed(pixels[1][0],pixels[1][1000].getRed())
setBlue(pixels[1][0],pixels[1][1000].getBlue())
setGreen(pixels[1][0],pixels[1][1000].getGreen())
repaint(pics[1])
explore(pics[1])
print(pixels[1][:4])
