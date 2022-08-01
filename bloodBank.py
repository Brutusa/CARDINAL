class BloodBank:
  
  def __init__(self, name, phone, location, patentNumber, plasmaBags, plateletBags, rbBags): #rbBags is number of bags of red blood cells
    self.name = name
    self.phone = phone
    self.location = location
    self.patentNumber = patentNumber
    self.plasmaBags = plasmaBags
    self.plateletBags = plateletBags
    self.rbBags = rbBags
    return None 
    
  
  def updatePlasma(self, amount):
    if amount > 0:
      self.plasmaBags += amount
    elif amount < 0 and self.plasmaBags > abs(amount):
      self.plasmaBags += amount
    else:
      print("Request cannot be processed, maximum you can get is: ", self.plasmaBags)
    return None    
  
  def updatePlatelet(self, amount):
    if amount > 0:
      self.plateletBags += amount
    elif amount < 0 and self.plateletBags > abs(amount):
      self.plateletBags -= amount
    else:
      print("Request cannot be processed, maximum you can get is: ", self.plateletBags)
    return None
  
  def updateRB(self, amount):
    if amount > 0:
      self.rbBags += amount
    elif amount < 0 and self.rbBags > abs(amount):
      self.rbBags -= amount
    else:
      print("Request cannot be processed, maximum you can get is: ", self.rbBags)
    return None   
  
  def addDonor(self, donor):
    self.donors.append(donor)
    return None

  def __str__(self):
    return 'DONATION CENTER: ' + self.name+  ' -- ADDRESS: '+self.location+ ' -- PHONE: ' + str(self.phone)+str(self.patentNumber)+' '+ str(self.plasmaBags)+' '+ str(self.plateletBags)+' '+ str(self.rbBags)
    




  
  
  
  