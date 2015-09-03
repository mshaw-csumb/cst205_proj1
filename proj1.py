import os.path
path = "C:\Users\Markus\School\CST 205\projects\proj1\cst205_proj1\Project1Images"

numfiles = len([f for f in os.listdir(path)
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
print(pics)


  
