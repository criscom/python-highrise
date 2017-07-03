#! python 2
# sunlime-deals.py - manage deals via api

from pyrise import *

# Set highrise variables
deal = Deal()
dealResponsible = 0
dealId = 0
dealAction = 0
# 0 = add
# 1 = update
# 2 = delete

# Set general variables
dealResponsible = 0
dealId = 0
dealAction = 0
sunlimeId = 0

# Set user IDs
christophId = 60274790
dominikId = 49290195
nicoleId = 61332931

# What do you wnat to do with your deal? function
# Set deal action
def dealActionSet(dealAction):
  if dealAction == 0:

    print('You are now adding a new deal.')
    print('Next, give the deal a name: e.g. Angebot-105340: A good, descriptive Name')

    # Set deal name
    dealName = raw_input()
    deal.name = (dealName)

    print ('Thank you! The name of the deal is: {}').format(dealName)

    print('Who is responsible for the deal')
    print('Enter \"1\" for Nicole Pfeiffer')
    print('Enter \"2\" for Dominik Fuchshofer')
    print('Enter \"3\" for Christoph Potzinger')

    # Set responsible person
    dealResponsibleSet(dealResponsible)
    print ('2. The highrise ID of Nicole is {}').format(deal.responsible_party_id)


  elif dealAction == 1:
    print ({dealAction})

  elif dealAction == 2:
    print ({dealAction})

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

  # Whos is responsible?
  dealResponsible = input()

  if dealResponsible in range(1, 3):
    if dealResponsible == 1:
      print ('You have entered {} and set Nicole as responsible for the deal').format(dealResponsible)
      deal.responsible_party_id = nicoleId
      print ('The highrise ID of Nicole is {}').format(deal.responsible_party_id)


    elif dealResponsible == 2:
      deal.responsible_party_id = dominikId

    elif dealResponsible == 3:
      deal.responsible_party_id = christophId

  else:
    print ('Your selection cannot be assigned to one of the administrators. Please choose 1, 2 or 3')
    dealResponsibleSet(dealResponsible)


Highrise.set_server('sunlime')
Highrise.auth('4572ff2d6932dabc5e4a9e905b60ae45')

print ('What do you want to do with your deal?')
print ('Enter 0 for adding a deal.')
print ('Enter 1 for updating a deal.')
print ('Enter 2 for deleting a deal.')
print ('Blank for quit.')

dealAction = input()
dealActionSet(dealAction)
