from marvel import Marvel 
from skimage import io
m = Marvel(PUBLIC_KEY="YOUR_PUBLIC_KEY", PRIVATE_KEY="YOUR_PRIVATE_KEY")

def searchByName():
  characters=m.characters
  i=1
  char_name=input("Enter the name of the Marvel Character:\t")
  all_characters=characters.all(name=char_name)["data"]["results"][0]
  id=all_characters["id"]
  n=all_characters["name"]
  description=all_characters["description"]
  thumbnail=all_characters["thumbnail"]["path"]+"/"+"portrait_fantastic.jpg"

  img = io.imread(thumbnail)
  io.imshow(img)

  print("ID =",id)
  print("Name=",n)
  print("Description=",description)
  print()
  print("Comic Appearances: ")
  print()

  for char in all_characters["comics"]["items"]:
    print(i,".",char["name"])
    i+=1

  i=1
  print()
  print("Series Appearances: ")
  print()

  for char in all_characters["series"]["items"]:
    print(i,".",char["name"])
    i+=1


def searchByStarting():
  characters=m.characters
  i=1
  char_name=input("Enter the name of the Marvel Character:\t")
  all_characters=characters.all(nameStartsWith=char_name)["data"]["results"]

  for char in all_characters:
    print(char["id"], char["name"])
    print()
    for comics in char["comics"]["items"]:
      print(comics["name"])
    print("==========================")

print("1. Search by Name")
print("2. Search for a character whose name starts with")
print()
choice=int(input("Enter your Choice:\t"))

if(choice==1):
  searchByName()
elif(choice==2):
  searchByStarting()
else:
  print("You have entered the wrong choice")
