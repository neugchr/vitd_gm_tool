import monster
import item
from random import choices
from random import randint

class Pixie(monster.Character):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'pixie',
					   'description': ('A wee little pixie flying around.'),
					   'hit_dice': '1d4',
					   'hit_points': -1,
					   'strength': '-3',
					   'dexterity': '3',
					   'constitution': '0',
					   'intelligence': '2d3-3',
					   'wisdom': '1d3-1',
					   'charisma': '2d3-2',
					   'damage': '1d3',
					   'natural_armour': 'none',
					   'ability': ('can fly')
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)
		if randint(1,4) < 3:
			self._attr['armour'] = item.choose_random_light_armour()
		# give it a 1 in 8 chance to have a random piece of equipment
		if randint(1,4) == 1:
			self._attr['loot'] = item.choose_random_miscellania()
		if randint(1,4) == 1:
			self._attr['loot'] = item.choose_random_miscellania()


