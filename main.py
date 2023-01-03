print("⚔️ Character Stats Generator ⚔️")
print()

def rollDice():
  import random
  anyNumber = random.random()
  return anyNumber

def rollDice2():
  import random
  sixside = random.randint(1,6)
  eightside = random.randint(1,8)
  together = sixside * eightside
  return together

haveCharacter = "yes"

while haveCharacter  == "yes":
  name = input("Name your warrior: ")
  anyNr = rollDice()
  print("Their health is:", str(anyNr)+"hp")
  print()
  name = input("Name your warrior: ")
  sixNeight = rollDice2()
  print("Their health is:", str(sixNeight)+"hp")
  print()
  haveCharacter = input("Would you like to create a character? ")
  print()