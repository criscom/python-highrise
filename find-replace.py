import os
import sys
import fileinput

# Read in the file
with open ('company.txt', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace(',' ';')

# Write the file out again
with open ('company.txt', 'w' as file :
  file.write(filedata))