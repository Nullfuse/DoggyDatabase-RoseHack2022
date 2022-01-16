import os.path

DOG_INFO_TYPES = 4

#Stores Dog Name, Age, Gender, Breed
#infoList will be a list of strings corresponding to
#a Dog's Name, Age, Gender, and Breed
class Dog:
  def __init__(self, infoList):
    self.name = infoList[0]
    self.age = infoList[1]
    self.gender = infoList[2]
    self.breed = infoList[3]

  def to_string(self):
    return self.name + "|" + self.age + "|" + self.gender + "|" + self.breed

def readList(doglist):
  if not os.path.isfile('doglist.txt'):
    f = open('doglist.txt', 'x')
  # Open file containing all saved dog information
  with open('doglist.txt', 'r') as f:
    lines = f.readlines()
  f.close()

  # Insert saved dogs into list
  lineCount = 0
  for line in lines:
    ++lineCount
    line = line.split('|')
    # Check for DOG_INFO_TYPES number of delimited arguments
    if len(line) != DOG_INFO_TYPES + 1:
      print("Incorrect number of arguments on line " + str(lineCount))
    # Add new Dog to doglist with specified information
    else:
      newDog = Dog(line)
      doglist.append(newDog)

# Saving items in the list to file
def saveList(doglist):
  with open('doglist.txt', 'w+') as f:
    if len(doglist) > 0:
      for dog in doglist:
          f.write(dog.to_string() + "|\n")
    else:
      f.write("")
    f.close()

def addDog(doglist, dogInfo):
  newDog = Dog(dogInfo)
  doglist.append(newDog)
  saveList(doglist)

def deleteDog(doglist, dogInfo):
  removalDog = Dog(dogInfo)
  found = False
  for ListDog in doglist:
    if ListDog.to_string() == removalDog.to_string():
      found = True
      doglist.remove(ListDog)
      saveList(doglist)
      break; # break to avoid removing more than one that may have the same data
  if found == False:
    print("No dog found matching entered data.")

def dog_gender(val):
  switcher = {
    0: "Undetermined",
    1: "Male",
    2: "Female"
  }
  return switcher.get(val)