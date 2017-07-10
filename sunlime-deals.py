#! python 2
# _*_ coding: latin-1 _*_
# sunlime-deals.py - manage deals via api

from pyrise import *

# Set highrise variables
deal = Deal()
dealResponsible = 0
dealInitialAction = 0
dealAction = 0
# 0 = add
# 1 = update
# 2 = delete

# Set general variables
dealResponsible = 0
dealId = 0
dealUpdate = 0
sunlimeId = 0
running = True

# Set user IDs
responsiblePartyId = 0
christophId = 1296386
dominikId = 1296544
nicoleId = 1296387

# What do you wnat to do with your deal? function
# Set deal action
def dealActionSet(dealAction):
  dealId = 0
  deal = Deal()
  ##################
  # Add deal
  ##################
  if dealAction == 0:

    print('You are now adding a new deal.')
    print('Next, set the deal number: e.g 105340')
    dealNumber = raw_input()

    print('Next, give the deal a name: e.g. A good, descriptive Name')

    # Set deal name
    dealName = raw_input()
    #type(dealName)
    #dealName = dealName.encode('ascii', 'replace')
    #dealName = dealName.decode('ascii', 'ignore') // strips out the umlaute
    #dealName = u' '.join((dealName)).encode('utf-8')
    #return dealName.encode('utf-8')
    deal.name = ('Angebot-{}: {}').format(dealNumber, dealName)

    print ('Thank you! The id of the deal is: Angebot-{}: The name of the deal is: {}').format(dealNumber, dealName)

    print('Who is responsible for the deal')
    print('Enter \"1\" for Nicole Pfeiffer')
    print('Enter \"2\" for Dominik Fuchshofer')
    print('Enter \"3\" for Christoph Potzinger')

    # Set responsible person
    responsiblePartyId = dealResponsibleSet(dealResponsible)
    print ('The ID is {}').format(responsiblePartyId)
    deal.responsible_party_id = responsiblePartyId

    # Deal background / description
    print('Give us some background for the deal')
    dealBackground = raw_input()
    deal.background = dealBackground

    # Deal currency
    print('Set the deal currency')
    dealCurrency = raw_input()
    deal.currency = dealCurrency

    # Deal price
    print('What is the net worth of the deal in EUR')
    dealPrice = raw_input()
    deal.price = int(dealPrice)

    deal.save()

  ##################
  # Update deal
  ##################
  elif dealAction == 1:
    deal = 0
    dealId = 0
    dealId = input('Enter the deal ID, please : ')
    # print (dealId)
    deal = Deal.get(dealId)
    print ('You have chosen deal \"{}\" with ID {} ').format(deal.name, dealId)
    print ('')

    dealUpdateAction = dealUpdateSet(dealUpdate)
    if dealUpdateAction in range(1, 4):
      if dealUpdateAction == 1:
        print('Entering Deal update mode ...')
        print('The current deal name is: {}').format(deal.name)
        dealUpdateName = raw_input('Now, enter the new **name** for the deal : ')
        deal.name = dealUpdateName
        print('Updating deal name ...')
        deal.save()
        print ('The new **name** for the deal is now set to : {}').format(dealUpdateName)
        print ('Exiting Deal update mode ...')


  ##################
  # Delete deal
  ##################
  elif dealAction == 2:
    while True:
      dealId = input('Enter the deal ID, please : ')
      deal = Deal.get(dealId)
      dealName = deal.name
      print ('You are deleting deal \'{}\' with ID {} ').format(dealName, dealId)
      #print ('Do you really want to delete deal %s? Press \'y\' to confirm deletion : ') % dealName
      dealDeleteConfirmation = raw_input('Do you really want to delete the deal? Press \'y\' to confirm deletion. Press any other key to continue : ')
      if dealDeleteConfirmation == 'y':
        print ('Deleting deal ')
        deal.delete()
        print('The deal \'{}\' with the ID {} has been deleted.').format(dealName, dealId)
        print ('Exiting Deal delete mode ...')
        break
      else:
        print('Let\'s start again...')


    # Continue with more actions
    # Doesn't work yet

  elif dealAction == 3:
    print ({dealAction})

  else:
    print('You haven\'t entered a correct number')
    print('Enter 0 for adding a deal.')
    print('Enter 1 for updating a deal.')
    print('Enter 2 for deleting a deal.')
    print('Blank for quit.')
    dealAction = input()

# Who is responsible? function
# Set responsible person
def dealResponsibleSet(dealResponsible):

  # Who is responsible?
  dealResponsible = input()

  if dealResponsible in range(1, 4):
    if dealResponsible == 1:
      print ('You have entered {} and set Nicole as responsible for the deal').format(dealResponsible)
      responsiblePartyId = nicoleId
      return responsiblePartyId
      print ('The highrise ID of Nicole is {}').format(responsiblePartyId)

    elif dealResponsible == 2:
      print ('You have entered {} and set Dominik as responsible for the deal').format(dealResponsible)
      responsiblePartyId = dominikId
      return responsiblePartyId
      print ('The highrise ID of Dominik is {}').format(responsiblePartyId)

    elif dealResponsible == 3:
      print ('You have entered {} and set Christoph as responsible for the deal').format(dealResponsible)
      responsiblePartyId = christophId
      print ('The highrise ID of Christoph is {}').format(responsiblePartyId)
      return responsiblePartyId

  else:
    print ('Your selection cannot be assigned to one of the administrators. Please choose 1, 2 or 3')
    dealResponsibleSet(dealResponsible)

# What update action do you want to perform? function
# Deal update action

def dealUpdateSet(dealUpdate):
  print ('What do you want to update?')
  # Update deal name
  print ('Enter \"1\" to update the **deal name**')
  # Add note to deal
  print ('Enter \"2\" to add a **note** to the deal')
  # Change the status
  print ('Enter \"3\" to change the **status** of the deal')

  dealUpdate = input()
  return dealUpdate

# What is the deal category? function
# Set deal category

def dealCategorySet(dealCategory):
  print ('Now, please, set the category of the deal')
  print ('Enter 1 for: WP Website')
  print ('Enter 2 for: WP Website mit Hartinger Consulting')
  print ('Enter 3 for: WP Website mit Fertigtemplate')
  print ('Enter 4 for: WP Erweiterung')
  print ('Enter 5 for: Custom WP Extension')
  print ('Enter 6 for: Webhosting')
  print ('Enter 7 for: Wartungsvertrag')
  print ('Enter 8 for: Shopware Webshop')
  print ('Enter 9 for: PHP Programmierung')
  print ('Enter 10 for: Magento Anpassung')


#import connectToHighrise
#connectToHighrise.connectToHighrise


##################
# Connect to Highrise
##################

Highrise.set_server('sunlime')
Highrise.auth('4572ff2d6932dabc5e4a9e905b60ae45')


# Import function dealInitialSet from file dealInitialActionSet.py
from dealInitialActionSet import dealInitialActionSet
print dealInitialActionSet

#dealInitialActionSet()
while running:
  initialValue = dealInitialActionSet()
  dealAction = dealActionSet(initialValue)
  quit = raw_input('Quit program? \'q\' for quit, \'c\' for continue : ')
  if quit == 'q':
    print ('Thank you for using my script! Have a good day!')
    print ('copyright Sunlime Web Innovations GmbH, 2017')
    break
  else:
    print ('Let\'s continue')
else:
  print ('copyright Sunlime Web Innovations GmbH, 2017')
