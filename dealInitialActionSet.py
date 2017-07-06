# What do you want to do? funtion
# Set the deal action
def dealInitialActionSet():
  print ('What do you want to do with your deal?')
  print ('Enter 0 for adding a deal.')
  print ('Enter 1 for updating a deal.')
  print ('Enter 2 for deleting a deal.')
  print ('Blank for quit.')

  dealAction = input()
  return dealAction