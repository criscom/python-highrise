from pyrise import *

def getAllDeals():
  deals = Deal.all()
  for deal in deals:
    print ('deal name = ') + deal.name + (' ') + ('deal id = ') + str(deal.id) + (' ') + ('deal category id = ') + str(deal.category_id)

Highrise.set_server('sunlime')
Highrise.auth('4572ff2d6932dabc5e4a9e905b60ae45')
deals = Deal.all()
print '\n' + ('Getting all Deals for you ...') + '\n'
print('This is your list of deals:') + '\n' + '==================================================='
for deal in deals:
  print ('deal id = ') + str(deal.id) + '\n' + ('deal name = ') + deal.name + (' // ') + ('deal category id = ') + str(deal.category_id) + (' // ') + ('deal status = ') + str(deal.status) + (' // ') + '\n' + '==================================================='
