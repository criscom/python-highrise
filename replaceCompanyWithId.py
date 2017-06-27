#! python 3
# match Company and replace with ID

import csv, os

os.makedirs('headerRemoved/replaceNameWithId', exist_ok=True)


print('Replacing company names with IDs  ...')

CompanyIdFile = open('headerRemoved/company-id.csv')
CompanyIdReader = csv.reader(CompanyIdFile)
CompanyIdData = list(CompanyIdReader)

print (CompanyIdData[0][1])
