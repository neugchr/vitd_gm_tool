from random import randint
def mood():
  i = randint(1,4)
  if i == 1:
    print('peacful but sullen')
  elif i == 2:
    print('quiet but anxious')
  elif i == 3:
    print('active but desperate')
  else:
    print('mirthful but pained')

def who():
  i = randint(1,6)
  if i == 1:
    print('merchants and brokers')
  elif i == 2:
    print('storytellers and singer')
  elif i == 3:
    print('warriors and cutthroats')
  elif i == 4:
    print('artisans and craftsmen')
  elif i == 5:
    print('prophets and philosophers')
  else:
    print('explorers and cartographers')

def have():
  i = randint(1,8)
  if i == 1:
    print('a working smithy')
  elif i == 2:
    print('collections of maps')
  elif i == 3:
    print('a reservoir of water')
  elif i == 4:
    print('hunting grounds')
  elif i == 5:
    print('stores of loadstone')
  elif i == 6:
    print('a well-known bazar')
  elif i == 7:
    print('an armory of tools and weapons')
  else:
    print('a dangerous artifact')


def prominence():
  i = randint(1,10)
  if i == 1:
    print('magus, with books for sale')
  elif i == 2:
    print('dervish, with a coat of blades')
  elif i == 3:
    print('masque, whispers secrets')
  elif i == 4:
    print('boot seller, none are pairs')
  elif i == 5:
    print('pyromancer, jars of fire to use')
  elif i == 6:
    print('scrollmaster, deals in spells')
  elif i == 7:
    print('black helm, dangerous rouge')
  elif i == 8:
    print('wastecrier, delivers news')
  elif i == 9:
    print('Nod, smiles and never speaks')
  else:
    print('Flutist, songs return memories')


def problem():
  i = randint(1,12)
  if i == 1:
    print('Food will soon run out')
  elif i == 2:
    print('water has been vanishing')
  elif i == 3:
    print('locals are disappearing')
  elif i == 4:
    print('metal is scarce')
  elif i == 5:
    print('tools are rusting away')
  elif i == 6:
    print('a political schism')
  elif i == 7:
    print('the complex is collapsing')
  elif i == 8:
    print('a great death has occured')
  elif i == 9:
    print('someone is a murderer')
  elif i == 10:
    print('an artifact in the ruins stirs')
  elif i == 11:
    print('dangerous beliefs arise')
  else:
    print('crawl have moved in')


def settlement():
  mood()
  who()
  have()
  prominence()
  problem()