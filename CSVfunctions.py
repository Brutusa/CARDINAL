import csv



#Prints established donation center public data
def locationCSV():
    with open('./publicDatabase/dcOUT.csv') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      line_count = 0
      for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            print(f'\tDONATION CENTER: {row[0]} -- ADDRESS: {row[1]} -- PHONE: {row[2]}')

            line_count += 1
    print(f'Found {line_count} centers.')
    return None

#Records donor donations
def donorDonCSV(donorName, bankNum, donType, amount):
  with open('./privateDatabase/donorDonationRecords.csv', 'a', newline='') as csvfile:
    record_writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    header = ['NAME', 'RECEIVING CENTER', 'TYPE DONATED', 'UNITS DONATED']
    record_writer.writerow(header)
    record_writer.writerow([donorName, bankNum, donType, amount])
  return None

  #Records donation center transactions
def centerTransCSV(receivingCenter, dispatchingCenter, typeSent, units):
  with open('./privateDatabase/centerTransferRecords.csv', 'a', newline='') as csvfile:
    record_writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    header = ['RECEIVING CENTER #', 'DISPATCHING CENTER #', 'UNIT TYPE', 'UNITS TRANSFERRED']
    record_writer.writerow(header)
    record_writer.writerow([receivingCenter, dispatchingCenter, typeSent, units])
  return None

#Records new registered donors
def registeredCSV(donorName, phone, bloodType):
  with open('./privateDatabase/registeredDonorsRecords.csv', 'a', newline='') as csvfile:
    register_writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    header = ['NAME', 'PHONE', 'BLOOD TYPE']
    register_writer.writerow(header)
    register_writer.writerow([donorName, phone, bloodType])
  return None

#Records new donation centers
def newCenterCSV(title, phone, location, patentNum, currPlasma, currPlatelets, currRB):
  with open('./privateDatabase/newDonCenter.csv', 'a', newline='') as csvfile:
    register_writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    header = ['NAME', 'PHONE', 'LOCATION', 'PATENT NUMBER', 'PLASMA AVAILABLE', 'PLATELETS AVAILABLE', 'BLOOD AVAILABLE']
    register_writer.writerow(header)
    register_writer.writerow([title, phone, location, patentNum, currPlasma, currPlatelets, currRB])
  return None
