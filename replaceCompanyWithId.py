#! python 3
# match company and replace with ID

import csv, os

os.makedirs('headerRemoved/replaceNameWithId', exist_ok=True)


print('Replacing company names with IDs  ...')

companyRows = []
companyIdFile = open('headerRemoved/company-id.csv')
companyIdReader = csv.reader(companyIdFile)
companyIdData = list(companyIdReader)
print (companyIdData[0])
print (companyIdData[0][0])
print (companyIdData[0][1])
print ("New Stlye: First column is Highrise ID = {} and second column is Company name = {}".format(companyIdData[0][0], companyIdData[0][1]))


# https://stackoverflow.com/questions/4440516/in-python-is-there-an-elegant-way-to-print-a-list-in-a-custom-format-without-ex
#print ('\n' . join('{}: {}' . format(*k) for k in (companyIdData)))

dealRows = []
dealFile = open ('headerRemoved/angebotsbuch.csv')
dealReader = csv.reader(dealFile)
dealData = list(dealReader)
#print (dealData[0])

for company1 in companyIdData:
    for company2 in dealData:
      if company1 == company2:
        print company1