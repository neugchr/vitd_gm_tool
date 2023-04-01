from dice import roll
from random import randint
from random import choices
import item
import monster


class Encounter:
	# those are the default keys, those items will appear in this order by printing
	keys = ['name', 'description', 'depth',
			'characters', 'loot']
	
	def __init__(self, **kwargs):
		self._attr = {}
		for k, v in kwargs.items():
			self._attr[k] = v
		# auto populate all fields that are not passed to the constructor
		for (k, v) in {'name': 'encounter',
					   'description': 'an encounter',
					   'depth': 0,
					   'characters': [],
					   'loot': []
					  }.items():
			if k not in kwargs.keys():
				self._attr[k] = v
	
	def __getitem__(self, key):
		return(self._attr[str(key)])
	
	def __setitem__(self, key, value):
		self._attr[str(key)] = value
	
	def __iter__(self):
		return(EncounterIterator(self))
	
	def __contains__(self, key):
		if key in self._attr:
			return(True)
		else:
			return(False)
	
	def __len__(self):
		return(len(self._attr))
	
	def __repr__(self):
		return(self.__str__())
	
	def __str__(self):
		ostr = ''
		# at first we add all the items in the defalt list
		for k in Encounter.keys:
			try:
				if k == 'name' or k == 'description':
					ostr += str(self._attr[k]+'\n')
				else:
					ostr += str(k).replace('_',' ')+': '+str(self._attr[k])+'\n'
			except:
				pass
		# then we again iterate over the content but omit everything we already have
		for k,v in self._attr.items():
			if k not in Encounter.keys:
				ostr += str(k).replace('_',' ')+': '+str(self._attr[k])+'\n'
		return(ostr)



class EncounterIterator():
	def __init__(self, item):
		self._item = item
		self._index = 0
	
	def __next__(self):
		if self._index < len(self._item._attr):
			k = list(self._item._attr.keys())[self._index]
			result=(k,self._item._attr[k])
		else:
			raise StopIteration
		self._index += 1
		return(result)

		
########################################
# ENCOUNTERS
########################################

class LostTraveler(Encounter):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'lost traveler',
					   'description': 'A lost traveler. Needs food and shelter. Helpful if assisted.',
					   'characters': [monster.Traveler()]
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)
		if randint(1,6) == 6:
			self._attr['loot'].append(item.choose_random_artifact(self._attr['depth']))


class Bandits(Encounter):
	def __init__(self, **kwargs):
		characterbuffer = []
		for n in range(randint(1,6)):
			characterbuffer.append(monster.Bandit())
		
		for (k, v) in {'name': 'Bandits',
					   'description': ('Bandits, demand a ration for each of them '
											+'or 100 lodestone. Willing to kill, but '
											+'flees if the battle is lost.'
									  ),
					   'characters': characterbuffer
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class FeverishFaithful(Encounter):
	def __init__(self, **kwargs):
		for (k,v) in {'name': 'Feverish Faithful',
					   'description': ('Feverish Faithful - Penitent worshippers pray to whatever entity for forgivness and guidance. '
											  +'They are clearly not in their right minds and will attack when disturbed.'
											  +'\nThere is '+str(randint(1,20))+' of them.'
									  ),
					   'characters': [monster.Bandit(name='Faithful',
													 description=('A troubled soul praying to some otherworldly entity for salvation.'),
													 level=2,
													 hit_dice='2d8',
													 hit_points=9,
													 strength=0,
													 dexterity=0,
													 constitution=0,
													 intelligence=0,
													 wisdom=0,
													 charisma=0,
													 damage=0
												 )]
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)

	
########################################
# Helper functions
########################################
def choose_random_encounter(depth=0, location='ruins'):	#location: ruins wastes pillars
	if location == 'ruins':
		r = randint(1,10)+depth
	elif location == 'wastes':
		r = randint(1,10)
	else:
		r = randint(-1,-10)
	#print(r)
	if r > 0 and r <= 5:
		return('nothing')
	elif r == 6:
		return(LostTraveler(depth=depth))
	elif r == 7:
		return('loadstone broker')
	elif r == 8:
		return('bandits')
	elif r == 9:
		return('Lodestone Prospectors')
	elif r <=12:
		return('1d6 cyclops')
	elif r == 13:
		return('1d6 cutthroats')
	elif r == 14:
		return('1d8 waning lodge initiates')
	elif r <= 16:
		return('1d3 Medusa')
	elif r == 17:
		return('griffon')
	elif r == 18:
		return('1d8 delvers')
	elif r == 19:
		return('lone survivor')
	else:
		return('The Wyrm')
