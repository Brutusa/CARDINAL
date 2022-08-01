from bloodBank import BloodBank

class Donor:
  MAX_WEEKLY = 2 
  def __init__(self, name, phone, bloodType):
    self.name = name
    self.phone = phone
    self.bloodType = bloodType
    self.nDonations = 0
    return None 
  
  def donate(self, bloodBank, donatedResource, amount):

    if self.nDonations < 2:
      self.nDonations += 1
      if donatedResource.lower() == "plasma":
        bloodBank.updatePlasma(amount)
      elif donatedResource.lower() == "platelets":
        bloodBank.updatePlatelet(amount)
      elif donatedResource.lower() == "blood":
        bloodBank.updateRB(amount)
      bloodBank.addDonor(self)
    
    else:
      print('Donor not allowed to donate more than twice a week.')
    return None  

  def __str__(self):
    return 'NAME: ' + self.name + ' PHONE: ' + str(self.phone) + ' BLOOD TYPE: '+ self.bloodType + ' DONATIONS: ' + str(self.nDonations)
    
