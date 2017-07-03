#! python 2
# sunlime-deals.py - manage deals via api

from pyrise import *

def dealResponsibleSet:
  dealResponsible = int(input())
    for dealResponsible in range(1, 3):
      if dealResponsible == 1:
        deal.responsible_party_id = NicoleId

      elif dealResponsible == 2:
        deal.responsible_party_id = DominikId

      elif dealResponsible == 3:
        deal.responsible_party_id = ChristophId

    print('Your selection cannot be assigned to one of the administrators. Please choose 1, 2 or 3')
        dealResponsibleSet


def dealActionSet(dealAction):
  if dealAction == 0:
    deal = Deal()

    print('Give the deal a name: e.g. Angebot-105340: A good, descriptive Name')
    dealName = input()

    deal.name = strg(dealName)

    print('Who is responsible for the deal')
    print('Enter \"1\" for Nicole Pfeiffer')
    print('Enter \"2\" for Dominik Fuchshofer')
    print('Enter \"3\" for Christoph Potzinger')



  elif dealAction == 1:
    print ({dealAction})

  elif dealAction == 2:
    print ({dealAction})

  elif dealAction == '':

  else:
    print('You haven\'t entered a correct number')
    print('Enter 0 for adding a deal.')
    print('Enter 1 for updating a deal.')
    print('Enter 2 for deleting a deal.')
    print('Blank for quit.')
    dealAction = input()

ChristophId = 60274790
DominikId = 49290195
NicoleId = 61332931

dealResponsible = 0
dealId = 0
dealAction = 0
# 0 = new
# 1 = update
# 2 = delete

Highrise.set_server('sunlime')
Highrise.auth('4572ff2d6932dabc5e4a9e905b60ae45')

print('What do you want to do with your deal?')
print('Enter 0 for adding a deal.')
print('Enter 1 for updating a deal.')
print('Enter 2 for deleting a deal.')
print('Blank for quit.')

dealAction = input()
dealActionSet

