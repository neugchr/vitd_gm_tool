#monster.py
from dice import roll
from random import randint
from random import choices
import item
import re

class Character:
	# those are the default keys, those items will appear in this order by printing
	keys = ['name', 'description', 'level',
			'hit_dice', 'hit_points',
			'damage', 'attack', 'natural_armour', 'defense',
			'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma',
			'equipment_slots','ability']
	
	def __init__(self, **kwargs):
		self._attr = {}
		for k, v in kwargs.items():
			self._attr[k] = v
		# auto populate all fields that are not passed to the constructor
		for (k, v) in {'name': 'character',
					   'description': 'a humble player on the stage of life',
					   'level': -1,
					   'hit_dice': '1d8',
					   'hit_points': -1,
					   'strength': '4d3-8',
					   'dexterity': '4d3-8',
					   'constitution': '4d3-8',
					   'intelligence': '4d3-8',
					   'wisdom': '4d3-8',
					   'charisma': '4d3-8',
					   'damage': '1d6',
					   'attack': 0,
					   'natural_armour': 'none',
					   'defense': 0,
					   'equipment_slots': -1,
					   'ability': 'none'
					  }.items():
			if k not in kwargs.keys():
				self._attr[k] = v
		# roll the attributes and determine lvl if it is not given yet
		for (k, v) in self._attr.items():
			if k in ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma'] and type(v) != int:
				self._attr[k] = int(float(roll(v)['result']))
			elif k == 'level' and v == -1:
				self._attr[k] = re.search('([0-9]*)(?:[dDwW]{1}(?!0))([0-9]+)',
								   self._attr['hit_dice']).group(1)
		# now we need to populate all derived statistics
		for (k, v) in self._attr.items():
			if k == 'hit_points' and v == -1:	# if hp were not in kwargs they're -1 and need to be rolled
				self._attr['hit_points'] = int(float(roll(self._attr['hit_dice'])['result']))
			elif k == 'equipment_slots' and v == -1:
				self._attr[k] = self._attr['strength']+self._attr['constitution']+6
				if self._attr[k] < 1:
					self._attr[k] = 1
			elif k =='attack':
				self._attr[k] = (int(float(self._attr['strength']))+11+int(float(self._attr['level'])))
			elif k == 'defense':
				self._attr[k] = (int(float(self._attr['dexterity']))+11+int(float(self._attr['level'])))
	
	def __getitem__(self, key):
		return(self._attr[str(key)])
	
	def __setitem__(self, key, value):
		self._attr[str(key)] = value
	
	def __iter__(self):
		return(CharacterIterator(self))
	
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
		for k in Character.keys:
			try:
				if k == 'name' or k == 'description':
					ostr += str(self._attr[k]+'\n')
				elif k in ['level', 'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']:
					ostr += str(k).replace('_',' ')+': '+str(self._attr[k])+'\n'
				else:
					ostr += str(k).replace('_',' ')+': '+str(self._attr[k])+'\n'
			except:
				pass
		# then we again iterate over the content but omit everything we already have
		for k,v in self._attr.items():
			if k not in Character.keys:
				ostr += str(k).replace('_',' ')+': '+str(self._attr[k])+'\n'
		return(ostr)



class CharacterIterator():
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
# NPCs and MONSTERS (implementes as character classes)
########################################

class Bandit(Character):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'bandid',
					   'description': 'Coldhearted or desperate, they prey upon those weaker than themselves. Will retreat at half health.',
					   'hit_dice': '2d8',
					   'damage': '1d6-2'
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)
		# give it a 3 in 4 chance to wear light armour
		if randint(1,4) < 4:
			self._attr['armour'] = item.choose_random_light_armour()
		self._attr['weapon'] = item.choose_random_weapon()
		self._attr['offhand'] = item.choose_random_offhand()
		if ( type(self._attr['weapon']) != type(item.Sword())
			 and type(self._attr['weapon']) != type(item.Dagger())
			 and type(self._attr['weapon']) != type(item.Greatsword())
			 and type(self._attr['offhand']) != type(item.Dagger())
		   ):
			self._attr['sidearm'] = item.choose_random_sidearm()


class Traveler(Character):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'traveler',
					   'description': 'A traveler through the vast. 2/6 chance to fight to the death otherwise will retreat at half health.',
					   'hit_dice': '3d8',
					   'damage': '1d6-2'
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)
		# give it a 3 in 4 chance to wear mail armour
		if randint(1,4) < 4:
			self._attr['armour'] = item.MailArmour()
		else:
			self._attr['armour'] = item.choose_random_light_armour()
		self._attr['weapon'] = item.choose_random_weapon()
		self._attr['offhand'] = item.choose_random_offhand()
		if ( type(self._attr['weapon']) != type(item.Sword())
			 and type(self._attr['weapon']) != type(item.Dagger())
			 and type(self._attr['weapon']) != type(item.Greatsword())
			 and type(self._attr['offhand']) != type(item.Dagger())
		   ):
			self._attr['sidearm'] = item.choose_random_sidearm()


class Cutthroat(Character):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'cutthroat',
					   'description': 'Cruel looters. 2/6 chance to fight to the death otherwise will retreat at half health.',
					   'hit_dice': '3d8',
					   'damage': '1d6-2'
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)
		# give it a 3 in 4 chance to wear mail armour
		if randint(1,4) < 4:
			self._attr['armour'] = item.MailArmour()
		else:
			self._attr['armour'] = item.choose_random_light_armour()
		self._attr['weapon'] = item.choose_random_weapon()
		self._attr['offhand'] = item.choose_random_offhand()
		if ( type(self._attr['weapon']) != type(item.Sword())
			 and type(self._attr['weapon']) != type(item.Dagger())
			 and type(self._attr['weapon']) != type(item.Greatsword())
			 and type(self._attr['offhand']) != type(item.Dagger())
		   ):
			self._attr['sidearm'] = item.choose_random_sidearm()


class Magus(Character):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'traveler',
					   'description': 'A dabbler in magical powers',
					   'hit_dice': '3d8',
					   'damage': '1d6-2'
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)
		# give it a 3 in 4 chance to wear light
		if randint(1,4) < 4:
			self._attr['armour'] = item.choose_random_light_armour()
		self._attr['weapon'] = item.Chisel()






