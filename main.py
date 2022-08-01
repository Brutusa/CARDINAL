from menuItems import *
import pandas as pd
from CSVfunctions import *
from donor import Donor
from bloodBank import BloodBank
from privateDatabase import *

#Software designed by Andujar Brutus and El Arbi
def menu():
  print("\n:::CARDINAL MAIN MENU:::")
  print("1. Register a New Member Donor.")
  print("2. Register a New Donation Center.")
  print("3. Print list of newly registered donors.")
  print("4. Print list of newly registered centers.")
  print("5. Suggest Potential Centers.")
  print("6. Make a Plasma Transaction.")
  print("7. Make a Blood Transaction.")
  print("8. Make a Platelets Transaction. ")
  print("9. Centers in Need ")
  
  return None

while True:
  menu()
  choice = int(input("Choose an option: "))

  if choice == 1:
    newDonor()

  elif choice == 2:
    newCenter()
      
  elif choice == 3:
    printNewDonorList()

  elif choice == 4:
    printNewCenterList() 
    
  elif choice == 5:
    locationCSV()

  elif choice == 6:
    plasmaTransaction()

  elif choice == 7:
    bloodTransaction()

  elif choice == 8:
    plateletTransaction()

  elif choice == 9:
    priorityCenter()
