import sys
sys.path.insert(1, './privateDatabase')
import pandas as pd
from donor import Donor
from bloodBank import BloodBank
from CSVfunctions import *
from privateDatabase import *

#This is the list of menu items/ functions


#Blood transaction function
def bloodTransaction():
  answer = (input("Is the transaction between centers?(Y/N) ").lower())
  if answer == 'y':
    receivingCenter = int(input("Please enter the receiving center's patent number? "))
    dispatchingCenter = int(input("Please enter the sending center's patent number? "))
    amount = int(input("How many units of blood are requested? "))
    for bank in bloodBankList:
      if bank.patentNumber == bank1:
        for bank_ in bloodBankList:
          if bank_.patentNumber == bank2:
            bank.updateRB(amount)
            bank_.updateRB(-amount)
            break
        break
    centerTransCSV(receivingCenter, dispatchingCenter, 'Blood', amount)     
  else:
    print("It is assumed that the transaction is between a donor and center. ")
    donorName = (input("What is the donor's name? "))
    bankNum = int(input("Please enter the receiving center's patent number? "))
    amount = int(input("How many units of blood are donated? "))
    for bank in bloodBankList:
      if bank.patentNumber == bankNum:
          bank.updateRB(amount)            
          break
    #donor1.donate(bank1, 'blood', amount)
    #donors.append(donor1)
    donorDonCSV(donorName, bankNum, 'Blood', amount)
    
  return None

#Plasma transaction function
def plasmaTransaction():
  answer = (input("Is the transaction between centers?(Y/N) ").lower())
  if answer == 'y':
    receivingCenter = int(input("Please enter the receiving center's patent number? "))
    dispatchingCenter = int(input("Please enter the sending center's patent number? "))
    amount = int(input("How many units of plasma are requested? "))
    for bank in bloodBankList:
      if bank.patentNumber == bank1:
        for bank_ in bloodBankList:
          if bank_.patentNumber == bank2:
            bank.updatePlasma(amount)
            bank_.updatePlasma(-amount)
            break
        break
    centerTransCSV(receivingCenter, dispatchingCenter, 'Plasma', amount)
  else:
    print("It is assumed that the transaction is between a donor and a center. ")
    donorName = (input("What is the donor's name? "))
    bankNum = int(input("Please enter the receiving blood bank patent number? "))
    amount = int(input("How many units of plasma are donated? "))
    #donors.append(donor1)
    #donor1.donate(bank1, 'plasma', amount)
    for bank in bloodBankList:
      if bank.patentNumber == bankNum:
          bank.updatePlasma(amount)            
          break
        
    donorDonCSV(donorName, bankNum, 'Plasma', amount)
  return None

#Platelets transaction function
def plateletTransaction():
  answer = (input("Is the transaction between centers?(Y/N) ").lower())
  if answer == 'y':
    receivingCenter = int(input("Please enter the receiving center's patent number? "))
    dispatchingCenter = int(input("Please enter the sending center's patent number? "))
    amount = int(input("How many units of platelets are requested? "))
    for bank in bloodBankList:
      if bank.patentNumber == bank1:
        for bank_ in bloodBankList:
          if bank_.patentNumber == bank2:
            bank.updatePlatelet(amount)
            bank_.updatePlatelet(-amount)
            break
        break
    centerTransCSV(receivingCenter, dispatchingCenter, 'Platelets', amount)    
  else:
    print("It is assumed that the transaction is between a donor and a center. ")
    donorName = (input("What is the donor's name? "))
    bankNum = int(input("Please enter the receiving center's patent number? "))
    amount = int(input("How many units of platelets are donated? "))
    for bank in bloodBankList:
      if bank.patentNumber == bankNum:
          bank.updatePlatelet(amount)            
          break
    #donor1.donate(bank1, 'platelets', amount)
    #donors.append(donor1)
    donorDonCSV(donorName, bankNum, 'Platelets', amount)
  return None

  #Register new donor
def newDonor():
    name = input("What's the new donor's name? ")
    phone = input("What is the phone number? ")
    bType = input("What is the donor's blood type? ")
    donors.append(Donor(name, phone, bType))
    registeredCSV(name, phone, bType)
    print("Donor registered successfully.")
    
    return None

#Register new center
def newCenter():
  title = input("What's the center's name? ")
  phone = input("What is the phone number? ")
  location = input("Where is the center located? ")
  patentNumber = int(input("What is the patent number? "))
  currPlasma = int(input("How many units of plasma are available? "))
  currPlatelets = int(input("How many units of platelets are available? "))
  currRB = int(input("How many units of blood are available? "))
  bloodBankList.append(BloodBank(title, phone, location, patentNumber, currPlasma, currPlatelets, currRB))
  newCenterCSV(title, phone, location, patentNumber, currPlasma, currPlatelets, currRB )

  print("Center added successfully.")
  return None

#Print list of new centers
def printNewCenterList():
  if not bloodBankList:
    print("no newly registered centers")
  else:
    for x in range(len(bloodBankList)):  
      print(bloodBankList[x])
    return None

#Print list of new donors
def printNewDonorList():
  if not donors:
    print("no newly registered donors")
  else:
    for x in range(len(donors)):
      print(donors[x])
    return None

#Center Prioritization
def priorityCenter():
  fileRead = pd.read_csv('./publicDatabase/dcOUT.csv')
  priorityBlood = fileRead['Blood Units'].min()
  priorityPlasma = fileRead['Plasma Units'].min()
  priorityPlatelets = fileRead['Platelet Units'].min()
  print('donation center with lowest Blood inventory has ' + str(priorityBlood) + ' units of Blood remaining')
  print('donation center with lowest Plasma inventory has ' + str(priorityPlasma) + ' units of Plasma remaining')
  print('donation center with lowest Platelet inventory has ' + str(priorityPlatelets) + ' units of Platelets remaining')
  return None
