#! python 2
# sunlime-deals.py - manage deals via api

from pyrise import *

# Set highrise variables
deal = Deal()
dealResponsible = 0
dealId = 0
dealInitialAction = 0
dealAction = 0
# 0 = add
# 1 = update
# 2 = delete

# Set general variables
dealResponsible = 0
dealId = 0
dealAction = 0
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
    dealId = raw_input('Enter the deal ID, please : ')
    deal = Deal.get(dealId)
    print ('You have chosen deal \"{}\" with ID {} ').format(deal.name, dealId)
    print ('')
    print ('What do you want to do?')
    # Update deal name
    print ('Enter \"1\" to update the deal name')

    # Add note to deal
    print ('Enter \"2\" to add a note to the deal')

    #
    print ('Enter \"3\" to change the status of the deal')

  ##################
  # Delete deal
  ##################
  elif dealAction == 2:
    dealId = raw_input('Enter the deal ID, please : ')
    deal = Deal.get(dealId)
    print ('You are deleting deal \"{}\" with ID {} ').format(deal.name, dealId)
    deal.delete()
    print('The deal with the ID {} has been deleted.').format(dealId)

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

Highrise.set_server('sunlime')
Highrise.auth('4572ff2d6932dabc5e4a9e905b60ae45')

from file dealInitialActionSet import dealInitialActionSet

#Start of programm
# print ('What do you want to do with your deal?')
# print ('Enter 0 for adding a deal.')
# print ('Enter 1 for updating a deal.')
# print ('Enter 2 for deleting a deal.')
# print ('Blank for quit.')

# dealAction = input()

# deals = Deal.all()
# for deal in deals:
#  print ('deal name = ') + deal.name + (' ') + ('deal id = ') + str(deal.id) + (' ') + ('deal category id = ') + str(deal.category_id)

#dealInitialActionSet()
while running:
  initialValue = dealInitialActionSet()
  dealAction = dealActionSet(initialValue)
  quit = raw_input('Quit program? y for quit, n for continue : ')
  if quit == 'y':
    print ('Thank you for using my script! Have a good day!')
  else:
    print ('Let\'s continue')
else:
  print ('copyright by Sunlime Web Innovations GmbH, 2017')
