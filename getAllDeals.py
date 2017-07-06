def getAllDeals():
  deals = Deal.all()
  for deal in deals:
    print ('deal name = ') + deal.name + (' ') + ('deal id = ') + str(deal.id) + (' ') + ('deal category id = ') + str(deal.category_id)