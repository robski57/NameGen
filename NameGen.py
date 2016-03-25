import unittest
import cap
from random import choice
def makename():

    
    firstN = ["Robert","James","Danny","Billy","John","Eddie","David","Luke","Joshua","Mannie","Edward"]
    lastN = ["Carter","Anderson","Williams","Brown","Smith","Washington","Jones","Baker","Williamson","Turner","Johnson"]
    name=(choice(firstN)+choice(lastN))
    decision = input("would you like me to generate a text name Y/N?")
    if decision =="Y"or"Yes"or"y":
        writing = open("generator name.text","w")
        writing.write(name)
    else:
        print("thank you")
    print("We are going to make you a new name")
    print("your new name is:  ")
    print( name)
  
                  
makename()
print("Press enter to close program")

if __name__=='__main__':
    unittest.main()
